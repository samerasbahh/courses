import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import moment from 'moment'


Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(BootstrapVue)
Vue.use(moment);
Vue.config.devtools = true
Vue.component('Datatable', require('./components/Datatable.vue').default);

new Vue({
  el: '#app',
  render: h => h(App)
})

