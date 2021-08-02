<template>
  <div id="app" class="font-sans text-gray-800">
    <header class="border-t-4 border-green-700 bg-white z-10 absolute w-full shadow-md">
      <nav class="container mx-auto px-8 flex flex-wrap justify-between items-start py-8  ">
        <div class="mb-0 lg:mb-6 xl:mb-0 ">
          <router-link :to="`/`" class="mt-2 font-bold text-xl flex items-end">
<!--            <img src="@/assets/media/audi.jpg" alt="logo" class="w-12 h-12">-->
            <h1>АвтоДом</h1>
          </router-link>
        </div>

        <div class="block lg:hidden">
          <button @click="toggleMenu" class="flex items-center px-3 py-2 border rounded border-gray-500 hover:text-gray-600 hover:border-gray-600">
            <svg class="current-color h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" fill="gray" /></svg>
          </button>
        </div>
        <ul
          class="uppercase tracking-wide font-bold w-full block flex-grow lg:flex lg:flex-initial lg:w-auto items-center mt-8 lg:mt-0 "
          :class="menuOpen ? 'block': 'hidden' ">
          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu/>
          </li>
          <li class="mr-12 mb-6 lg:mb-0">
            <search-component />
          </li>
          <template v-if="user_id == null">
            <li class="mr-8 mb-6 lg:mb-0" >
              <modal-login />
            </li>
            <li class="mr-8 mb-6 lg:mb-0">
              <modal-register />
            </li>
          </template>
          <div v-else>
          <li class="mr-8 mb-6 lg:mb-0" >
            <h1>{{username}}</h1>
          </li>
          </div>
          <li>
            <dropdown-menu />
          </li>
        </ul>
      </nav>
    </header>


    <div class="bg-gray-100 min-h-screen pt-32 text-lg">
      <router-view/>
    </div>
      <Footer />
  </div>

</template>

<script>
import DropdownMenu from '@/components/DropdownMenu.vue'
import MegaMenu from '@/components/MegaMenu.vue'
import ModalLogin from '@/components/ModalLogin.vue'
import ModalRegister from '@/components/ModalRegister.vue'

// import LanguageSwitcher from '@/components/LanguageSwitcher.vue'
import SearchComponent from '@/components/SearchComponent.vue'
import Footer from '@/components/Footer.vue'
import $ from "jquery";


export default {
  name: 'app',
  data(){
    return{
      user_id: null,
      models:[],
      menuOpen: false,
      username:'',
    }
  },
  created() {
    this.loadModel()

    if(localStorage.getItem("token")) {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + localStorage.getItem("token")},
      });
    }
  },
  mounted(){
    this.loadUser()
  },

  components: {
    DropdownMenu,
    MegaMenu,
    Footer,
    ModalLogin,
    ModalRegister,
    // LanguageSwitcher,
    SearchComponent,

  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen
    },
    loadModel() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/models/",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.models = response.data;
          console.log(response +"WALERA")
        }
      })
    },
    loadUser() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/me/",
        contentType: 'application/vnd.api+json',
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')},
        type: "GET",
        success: (response) => {
          this.user_id = response.data.id;
          this.username= response.data.attributes.username;

        }
      })
    }
  }
}
</script>

<style src="@/assets/css/tailwind.css" />


