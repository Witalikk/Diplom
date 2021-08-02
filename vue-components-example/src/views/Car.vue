<template>
  <div>
    <div class="flex justify-center p-absolute bg-green-200  ">
      <div v-if="formModel.model.includes('A8')">
        <video width="300%" height="30%" preload="auto" autoplay="true"  src="@/assets/media/video//a8.mp4"  ></video>
      </div>
<!--      <div v-if="formModel.model.includes('A4')">-->
<!--        <img class="relative" src="@/assets/media/A4.jpg" alt="logo">     -->
<!--      </div>-->
      <div v-else>
      <img class="relative" :src="formModel.logo" alt="logo">
      <div class="absolute font-bold text-2xl text-white mt-4">
      <h1 class="">{{formModel.model}}</h1>
      </div>
      </div>
    </div>
<template v-if="username === 'admin'">
    <form @submit.prevent="setAuto" class=" br-20 flex justify-center bg-green-200 ">
      <div class="rounded-md shadow-sm">
        <div>
          <label for="model" class="text-sm">Модель</label>
          <input v-model="formModel.model" type="text" id="model" name="model" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Модель" />
        </div>
        <div>
          <label for="year_of_issue" class="text-sm">Год выпуска</label>
          <input v-model="formModel.year_of_issue" type="number" placeholder="Год выпуска" id="year_of_issue" name="year_of_issue" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
        </div>
        <div>
          <label for="body_type" class="text-sm">Тип кузова</label>
          <input v-model="formModel.body_type" type="text" id="body_type" name="body_type"  placeholder="Тип кузова"  class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
        </div>
        <div>
          <label for="power" class="text-sm">Мощность</label>
          <input v-model="formModel.power" type="number" id="power" name="power" placeholder="Мощность" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
        </div>
        <div>
          <label for="engine_volume" class="text-sm">Объем двигателя</label>
          <input v-model="formModel.engine_volume" type="number" id="engine_volume" name="engine_volume" placeholder="Объем двигателя" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
        </div>
        <div >
          <label for="number_of_gears" class="text-sm">Количество передач</label>
          <input v-model="formModel.number_of_gears" type="number" id="number_of_gears" name="number_of_gears" placeholder="Количество передач" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
        </div>
        <div>
          <label for="price" class="text-sm">Цена</label>
          <input  v-model="formModel.price" type="number" id="price" name="price" placeholder="Цена" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
        </div>
        <div class="form-group mb-4">
          <input  type="file" @change="onFileSelected" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm">
          <button @click="onUpload" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-800 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
            Изменить
          </button>
        </div>
      </div>
    </form>
        <div class="rounded-md flex justify-center bg-green-200 form-group mb-4">
          <div>
            <button @click="deleteCar" type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-800 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Удалить</button>
          </div>
        </div>

