from myApp.models import *

def getAllGoods():
    return Products.objects.all()