import scrapy
from apteka.items import AptekaItem

class aptekaSpider(scrapy.Spider):
    name = "apteka"
    allowed_domains = ['aptekaplus.kz']
    
    def start_requests(self):
        urls = [
            'https://aptekaplus.kz/catalog/med/lekarstvennye-sredstva/section'
            # 'https://aptekaplus.kz/catalog/main/sanitariya-i-gigiena/section',
            # 'https://aptekaplus.kz/catalog/main/retseptura-i-pitanie/section',
            # 'https://aptekaplus.kz/catalog/main/mama-i-rebenok/section',
            # 'https://aptekaplus.kz/catalog/main/detskoe-pitanie/section',
            # 'https://aptekaplus.kz/catalog/main/credstva-dlya-reabilitatsii/section',
            # 'https://aptekaplus.kz/catalog/main/bandazhi-i-kompressionnoe-bele/section'
            # 'https://aptekaplus.kz/catalog/main/meditsinskie-tovary/section',
            # 'https://aptekaplus.kz/catalog/main/meditsinskaya-tekhnika/section',
            # 'https://aptekaplus.kz/catalog/main/kosmetika/section',
            # 'https://aptekaplus.kz/catalog/main/optika/section',
            # 'https://aptekaplus.kz/catalog/main/kafeplyus/section'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.open_small_category, meta = {
                  'dont_redirect': True,
                  'handle_httpstatus_list': [302]
              })

    def open_small_category(self,response):
        item = AptekaItem() 
        item['high_category'] = response.css('h1.bx_catalog_line_category_title::text').get().strip()
        for link in response.css('ul.bx_catalog_line_ul a'):
            item['small_category'] = link.css('::text').get().strip()
            the_link = link.css('::attr(href)').get()
            yield response.follow(the_link, callback = self.open_item, meta={'high_category': item['high_category'],'small_category':item['small_category']})

    def open_item(self,response):
        item = AptekaItem() 
        item['high_category'] = response.meta.get('high_category')
        item['small_category'] = response.meta.get('small_category')
        for product in response.css('div.product-item-title a::attr(href)'):
            product_link = product.get()
            item['prod_link'] = product_link
            yield response.follow("https://aptekaplus.kz" + product_link, callback=self.parse_item, meta={'high_category': item['high_category'],
            'small_category':item['small_category'],'prod_link':item['prod_link']})
        
        next_page = response.css('li.bx-pag-next a::attr(href)').get()
        if next_page is not None:
            url= "https://aptekaplus.kz"+next_page
            yield response.follow(url, callback=self.open_item, meta={'high_category': item['high_category'],'small_category':item['small_category']})

    def parse_item(self, response):
        item = AptekaItem()             
        item['high_category'] = response.meta.get('high_category') 
        item['small_category'] = response.meta.get('small_category') 
        item['prod_link'] = "https://aptekaplus.kz" + response.meta.get('prod_link') 

        item['name'] = response.css('h1::text').get().strip()
        the_price = response.css('span.current-price__value::text').get()
        if the_price is not None:
            item['price'] = the_price.replace('тг.','').strip()
        else:
            item['price'] = ''
        #The images download part. 
        picture = response.css('div.slider_switch.product-item-detail-slider-image').css('img ::attr(src)').getall()
        #this is for lekarstvennye-sredstva category
        default = '/local/templates/aptekaplus_template/components/bitrix/catalog.element/lek/images/no_photo.png'
        #this is for other categories, enable it when uncomment other categories 
        # default = '/local/templates/aptekaplus_template/components/bitrix/catalog.element/.default/images/no_photo.png'          
        picture_list = []
        if default not in picture:
            for i in range(len(picture)):
                picture_list.append("https:"+picture[i])s
            item['image_urls'] = picture_list
        else:
            item['image_urls'] = ''

        item['image_link'] = [item['sku']+ '_' + str(index) + '.jpg' for index, x in enumerate(item['image_urls'], start = 1)]
        
        #Specifications part
        d = {}
        for m in response.css('div#tab2block'):
            key = []
            for i in m.css('p b::text').getall():
                i = i.replace(':','').strip()
                key.append(i)
            value = m.css('p span::text').getall()
            d = dict(zip(key, value))
        
        item['sku'] = list(d.values())[0]
        main_dict = {}
        for i in range(3,8):
            if response.css(f'button#tab{i}::text').get() != None:
                names = response.css(f'button#tab{i}::text').get().strip()
            else:
                names = ''
            if response.css(f'div#tab{i}block p::text').get() != None:
                spec = response.css(f'div#tab{i}block p::text').get().replace('\n','').strip()
            else:
                spec = ''
            main_dict[names] = spec
        fin_dict = {}
        fin_dict.update(d)
        fin_dict.update(main_dict)
        item['specification'] = fin_dict
        the_description = response.css('div#tab1block p::text').get()
        if the_description is not None:
            item['description'] = the_description.strip()
        else:
            item['description'] = ''
        yield item

