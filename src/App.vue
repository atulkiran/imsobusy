<template>
  <div id="app">
    <div>
  
    <b-card-header header-tag="nav" id="navbar">
      <b-nav card-header tabs>
        <b-nav-item to="/summary" exact exact-active-class="active">Summary</b-nav-item>
        <b-nav-item to="/todos" exact exact-active-class="active">Todos</b-nav-item>
      </b-nav>
    </b-card-header>

    

    </div>




    <router-view> </router-view>
  </div>
</template>




<script>
import Vue from 'vue'
import VueRouter from 'vue-router'
import {BootstrapVue} from 'bootstrap-vue'
import { NavPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import axios from 'axios'
import summary from './summary.vue'
import todos from './todos.vue'
import login from './login.vue'
Vue.use(VueRouter)
Vue.use(BootstrapVue)
Vue.use(NavPlugin)


const routes = [
  {path: '/', component: login},
  {path: '/todos', component: todos},
  {path: '/summary' , component: summary},
]

const router = new VueRouter({
  routes // short for `routes: routes`
})

export default {
    name: 'App',
    router,
}
</script>




<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
#navbar {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #688B62;
  margin-top: 10px;
  display: block;
}

p {
    margin-bottom: 16px;
}

header {
   display: flex;
   align-items: center;
   padding: 20px 4%;
   margin-bottom: 20px;
}

header h1, header p {
   width: 100%;
}

header p {
   text-align: center;
   color: #353B86;
}

.tabs {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #688B62;
  margin-top: 10px;
  display: block;
}


</style>
