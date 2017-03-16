
BOT_NAME = 'LJSpider'

SPIDER_MODULES = ['LJSpider.spiders']
NEWSPIDER_MODULE = 'LJSpider.spiders'

ITEM_PIPELINES = {
    'LJSpider.pipelines.MongoPipeline':505
}


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

