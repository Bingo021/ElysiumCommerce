<template>
    <div>
        <Card style="width:98%;margin:0 auto">
            <template #title>
                <Icon type="md-search"></Icon>
                条件选择
            </template>
            <Form>
                <Row justify="space-around" class="code-row-bg">
                    <Col span="4">
                    <FormItem>
                        地址
                        <Select>
                            <option value="不限"></option>
                        </Select>
                    </FormItem>
                    </Col>
                    <Col span="4">
                    <FormItem>
                        产品类型
                        <Select>
                            <option value="不限"></option>
                        </Select>
                    </FormItem>
                    </Col>
                    <Col span="4">
                    <FormItem>
                        </br>
                        <Button type="primary" shape="circle" icon="ios-search">Search</Button>
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
            <List border style="height: 500px;">
                <ListItem>
                    <Row style="width: 100%;text-align: left;">
                        <Col span="2">商品录入ID</Col>
                        <Col span="2">类型</Col>
                        <Col span="5">名称</Col>
                        <Col span="2">价格</Col>
                        <Col span="2">销量</Col>
                        <Col span="6">图片</Col>
                        <Col span="2">地址</Col>
                        <Col span="">包邮情况</Col>
                    </Row>
                </ListItem>
            </List>
        </Card>
    </div>
</template>

<script>
import { Card, FormItem } from 'view-design';

export default {

}
</script>

<style scoped></style>
