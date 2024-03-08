from django.http import JsonResponse
from .utils import getScreenData
from .utils import getSummaryData

# Create your views here.
def screenData(request):
    if request.method == "GET":
        cityList, volumnList = getScreenData.getSquareData()
        pieList = getScreenData.getPieData()
        mapData = getScreenData.getMapData()
        lineRowData,lineColData = getScreenData.getLineData()
        rosePieData = getScreenData.getRosePieData()
        return JsonResponse({
            "cityList": cityList,
            "volumnList": volumnList,
            "pieList": pieList,
            "mapData": mapData,
            "lineRowData": lineRowData,
            "lineColData": lineColData,
            "rosePieData":rosePieData
        })

def summary(request):
    if request.method == "GET":
        goodsType, goodsCity = getSummaryData.getChangeList()
        city = "不限"
        type = "不限"
        if request.GET.get("city"):city = request.GET.get("city")
        if request.GET.get("type"):type = request.GET.get("type")
        # print(city,type)
        goodsData = getSummaryData.getSummaryData(city,type)
        return JsonResponse({
            "goodsType": goodsType,
            "goodsCity":goodsCity,
            "goodsData":goodsData,
        })