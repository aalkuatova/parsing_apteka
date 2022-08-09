
from scrapy.pipelines.images import ImagesPipeline
import urllib


class AptekaPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        for index, image_url in enumerate(item['image_urls'],start = 1):
            urllib.request.urlretrieve(image_url, f"images_folder/{item['sku']}_{str(index)}.jpg")
        return item
