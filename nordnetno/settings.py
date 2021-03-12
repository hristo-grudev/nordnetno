BOT_NAME = 'nordnetno'

SPIDER_MODULES = ['nordnetno.spiders']
NEWSPIDER_MODULE = 'nordnetno.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 2

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'nordnetno.pipelines.NordnetnoPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
