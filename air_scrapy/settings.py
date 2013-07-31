# Scrapy settings for scr_l_mysql project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scr_l_mysql'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scr_l_mysql.spiders']
NEWSPIDER_MODULE = 'scr_l_mysql.spiders'
DEFAULT_ITEM_CLASS = 'scr_l_mysql.items.ScrLMysqlItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = [
        #'scr_l_mysql.SanitizeDataPipeline.SanitizeDataPipeline',
	'scr_l_mysql.pipelines.MysqlInsert',
	]

MYSQL_HOST  = "127.0.0.1"
MYSQL_USER  = "---"
MYSQL_PASS  = "---"
MYSQL_DB    = "---"

