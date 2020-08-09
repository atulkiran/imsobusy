import Vue from 'vue'
import App from './App.vue'

require('dotenv').config()

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
