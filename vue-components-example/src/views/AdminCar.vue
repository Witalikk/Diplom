<template>
  <div class="min-h-screen flex items-center justify-center bg-green-200 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <img class="mx-auto h-16 w-auto" src="http://pngimg.com/uploads/car_logo/car_logo_PNG1640.png" alt="Workflow" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Добавление машин
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          Или
          <a href="/avtomobili_v_nalichii" class="font-medium text-green-800 hover:text-green-500">
            посмотреть список всех машин
          </a>
        </p>
      </div>

        <div class="rounded-md shadow-sm -space-y-px">
          <form>
          <div>
            <label for="model" class="sr-only">Модель</label>
            <small
                class="text-red-800 font-bold"
                v-if="$v.model.$dirty && !$v.model.required"
            >Поле модели не должно быть пустым</small>
            <input v-model="model"
                   :class="{invalid: ($v.model.$dirty && !$v.model.required)}"
                    type="text" id="model" name="model" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Модель" />
          </div>
          <div>
            <label for="year_of_issue" class="sr-only">Год выпуска</label>
            <small
                class="text-red-800 font-bold"
                v-if="$v.year_of_issue.$dirty && !$v.year_of_issue.required"
            >Поле года выпуска не должно быть пустым</small>
            <input v-model="year_of_issue"
                   :class="{invalid: ($v.year_of_issue.$dirty && !$v.year_of_issue.required)}"
                   type="number" placeholder="Год выпуска" id="year_of_issue" name="year_of_issue" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
          </div>
          <div>
            <label for="body_type" class="sr-only">Тип кузова</label>
            <small
                class="text-red-800 font-bold"
                v-if="$v.body_type.$dirty && !$v.body_type.required"
            >Поле типа кузова не должно быть пустым</small>
            <input v-model="body_type"
                   :class="{invalid: ($v.body_type.$dirty && !$v.body_type.required)}"
                   type="text" id="body_type" name="body_type"  placeholder="Тип кузова"  class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
          </div>
          <div>
            <label for="power" class="sr-only">Мощность</label>
            <small
                class="text-red-800 font-bold"
                v-if="$v.body_type.$dirty && !$v.body_type.required"
            >Поле мощности не должно быть пустым</small>
            <input v-model="power"
                   :class="{invalid: ($v.body_type.$dirty && !$v.body_type.required)}"
                   type="number" id="power" name="power" placeholder="Мощность" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
          </div>
          <div>
            <label for="engine_volume" class="sr-only">Объем двигателя</label>
            <small
                class="text-red-800 font-bold"
                v-if="$v.engine_volume.$dirty && !$v.engine_volume.required"
            >Поле объема двигателя не должно быть пустым</small>
            <input v-model="engine_volume"
                   :class="{invalid: ($v.engine_volume.$dirty && !$v.engine_volume.required)}"
                   type="number" id="engine_volume" name="engine_volume" placeholder="Объем двигателя" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
          </div>
          <div >
            <label for="number_of_gears" class="sr-only">Количество передач</label>
            <small
                class="text-red-800 font-bold"
                v-if="$v.number_of_gears.$dirty && !$v.number_of_gears.required"
            >Поле количества передач не должно быть пустым</small>
            <input v-model="number_of_gears"
                   :class="{invalid: ($v.number_of_gears.$dirty && !$v.number_of_gears.required)}"
                   type="number" id="number_of_gears" name="number_of_gears" placeholder="Количество передач" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
          </div>
          <div>
            <label for="price" class="sr-only">Цена</label>
            <small
                class="text-red-800 font-bold"
                v-if="$v.price.$dirty && !$v.price.required"
            >Поле цены не должно быть пустым</small>
            <input  v-model="price"
                    :class="{invalid: ($v.price.$dirty && !$v.price.required)}"
                    type="number" id="price" name="price" placeholder="Цена" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"  />
          </div>
          <div class="form-group mb-4">
            <input  type="file" @change="onFileSelected" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm">
            <button @click.prevent="onUpload" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-800 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
              Добавить
            </button>
          </div>
          </form>
        </div>
    </div>
  </div>
</template>

<script>
import $ from "jquery";
import axios from "axios"
import { required, minLength, sameAs} from 'vuelidate/lib/validators'
import Swal from "sweetalert2";

export default {
  name: "AdminCar",
  data() {
    return {
      marka: 1,
      model: '',
      year_of_issue: null,
      body_type: '',
      power: null,
      price: null,
      engine_volume: null,
      number_of_gears: null,
      logo: null
    }
  },
  validations: {
    model:{required},
    year_of_issue:{required},
    body_type:{required},
    power:{required},
    engine_volume:{required},
    number_of_gears:{required},
    price:{required}
  },
  methods: {
    onFileSelected(event){
      this.logo = event.target.files[0]
    },
    onUpload(){
      if(this.$v.$invalid){
        this.$v.$touch()
        return
      }
      const fd = new FormData();
      fd.append('logo',this.logo, this.logo.name )
      fd.append('body_type',this.body_type )
      fd.append('marka',this.marka)
      fd.append('model',this.model)
      fd.append('price',this.price)
      fd.append('year_of_issue',this.year_of_issue)
      fd.append('power',this.power)
      fd.append('engine_volume',this.engine_volume)
      fd.append('number_of_gears',this.number_of_gears)
      axios.post('http://127.0.0.1:8000/api/models/new/',fd)
      .then(res => {
        console.log(res)
        Swal.fire({
          type: 'success',
          title: 'Добавление автомобиля',
          text:'Новый автомобиль добавлен в автосалон',
          showConfirmButton: false,
          timer:2000
        })
      })
    }
  }
}
</script>

<style scoped>

</style>















