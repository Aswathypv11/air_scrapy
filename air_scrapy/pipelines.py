# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from twisted.enterprise import adbapi
import sys
import MySQLdb.cursors
from scrapy import log
#from scr_l_mysql.settings import MYSQL 
from scrapy.conf import settings

class MysqlInsert(object):
    def __init__(self):
        # Connect to database
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host        = settings['MYSQL_HOST'],
            db          = settings['MYSQL_DB'],
            user        = settings['MYSQL_USER'],
            passwd      = settings['MYSQL_PASS'],
            cursorclass = MySQLdb.cursors.DictCursor,
            charset     = 'utf8', use_unicode=True
        )
   
    def process_item(self, item, spider):
        """Insert the item to the database, handle the errors if it fails"""
        
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._insert, item)
            
        query.addErrback(self.handle_error)
        return item

    def _insert(self, tx, item):
        """
        Insert the item to the modules and slots table. Should any of the
        intermediate transactions fail, it will rollback the query.
        """
        
       
	tx.execute(
	"insert into av_meterology (Station, DateAT, TimeAT, AmbientTemperature, DateBP, TimeBP,BarometricPressure, DatePM10, TimePM10, ParticulateMatterless10, DatePM2, TimePM2, ParticulateMatterless2, DateRH, TimeRH, RelativeHumidity, DateSR, TimeSR, SolarRadiation, DateVW, TimeVW, VerticalWindSpeed, DateHW, TimeHW, HorizontalWindSpeed, DateWD, TimeWD, WindDirection)"
	"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (item['col1'][0],item['col2'][2],item['col3'][1],item['col4'][1],item['col5'][1],item['col6'][1],item['col7'][1],item['col8'][2],item['col9'][1],item['col10'][1],item['col11'][2],item['col12'][1],item['col13'][1],item['col14'][1],item['col15'][1],item['col16'][1],item['col17'][1],item['col18'][1],item['col19'][1],item['col20'][1],item['col21'][1],item['col22'][1],item['col23'][1],item['col24'][1],item['col25'][1],item['col26'][1],item['col27'][1],item['col28'][1]))

	tx.execute(
	"insert into av_pollutants (Station, DateAm, TimeAm, Ammonia, DateBe, TimeBe, Benzene, DateCa, TimeCa, CarbonMonoxide, DateND, TimeND, NitrogenDioxide, DateNO, TimeNO, NitrogenOxide, DateON, TimeON, OxidesofNitrogen, DatepX, TimepX, pXylene, DateSD, TimeSD, SulphurDioxide, DateTo, TimeTo, Toluene)"
	"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (item['col1'][0],item['col2'][1],item['col3'][0],item['col4'][0],item['col5'][0],item['col6'][0],item['col7'][0],item['col8'][0],item['col9'][0],item['col10'][0],item['col11'][1],item['col12'][0],item['col13'][0],item['col14'][0],item['col15'][0],item['col16'][0],item['col17'][0],item['col18'][0],item['col19'][0],item['col20'][0],item['col21'][0],item['col22'][0],item['col23'][0],item['col24'][0],item['col25'][0],item['col26'][0],item['col27'][0],item['col28'][0]))
         
      
        

            # Database transaction complete!
        log.msg("Item stored in db: %s" % item, level=log.DEBUG)
        #return query
    
    def handle_error(self, e):
           """Handles any errors in the database query."""
           log.err(e)
		