</template>
 <div v-else>

   <div class="mt-20 grid grid-flow-col grid-rows-1  ml-48 mb-12 ">
     <div>
       <router-link :to="`/TestdriveForm`" class="font-bold ">
         <img src="@/assets/media/icons/test64.png" alt="logo" >
         <p >Запись на<br> тест-драйв</p>
       </router-link>
     </div>
     <div>
       <router-link :to="{name:'credit', params:{id:id_model}}" class="font-bold ">
         <img src="@/assets/media/icons/credit64.png" alt="logo" >
         <p >Рассчитать<br>кредит</p>
       </router-link>
     </div>
     <div>
       <router-link :to="`/buyform`" class="font-bold">
         <img src="@/assets/media/icons/buy64.png" alt="logo" >
         <p >Запись на<br> покупку</p>
       </router-link>
     </div>
     <div>
       <router-link :to="`/garanty`" class="font-bold">
         <img src="@/assets/media/icons/garanty64.png" alt="logo" >
         <p >5 лет<br> гарантии</p>
       </router-link>
     </div>

   </div>




   <h1 class="mt-16 text-center mb-16 mt-40 text-4xl font-extrabold text-black">
     Он провоцирует на скорость
   </h1>
    <div class="block pb-16 flex justify-evenly  mb-20">
        <div class="mt-10 ">
          <p class="mb-4 text-2xl font-extrabold text-gray-900">Кол-во передач: {{formModel.number_of_gears}}</p>
        </div>
        <div class="mt-10">
          <p class="mb-4 text-2xl font-extrabold text-gray-900">Мощность: {{formModel.power}} л/c</p>
        </div>
        <div class="mt-10">
          <p class="mb-4 text-2xl font-extrabold text-gray-900">Объем двигателя: {{formModel.engine_volume}}</p>
        </div>
    </div>

   <div class="mx-auto py-8 md:flex md:justify-between md:flex-wrap">
     <radar-swiper :swiperListRadar="swiperListRadar"/>
   </div>
   <div class="bg-black">
     <div v-if="formModel.model.includes('A4')">
          <div class="mt-16 sketchfab-embed-wrapper flex justify-center mb-80 bg-black ">
            <iframe class="mt-32"  frameborder="2" loading = "lazy"  webkitallowfullscreen="true" allow="fullscreen; vr" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="1240" height="620" src="https://sketchfab.com/models/e8f318eeaeca43669b9b341fd446698d/embed?autostart=1&autospin=0&preload=1&annotation=1&annotation_cycle=3&ui_hint=0">
            </iframe>
          </div>
       <div class="mb-32 mt-64 bg-black">
         <h1 class="mb-32 mt-16 text-center text-4xl font-extrabold text-white">Лучший разгон среди конкурентов</h1>
         <video preload="auto" autoplay="true" loop="true" muted="muted"  src="@/assets/media/video//100.mp4"  width="100%"   />
       </div>
     </div>
     <div v-if="formModel.model.includes('A8')">
       <div class="mt-16 mb-80 sketchfab-embed-wrapper flex justify-center mb-4 bg-black ">
         <iframe class="mt-32" frameborder="2" loading = "lazy"  webkitallowfullscreen="true" allow="fullscreen; vr" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="1240" height="820" src="https://sketchfab.com/models/f14648e379654ec4835c98bbf677444f/embed?autostart=1&preload=1&ui_theme=dark">
         </iframe>
       </div>
     </div>
     <div v-if="formModel.model.includes('A7')">
       <div class="mb-80 mt-80">
           <h1 class="mt-16 bg-white text-center text-4xl font-extrabold text-black">Новая свобода</h1>
         <h4 class="bg-white text-center text-xl font-extrabold text-black">
           Ощутите пространство на новом уровне: опциональная панорамная крыша на 60% расширяет обзор, а интерьер залит солнечным светом. При необходимости раскрытая солнцезащитная шторка обеспечит 100% защиту от света и низкий нагрев салона.         </h4>
         <video class="relative" preload="auto" autoplay="true" loop="true" muted="muted"  src="@/assets/media/video//A7.mp4"  width="100%" ></video>
         <img  src="@/assets/media/video/a7.jpg" alt="logo" >
       </div>
       <div class="mt-16 mb-80 sketchfab-embed-wrapper flex justify-center mb-4 bg-black ">
         <iframe class="mt-32" title="Audi A7 Sportback 2018" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="fullscreen; autoplay; vr" xr-spatial-tracking execution-while-out-of-viewport width="1240" height="820" execution-while-not-rendered web-share src="https://sketchfab.com/models/95700e5a98904b3591c6a03a4b67787b/embed?autostart=1&preload=1"> </iframe>
         <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"></p>
       </div>
     </div>

     <div class="mb-20" v-if="formModel.model.includes('Q8') || formModel.model.includes('RSQ8')" >
       <div class="mb-80 mt-80">
         <h1 class="mb-10 text-left ml-20 text-4xl font-extrabold text-white">Видеть. Осязать. Управлять</h1>
         <h4 class=" mb-20 ml-20 text-left text-xl font-extrabold text-gray-300">
           Салон Audi RS Q8 оснащен множеством цифровых технологий, которые предоставят вам<br> разнообразную поддержку во время каждой поездки. Специфические для серии RS<br> индикаторы цифровой панели приборов Audi virtual cockpit проинформируют вас<br> о крутящем моменте, мощности, ускорении, времени прохождения кругов и перегрузках.
         </h4>
         <div class="img-container">
         <img class="relative" src="https://www.audi.by/dam/nemo/models/q8/rs-q8/my-2021/_update/1920x1080-mtc-xl-16-9/1920x1080-audi-rs-q8-cockpit-RSQ8_2020_1557.jpg?output-format=webp&downsize=1920px:*"/>
         </div>
         </div>
     </div>



     <div class="flex ">
       <div class="flex-none relative">
         <video preload="auto" autoplay="true" loop="true" muted="muted"  src="https://www.audi.by/dam/nemo/models/a6/a6-limousine/my-2019/730x730-media-text-combi-XL-1-1-framed/video/730x730_Modul7_%20Modul07__MTC_1Framed_XL_%20Ambientlight_AA6_D181009_.mp4" />
       </div>
       <div class="flex flex-wrap">
         <h1 class="mt-16 ml-20 text-left ml-16 text-4xl font-extrabold text-white">
           Приятная <br> атмосфера
         </h1>
         <h4 class=" mb-4 ml-20 text-left mr-8 text-xl font-extrabold text-gray-300">
           Доступная в качестве опции контурная подсветка салона придает внутреннему пространству Audi дополнительную привлекательность и создает уникальную атмосферу благополучия. Тонкие световые линии, обрамляющие панель приборов, центральную консоль и другие элементы салона, могут окрашиваться в 30 разных цветов и имеют бесступенчатую регулировку яркости.
         </h4>
       </div>
     </div>
     <div class="flex justify-left p-absolute mb-32 mt-80">
       <img class="relative" src="https://www.audi.by/dam/nemo/models/q8/rs-q8/my-2021/_update/1920x1920-mtc-xl-1-1/1920x1920-audi-rs-q8-interior-RSQ8_2020_1558.jpg?output-format=webp&downsize=1920px:*"   />
       <div class="absolute mt-16 mb-4 ml-16 mr-80  text-left text-4xl  font-serif  text-black bg-white" >
         <h1 class="ml-20 mr-16 mt-8 font-bold ">
           Продуман до мелочей:<br> интерьер
         </h1>
         <h1 class="ml-20 mr-20 mb-8 mt-4 text-xl ">
           Элегантная приборная панель и четко выраженные горизонтальные линии создают ощущение простора. Широкая, симметрично организованная центральная консоль с отделкой по периметру матовыми карбоновыми вставками с саржевым плетением, является ключевым элементом дизайна. Спортивные сиденья с комбинированной обивкой из материала Alcantara черного цвета и кожи с тиснением RS обеспечивают превосходную боковую поддержку даже во время вождения в динамичном стиле. Опционально доступны спортивные сиденья с обивкой перфорированной кожей Valcona с прострочкой в видео сот. Опциональные дизайн-пакеты RS в серых и красных тонах продуманы до мельчайших деталей. Сочетание материала Alcantara и кожи с контрастной строчкой создает еще более спортивную атмосферу.
         </h1>
       </div>

     </div>


