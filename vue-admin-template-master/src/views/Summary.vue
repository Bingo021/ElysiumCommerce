<template>
    <div>
        <Card style="width:98%;margin:0px auto">
            <template #title>
                <Icon type="md-search"></Icon>
                条件选择
            </template>
            <Form>
                <Row justify="space-around" class="code-row-bg">
                    <Col span="4">
                    <FormItem>
                        地址
                        <Select name="city" v-model="realData.selectCity">
                            <Option value="不限"></Option>
                            <Option v-for="city in realData.goodsCity" v-bind:key="city" :value="city">{{ city }}
                            </Option>
                        </Select>
                    </FormItem>
                    </Col>
                    <Col span="4">
                    <FormItem>
                        产品类型
                        <Select name="type" v-model="realData.selectType">
                            <Option value="不限"></Option>
                            <Option v-for="type in realData.goodsType" v-bind:key="type" :value="type">{{ type }}
                            </Option>
                        </Select>
                    </FormItem>
                    </Col>
                    <Col span="4">
                    <FormItem>
                        </br>
                        <Button type="primary" shape="circle" icon="ios-search" v-on:click="query">Search</Button>
                    </FormItem>
                    </Col>
                    <Col span="4">
                    </Col>
                </Row>
            </Form>
        </Card>
        <Card style="width: 98%;margin: 5px auto;">

            <template #title>
                <Icon type="md-paper"></Icon>
                商品数据
            </template>
            <List border style="height: 480px;overflow:auto">
                <div style="position: sticky; top: 0; background-color: white; z-index: 1;">
                    <ListItem>
                        <Row style="width: 100%; text-align: center;">
                            <Col span="2">商品录入ID</Col>
                            <Col span="1">类型</Col>
                            <Col span="5">名称</Col>
                            <Col span="1">价格</Col>
                            <Col span="1">销量</Col>
                            <Col span="4">图片</Col>
                            <Col span="3">店铺</Col>
                            <Col span="2">地址</Col>
                            <Col span="">包邮情况</Col>
                        </Row>
                    </ListItem>
                </div>
                <ListItem v-for="good in realData.goodsData" v-bind:key="good.id">
                    <Row style="width: 100%;text-align: center;">
                        <Col span="2">{{ good.id }}</Col>
                        <Col span="1">{{ good.type }}</Col>
                        <Col span="5"><a :href="good.href" style="color:grey">{{ good.title }}</a></Col>
                        <Col span="1">{{ good.price }}</Col>
                        <Col span="1">{{ good.buy_len }}</Col>
                        <Col span="4"><a :href="good.href"><img :src="good.img_src" alt="" style="height:80px"></a></Col>
                        <Col span="3"><a :href="good.nameHref" style="color:grey">{{ good.name }}</a></Col>
                        <Col span="2">{{ good.address }}</Col>
                        <Col span="">{{ good.isFreeDelivery }}</Col>
                    </Row>
                </ListItem>
            </List>
        </Card>
    </div>
</template>

<script>
    // import { Card, FormItem } from 'view-design';
    export default {
        data() {
            return {
                realData: {
                    goodsCity: "",
                    goodsType: "",
                    selectCity: "",
                    selectType: "",
                    goodsData: ""
                }
            }
        },
        methods: {
            async query() {
                var city = this.realData.selectCity
                var type = this.realData.selectType
                var res = await this.$http.get('myApp/summary', { params: { city: city, type: type } })
                this.$set(this.realData, "goodsData", res.data.goodsData)
            }
        },
        async mounted() {
            const res = await this.$http.get('myApp/summary')
            this.$set(this.realData, "goodsCity", res.data.goodsCity)
            this.$set(this.realData, "goodsType", res.data.goodsType)
        },
    }
</script>

<style scoped></style>