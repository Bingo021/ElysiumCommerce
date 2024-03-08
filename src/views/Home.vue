<template>
    <div class="layout">
        <div class="header">
            <dv-decoration-8 style="width:300px;height:50px;" />
            <div>
                <span class="title-text">大数据可视化平台</span>
                <dv-decoration-5 style="width:300px;height:40px;" />
            </div>
            <dv-decoration-8 :reverse="true" style="width:300px;height:50px;" />
        </div>
        <div class="content">
            <div class="left">
                <dv-border-box-13>
                    <dv-decoration-1 style="width:300px;height:12px;" />
                    <div ref="firstMain" style="width: 360px;height:320px;margin: 20px auto;"
                        v-bind:key="realData.volumnList[0]" @mouseenter="startAction" @mouseleave="cancelAction"></div>
                </dv-border-box-13>
                <dv-border-box-8>
                    <div ref="secondMain" style="width: 360px;height:320px;margin: 20px auto;"
                        v-bind:key="realData.pieList[0][1]"></div>
                </dv-border-box-8>
            </div>
            <div class="center">
                <div ref="thirdMain" style="width: 670px;height: 670px;margin: 0px auto;" v-bind:key="realData.mapData[0][1]"></div>
            </div>
            <div class="right">
                <dv-border-box-12>
                    <dv-decoration-3 style="width:300px;height:12px;" />
                    <div ref="fourthMain" style="width: 380px;height:320px;margin: 20px auto;"
                        v-bind:key="realData.lineColData[1]"></div>
                </dv-border-box-12>
                <dv-border-box-1>
                    <div ref="fifthMain" style="width: 360px;height: 320px;margin: 20px auto;"
                        v-bind:key="realData.rosePieData[0][1]"></div>
                </dv-border-box-1>
            </div>
        </div>
    </div>
</template>