<div class="ml-40 mr-40 mt-40 mb-80">
  <h1 class="font-serif mt-16 mb-8 text-center text-4xl font-extrabold text-white">
    Цифровое освещение
  </h1>
  <h4 class=" mb-12 text-center text-l text-white">
    Доступные по запросу светодиодные фонари HD Matrix LED говорят на<br> новом языке цифрового дизайна.
  </h4>

     <div class="flex-none relative">
       <video   preload="auto" autoplay="true" loop="true" muted="muted"   src="@/assets/media/video/fara.mp4" />
     </div>

<!--     <div class="flex flex-wrap">-->
<!--       <h1 class="mt-16 ml-20 text-left ml-16 text-4xl font-extrabold text-white">-->
<!--         Приятная <br> атмосфера-->
<!--       </h1>-->
<!--     </div>-->
</div>
   </div>



 </div>








 </div>
</template>

<script>
import $ from "jquery";
import axios from "axios";
import SelectablePlan from '@/components/SelectablePlan.vue'
import PricingTable from '@/components/PricingTable.vue'
import { swiperListRadar } from '@/assets/data/swiperRadar.js'
import RadarSwiper from '@/components/RadarSwiper.vue'
export default {
  components: {
    PricingTable,
    RadarSwiper,
  },
  name: "Car",
  data() {
    return {
      username:'',
      id_model: null,
    //  marka: 1,
      formModel:{
        model:'',
        power:'',
        engine_volume:'',
        logo:'',
        number_of_gears:'',
        price:'',
        body_type:'',
        year_of_issue:''
      },
      swiperListRadar:[],


    }
  },
  mounted() {
    this.loadMod()
    this.loadUser()
    this.swiperListRadar = swiperListRadar
  },
  methods: {
    loadMod() {
      $.ajax({
        url: `http://127.0.0.1:8000/api/models/${this.$route.params.id}`,
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.formModel = response.data.attributes;
          this.id_model = response.data.id;
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
          this.username = response.data.attributes.username;
        }
      })
    },
    onFileSelected(event){
      this.formModel.logo = event.target.files[0]
    },
    setAuto(){
      const fd = new FormData();
      fd.append('logo',this.formModel.logo, this.formModel.logo.name )
      fd.append('body_type',this.formModel.body_type )
      //fd.append('marka',this.marka)
      fd.append('model',this.formModel.model)
      fd.append('price',this.formModel.price)
      fd.append('year_of_issue',this.formModel.year_of_issue)
      fd.append('power',this.formModel.power)
      fd.append('engine_volume',this.formModel.engine_volume)
      fd.append('number_of_gears',this.formModel.number_of_gears)
      axios.put('http://127.0.0.1:8000/api/models/' + this.id_model,fd)
          .then(res => {
            console.log(res)
          })
    },
    deleteCar(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/models/destroy/" + this.id_model,
        type: "DELETE",
        success: (response) => {
          console.log("SUCCESS",response)
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Что-то нетак')
          }
        }
      })
    }


  }
}
</script>

<style scoped>
.img-container img{
  transition: all 0.4s ease-out;
}
.img-container img:hover{
  transform: scale(1.3)
}
.img-container {
  overflow: hidden;
}
</style>