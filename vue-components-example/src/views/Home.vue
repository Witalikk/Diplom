<template>
  <div class>
    <div class="container mx-auto mt-4 ">

      <swiper :swiperList="swiperList"/>

      <div class="flex flex-row">

  <div class="mr-2">
    <p class="mb-4 text-2xl font-bold">Сервис AUDI</p>
    <div class="image-container serv text-white">
    <img src="@/assets/media/servis.jpg" alt="logo" class="">
    </div>
    <router-link :to="`/service`" class="font-bold text-xl flex items-end">
    <button class=" mt-2 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
      Подробнее
    </button>
    </router-link>
  </div>
        <div class="mr-2" >
          <p class="mb-4 text-2xl font-bold">Новые машины в наличии</p>
            <div class="image-container fade text-white">
          <img src="@/assets/media/audi-sq8-.jpg" alt="logo" >
            </div>
          <router-link :to="`/avtomobili_v_nalichii`" class="font-bold text-xl flex items-end">
          <button class=" mt-2 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
            Посмотреть
          </button>
          </router-link>
        </div>
</div>


        <p class="mb-4 mt-12 text-2xl font-bold">Специальные предложения сервиса</p>
      <div class="pb-16 flex flex-row">
        <a
            href="/service"
            class="flex group"
        >
        <div class="mr-2">
          <img src="@/assets/media/service-car1.jpg" alt="logo" class="w-200">
          <p class="mb-4 mt-4 text-1xl ">Шиномонтаж с выгодой в 50%
            Приобретайте резину и совершайте шиномонтаж с выгодой в 50% в официальный сервисных центрах Audi!
         </p>
        </div>
        <div class="mr-2">
          <img src="@/assets/media/service-car2.jpg" alt="logo" class="w-200">
          <p class="mb-4 mt-4 text-1xl ">Шиномонтаж + диагностика подвески с преимуществом 99%</p>
        </div>
        <div class="mr-2">
          <img src="@/assets/media/service-car3.jpg" alt="logo" class="w-200">
          <p class="mb-4 mt-4 text-1xl ">Услуги по дезинфекции автомобиля с выгодой 30%</p>
        </div>
        </a>
      </div>
      <div class="flex flex-row">
        <div class="mr-2">
          <router-link :to="`/quiz`" class="font-bold text-xl flex items-end">
          <button class=" mt-1 mb-4 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
            Проверь себя на знание марки Audi
          </button>
          </router-link>
          <video width="100%" height="10%" preload="auto" autoplay="true" loop="true" muted="muted"  src="@/assets/media/video//Quiz.mp4"  ></video>

        </div>

<!--        <div>-->
<!--          <div class="mb-4 text-2xl font-bold">Новое поколение Audi A5 уже в Audi Центр</div>-->
<!--          <img src="@/assets/media/service-car4.jpg" alt="logo" class="w-200">-->
<!--          <button class=" mt-1 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">-->
<!--            Подробнее-->
<!--          </button>-->
<!--        </div>-->
      </div>
      <div class="mr-2 mt-40">
        <router-link  :to="`/rooms`" class="font-bold text-xl flex items-end">
          <div >
          <button   class=" mt-1 mb-4 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
            Обсудите актуальные темы марки Audi
          </button>
          </div>
        </router-link>
<!--        <div v-if="user_id == null" class="form-group mb-4">-->
<!--          <button type="submit" class=" bg-red-200 text-gray-900 font-bold py-2 px-4 rounded shadow opacity-70  cursor-not-allowed">Здесь вы можете обсудить важные темы касающиеся марки Audi, но вы не авторизованы.</button>-->
<!--        </div>-->
        <img width="100%" height="10%"  src="https://incrussia.ru/wp-content/uploads/2019/03/iStock-531632740.jpg"  ></img>

      </div>
      <div class="pb-16">
        <div class="mb-4 text-2xl font-bold">This is a title</div>
        <p>Lorem ipsum dolor sit amet <a href="#" class="text-blue-600 hover:text-blue-800">consectetur</a> adipisicing elit. Aut dicta incidunt ea ut commodi quidem temporibus illo quia. Et itaque deleniti veniam tempore facere ipsum animi totam culpa minima vel voluptatem adipisci natus blanditiis similique sunt expedita, ex dicta doloremque repellat vitae temporibus. Quisquam quia, accusantium blanditiis architecto facilis saepe! Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad unde laborum ut suscipit iure aliquam sapiente doloribus exercitationem nam sint.</p>
      </div>
    </div>

  </div>
</template>

<script>
// import SelectablePlan from '@/components/SelectablePlan.vue'
import { swiperList } from '@/assets/data/swiper.js'
import Swiper from '@/components/Swiper.vue'
import $ from "jquery";



export default {
  components: {
    // SelectablePlan,
    // PricingTable,
    Swiper,

  },
  data() {
    return {
      activePlan: '',
      swiperList:[],
      user_id: null,

    }
  },
  created(){
    this.loadUser();
  },
  methods: {
    loadUser() {
      console.log("user")
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/me/",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.user_id = response.data.id

        }
      })
    }
  },
  created(){
    this.swiperList = swiperList
  }
}
</script>
<style scoped>
.image-container{
  position:relative;
}

.fade::after{
  content:"Самое лучшее для вас";
  background:black;
  display:flex;
  justify-content:center;
  align-items:center;
  width:100%;
  font-size:20px;
  height:100%;
  top:0;
  left:0;
  position:absolute;
  opacity:0;
  transition: opacity 0.5s ease;
}
.fade:hover::after{
  opacity:0.7;
}

.serv::after{
  content:"Мы заботимся о клиентах";
  background:black;
  display:flex;
  justify-content:center;
  align-items:center;
  width:100%;
  font-size:20px;
  height:100%;
  top:0;
  left:0;
  position:absolute;
  opacity:0;
  transition: opacity 0.5s ease;
}
.serv:hover::after{
  opacity:0.7;
}

</style>