<script>
import getMap from '@/api/getMap.js';
export default {
    data() {
        return {
            isHovered: 'true',
            realData: {
                cityList: [1],
                volumnList: [1],
                pieList: [{ name: "data1", value: 10 }],
                mapData: [{ name: "data2", value: 10 }],
                lineRowData: [1],
                lineColData: [1],
                rosePieData: [{ name: "data3", value: 10 }]
            }
        }
    },
    methods: {
        drawLeftTop() {
            var myChart = this.$echarts.init(this.$refs.firstMain)
            var option = {
                xAxis: {
                    type: 'category',
                    data: this.realData.cityList,
                    axisLabel: {
                        textStyle: {
                            color: '#C0C0C0',
                        }
                    }
                },
                dataZoom: [
                    {
                        type: "slider",
                        start: 0,
                        end: 90,
                        show: false
                    }
                ],
                title: {
                    text: "各地区销售数据",
                    textStyle: {
                        color: "#C0C0C0"
                    }
                },
                toolbox: {
                    show: true,
                    feature: {
                        magicType: { show: true, type: ["line", "bar"] },
                        restore: { show: true },
                        saveAsImage: { show: true },
                    }
                },
                legend: {
                    orient: "vertical",
                    left: "left",
                    data: ["销售数据"],
                    textStyle: {
                        color: "#C0C0C0",
                    },
                    top: "8%",
                    left: "70%"
                },
                tooltip: {
                    trigger: "item",
                    formatter: ""
                },
                yAxis: {
                    type: 'value',
                    axisLabel: {
                        textStyle: {
                            color: '#C0C0C0',
                        }
                    }
                },
                series: [
                    {
                        name: "销售数据",
                        data: this.realData.volumnList,
                        type: 'bar',
                        label: {
                            show: true,
                            position: "inside",
                            textStyle: {
                                color: "#C0C0C0"
                            }
                        }
                    }
                ]
            }
            option && myChart.setOption(option);
        },
        drawLeftBottom() {
            var myChart = this.$echarts.init(this.$refs.secondMain)
            var option = {
                title: {
                    text: '各类型商品占比',
                    subtext: '',
                    left: 'right',
                    textStyle: {
                        color: "#C0C0C0"
                    }
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    textStyle: {
                        color: "#C0C0C0"
                    }
                },
                series: [
                    {
                        name: '数量',
                        type: 'pie',
                        radius: '50%',
                        data: this.realData.pieList,
                        center: ["60%", "60%"],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            };
            option && myChart.setOption(option);
        },
        async drawCenterMap() {
            var myChart = this.$echarts.init(this.$refs.thirdMain)
            const res = await getMap
            this.$echarts.registerMap('china', res.data)
            var data = this.realData.mapData
            var geoCoordMap = {
                上海: [121.472644, 31.231706],
                云南: [102.712251, 25.040609],
                内蒙古自治区: [111.670801, 40.818311],
                北京: [116.405285, 39.904989],
                台湾: [121.509062, 25.044332],
                吉林: [125.3245, 43.886841],
                四川: [104.065735, 30.659462],
                天津: [117.190182, 39.125596],
                宁夏回族自治区: [106.278179, 38.46637],
                安徽: [117.283042, 31.86119],
                山东: [117.000923, 36.675807],
                山西: [112.549248, 37.857014],
                广东: [113.280637, 23.125178],
                广西壮族自治区: [108.320004, 22.82402],
                新疆维吾尔自治区: [87.617733, 43.792818],
                江苏: [118.767413, 32.041544],
                江西: [115.892151, 28.676493],
                河北: [114.502461, 38.045474],
                河南: [113.665412, 34.757975],
                浙江: [120.153576, 30.287459],
                海南: [110.33119, 20.031971],
                湖北: [114.298572, 30.584355],
                湖南: [112.982279, 28.19409],
                甘肃: [103.823557, 36.058039],
                福建: [119.306239, 26.075302],
                西藏自治区: [91.132212, 29.660361],
                贵州: [106.713478, 26.578343],
                辽宁: [123.429096, 41.796767],
                重庆: [106.504962, 29.533155],
                陕西: [108.948024, 34.263161],
                青海: [101.778916, 36.623178],
                香港特别行政区: [114.173355, 22.320048],
                黑龙江: [126.642464, 45.756967],
            };
            var convertData = function (data) {
                var res = [];
                // console.log(data);
                for (var i = 0; i < data.length; i++) {
                    var geoCoord = geoCoordMap[data[i].name];
                    if (geoCoord) {
                        res.push({
                            name: data[i].name,
                            value: geoCoord.concat(data[i].value),
                        });
                    }
                }
                // console.log(res);
                return res;
            };
            var option = {
                scale: 0.1,
                backgroundColor: "transparent",
                title: {
                    text: "全国省市商品数据",
                    subtext: "数据来自淘宝",
                    left: "center",
                    textStyle: {
                        color: "#fff"
                    }
                },
                //光圈效果
                geo: {
                    show: true,
                    map: "china",
                    zoom: 1.25,
                    label: {
                        normal: {
                            show: true,
                            color: "white",
                            fontSize: "8"
                        },
                        emphasis: {
                            show: true,
                            textStyle: {
                                color: "white",
                                fontSize: "10px",
                            }
                        }
                    },
                    roam: true,
                    itemStyle: {
                        normal: {
                            areaColor: "skyblue",
                            borderColor: "#fff",
                        },
                        emphasis: {
                            areaColor: "#2B91B7",
                        },
                    },
                },
                series: [
                    {
                        name: "销量",
                        type: "effectScatter",
                        coordinateSystem: "geo",
                        data: convertData(data),
                        symbolSize: function (val) {
                            return val[2] / 10;
                        },
                        //光圈样式
                        showEffectOn: "render",
                        rippleEffect: {
                            brushType: "stroke",
                        },
                        hoverAnimation: true,

                        label: {
                            formatter: "{b}",
                            position: "right",
                            show: true,
                        },
                        //圆点样式
                        itemStyle: {
                            color: "#FF8C00",
                        },
                        emphasis: {
                            label: {
                                show: true,
                            },
                        },
                    },
                ],
            };
            option && myChart.setOption(option);
        },
        drawRightTop() {
            var myChart = this.$echarts.init(this.$refs.fourthMain)
            var option = {
                xAxis: {
                    type: 'category',
                    data: this.realData.lineRowData,
                    axisLabel: {
                        interval: 0,
                        textStyle: {
                            color: "#C0C0C0"
                        }
                    },
                    name: "元",
                },
                yAxis: {
                    type: 'value',
                    name: "种",
                    axisLabel: {
                        interval: 0,
                        textStyle: { color: "#C0C0C0" }
                    }
                },
                title: {
                    text: "商品价格占比",
                    subtext: "",
                    left: "center",
                    textStyle: {
                        color: "#C0C0C0"
                    }
                },
                tooltip: {
                    trigger: "item"
                },
                legend: {
                    data: ["占比情况"],
                    textStyle: {
                        color: "#C0C0C0"
                    },
                    top: "8%",
                    right: "10%"
                },
                series: [
                    {
                        name: "占比情况",
                        data: this.realData.lineColData,
                        type: 'line'
                    }
                ]
            };
            option && myChart.setOption(option);
        },
        drawRightBottom() {
            var myChart = this.$echarts.init(this.$refs.fifthMain)
            var option = {
                title: {
                    text: "畅销商品类前10名",
                    subtext: "",
                    left: "center",
                    textStyle: {
                        color: "#C0C0C0"
                    }
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    bottom: '1%',
                    left: 'center',
                    textStyle: {
                        color: "#C0C0C0"
                    }
                },
                series: [
                    {
                        name: '畅销商品前10名',
                        type: 'pie',
                        textStyle: {
                            color: "#C0C0C0"
                        },
                        radius: ['30%', '60%'],
                        avoidLabelOverlap: true,
                        padAngle: 5,
                        itemStyle: {
                            borderRadius: 10
                        },
                        label: {
                            show: false,
                            position: 'center',
                            textStyle: { color: "#C0C0C0" }
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: 40,
                                fontWeight: 'bold'
                            }
                        },
                        data: this.realData.rosePieData
                    }
                ]
            };
            option && myChart.setOption(option)
        },
        changeData(x) {
            var st = x[0]
            for (var i = 0; i < x.length - 1; i++) {
                x[i] = x[i + 1]
            }
            x[x.length - 1] = st
        },
        updateBarChart() {
            if (this.isHovered == true) {
                this.changeData(this.realData.cityList)
                this.changeData(this.realData.volumnList)
                var myChart = this.$echarts.init(this.$refs.firstMain)
                // console.log(this.realData.cityList)
                myChart.setOption({
                    xAxis: {
                        data: this.realData.cityList
                    },
                    series: [
                        {
                            data: this.realData.volumnList
                        }
                    ]
                })
            } else {
                clearInterval(this.timer)
            }
        },
        startDataUpdataInterval() {
            const interval = 2000
            clearInterval(this.timer)
            setInterval(this.updateBarChart, interval)
        },
        startAction() {
            this.isHovered = false
        },
        cancelAction() {
            this.isHovered = true
        }
    },
    async mounted() {
        const res = await this.$http.get("myApp/screenData")
        this.$set(this.realData, 'cityList', res.data.cityList)
        this.$set(this.realData, 'volumnList', res.data.volumnList)
        this.$set(this.realData, 'pieList', res.data.pieList)
        this.$set(this.realData, 'mapData', res.data.mapData)
        this.$set(this.realData, 'lineRowData', res.data.lineRowData)
        this.$set(this.realData, 'lineColData', res.data.lineColData)
        this.$set(this.realData, 'rosePieData', res.data.rosePieData)
        // console.log(this.realData.rosePieData)
    },
    async updated() {
        this.drawLeftTop()
        this.drawLeftBottom()
        this.drawCenterMap()
        this.drawRightTop()
        this.drawRightBottom()
        this.startDataUpdataInterval()
    }
}
</script>

<style scoped>
.layout {
    height: 100vh;
    width: 100%;
    background: url('../assets/imgs/01.png');
}

.header {
    display: flex;
    align-items: center;
    justify-content: center;
}

.header div {
    width: 50%;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

.header div span {
    color: steelblue;
    font-weight: bold;
    font-size: 28px;
    padding: 10px;
}

.content {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
}

.content .left {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    height: 80%;
    width: 420px;
}

.content.left div {
    flex-grow: 1;
    height: 300px;
    width: 420px;
    padding: 5px;
}

.content .right {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    height: 80%;
    width: 420px;
}

.content.right div {
    flex-grow: 1;
    height: 300px;
    width: 420px;
    padding: 5px;
}

.content .center {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    height: 80%;
    width: 680px;
}
</style>