import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './app/router'
import i18n from './app/locales/i18n'


import '@fortawesome/fontawesome-free/css/all.css'
import { create, NButton, NLayout, NLayoutHeader, NLayoutContent,
  NLayoutFooter, NDropdown, NCard, NSpace, NTag, NList, NListItem,
  NCarousel, NModal, NImage } from 'naive-ui'

const naive = create({
  components: [NButton, NLayout, NLayoutHeader, NLayoutContent,
    NLayoutFooter, NDropdown, NCard, NSpace, NTag, NList, NListItem,
    NCarousel, NModal, NImage]
})

createApp(App)
  .use(naive)
  .use(router)
  .use(i18n)
  .mount('#app')
