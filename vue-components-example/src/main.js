import Vue from 'vue'
import VueFuse from 'vue-fuse'
import VModal from 'vue-js-modal'
import ToggleButton from 'vue-js-toggle-button'

import App from './App.vue'
import router from './router'
// import i18n from './i18n'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuelidate from "vuelidate/src";
import VueSimpleAlert from "vue-simple-alert";

Vue.use(VueSimpleAlert);
Vue.use(ElementUI)
Vue.use(ToggleButton)
Vue.use(VueFuse)
Vue.use(VModal)
Vue.use(VueAxios, axios)
Vue.use(Vuelidate)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
  axios
}).$mount('#app')
