from .getBaseData import *
from myApp.models import *

def getChangeList():
    goods = list(getAllGoods())
    goodsType =[]
    goodsCity = []
    for i in goods:
        goodsType.append(i.type)
        goodsCity.append(i.address)
    goodsType = list(set(goodsType))
    goodsCity = list(set(goodsCity))
    return goodsType, goodsCity

def getSummaryData(city,type):
    if type == "不限" and city == "不限":
        goods = list(getAllGoods())
    elif city == "不限":
        goods = Products.objects.filter(type=type)
    elif type == "不限":
        goods = Products.objects.filter(address= city)
    else:
        goods = Products.objects.filter(type=type, address= city)
    goodsData= []
    for i in goods:
        goodsData.append({
            "id":i.id,
            "type":i.type,
            "title":i.title,
            "price":i.price,
            "buy_len":i.buy_len,
            "img_src":i.img_src,
            "name":i.name,
            "address":i.address,
            "isFreeDelivery":i.isFreeDelivery,
            "href":i.href,
            "nameHref":i.nameHref
        })
    return goodsData