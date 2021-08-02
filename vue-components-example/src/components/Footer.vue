<template>
  <footer class="text-gray-100 bg-black">
    <div class="max-w-4xl mx-auto py-6">
<!--      <h1 class="text-center text-lg lg:text-2xl">-->
<!--        Join 31,000+ other and never miss <br> out on new tips, tutorials, and more.-->
<!--      </h1>-->

      <div class="flex mt-6">
        <div class="flex flex-row">
          <div class=" justify-between md:flex-row">
            <router-link :to="`/contact`" class="font-bold text-xm flex items-end">
            <button class="hover:text-gray-500  w-full m- p-2 text-xm  uppercase lg:w-auto">
              <img src="@/assets/media/icons/contacts.png" alt="logo" >
              Контакты
            </button>
            </router-link>
          </div>
          <div class="">
            <router-link :to="`/TestdriveForm`" class="font-bold text-xm flex items-end">
              <button class="hover:text-gray-500  w-full m- p-2  text-xm  uppercase lg:w-auto">
                <img src="@/assets/media/icons/prokat.png" alt="logo" >
                Запись на тест-драйв</button>
            </router-link>
          </div>
          <div>
            <router-link :to="`/buyform`" class="font-bold text-xl flex items-end">
              <button class="hover:text-gray-500  w-full m- p-2 text-sm uppercase lg:w-auto"><img src="@/assets/media/icons/nal.png" alt="logo" >Запись на покупку</button>
            </router-link>
          </div>
          <div>
            <router-link :to="`/ServiceForm`" class="font-bold text-xl flex items-end">
              <button class="hover:text-gray-500  w-full m- p-2 text-sm uppercase lg:w-auto">  <img src="@/assets/media/icons/car-service.png" alt="logo" >Официальный сервис</button>
            </router-link>
          </div>
          <div>
            <router-link :to="`/3dTour`" class="font-bold text-xl flex items-end">
              <button class="hover:text-gray-500  w-full m- p-2 text-sm uppercase lg:w-auto">  <img src="@/assets/media/icons/3d.png" alt="logo" >3D тур</button>
            </router-link>
          </div>
        </div>
      </div>

      <hr class="h-px mt-6 bg-gray-700 border-none">

      <div class="flex flex-col items-center justify-between mt-6 md:flex-row">
        <div>
          <p href="#" class="text-xl font-bold text-gray-100">© 2021 AUDI AG. Все права защищены</p>
        </div>

        <div class="flex mt-4 md:m-0">
          <div class="-mx-4">
            <a href="" class="px-4 text-sm text-gray-100 font-medium hover:text-gray-400">О нас</a>
            <a href="#" class="px-4 text-sm text-gray-100 font-medium hover:text-gray-400">Блог</a>
            <router-link :to="`/contact`">
            <a href="#" class="px-4 text-sm text-gray-100 font-medium hover:text-gray-400">Контакты</a href="#">
            </router-link>

          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  name: "Footer"
}
</script>
