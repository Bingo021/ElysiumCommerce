import Vue from 'vue'
import ViewUI from 'view-design'
import App from './App'
import store from './store'
import router from './router'
import 'view-design/dist/styles/iview.css'
import './permission'
import dataV from '@jiaminghi/data-view'
import * as echarts from 'echarts';
import $http from '@/api/index.js'

Vue.use(dataV)
Vue.config.productionTip = false
Vue.use(ViewUI)
Vue.prototype.$echarts = echarts
// Vue.prototype.$axios = axios
Vue.prototype.$http = $http

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App),
})