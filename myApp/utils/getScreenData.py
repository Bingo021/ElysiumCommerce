from .getBaseData import *

def getSquareData():
    goods = list(getAllGoods())
    goodsVolumn = {}
    for i in goods:
        if goodsVolumn.get(i.address,-1):
            goodsVolumn[i.address] = int(i.buy_len)
        else:
            goodsVolumn[i.address] += int(i.buy_len)
    goodsSortVolumn = sorted(goodsVolumn.items(), key=lambda x:x[1], reverse=True)
    cityList =[]
    volumnList=[]
    for i in goodsSortVolumn:
        cityList.append(i[0])
        volumnList.append(i[1])
    return cityList[:7], volumnList[:7]
def getPieData():
    goods = list(getAllGoods())
    goodsNumeber= {}
    for i in goods:
        if goodsNumeber.get(i.type,-1) ==-1:
            goodsNumeber[i.type] = 1
        else:goodsNumeber[i.type] += 1
    pieList = []
    for k,v in goodsNumeber.items():
        pieList.append({
            'name':k,
            'value':v
        })
    return pieList
def getMapData():
    goods = list(getAllGoods())
    cityVolumn={}
    for i in goods:
        if cityVolumn.get(i.address,-1) ==-1:
            cityVolumn[i.address] = 1
        else:
            cityVolumn[i.address] +=1
    mapData= []
    for k,v in cityVolumn.items():
        mapData.append({
            'name':k,
            'value':v
        })
    return mapData
def getLineData():
    goods = list(getAllGoods())
    priceDict = {'0-100':0, '100-200':0, '200-500':0, '500-1000':0, '>1000':0}
    for i in goods:
        p =float(i.price)
        if p<100:
            priceDict['0-100']+=1
        elif p>=100 and p<200:
            priceDict['100-200']+=1
        elif p>=200 and p<500:
            priceDict['200-500']+=1
        elif p>=500 and p<1000:
            priceDict['500-1000']+=1
        else:
            priceDict['>1000']+=1
    lineRowData = list(priceDict.keys())
    lineColData = list(priceDict.values())
    return lineRowData,lineColData
def getRosePieData():
    goods = list(getAllGoods())
    salesVolumn={}
    for i in goods:
        if salesVolumn.get(i.type, -1):
            salesVolumn[i.type] = int(i.buy_len)
        else:
            salesVolumn[i.type] += int(i.buy_len)
    salesSortVolumn = sorted(salesVolumn.items(), key=lambda x: x[1], reverse=True)
    rosePieData=[]
    for k,v in salesSortVolumn:
        rosePieData.append({
            'name':k,
            'value':v
        })
    return rosePieData[:10]