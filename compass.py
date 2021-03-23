import graphic as gp
import webScraping as ws
import readPortfolio as rp
import readMajorIndices as rm

while True:
    try:
        scrapy = ws.webScraping()
        rp.portfolio()
        rm.majorIndices()
        gp.graphic()
        if (scrapy == 'Success'):
            print ('Success')
        else:
            print ('Error em WebScraping')
    except:
        print('Error em Compass')