import json
import graphic as gp
import webScraping as ws
import readPortfolio as rp
import readMajorIndices as rm

def compass():
    loop = True
    while loop:
        try:
            scrapy = ws.webScraping()
            if (scrapy == 'Success'):
                print ('Success webScraping')
                loop = False
            else:
                print ('Error em WebScraping')
            
            rp.portfolio()
            rm.majorIndices()
            gp.graphic()

            with open('dadosGraphic.json', 'r') as arq:
                dadosGraphic = json.load(arq)
        except:
            print('Error em Compass')

    return dadosGraphic
