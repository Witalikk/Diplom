<template>
  <div class="container flex flex-row">
    <div class="px-20 py-8 mt-5">
      <h2 class="mb-4 uppercase tracking-wide text-xl">Запись на тест-драйв</h2>
      <form @submit="testdrive">
        <div class="form-group mb-4">
        <select v-model="model"   class="border px-4 py-2 w-full rounded bg-gray-200">
          <option disabled selected>Выбрать авто</option>
          <option v-for="currency in auto" :value="currency.id" :key="currency.id">{{currency.attributes.marka.marka}} {{currency.attributes.model}}</option>
        </select>
        </div>
        <div class="form-group mb-4">
        <input v-model="date" min="2021-06-14" type="date" class="border px-4 py-2 w-full rounded bg-gray-200"/>
        </div>
        <div v-if="user_id != null" class="form-group mb-4">
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Отправить</button>
        </div>
        <div v-if="user_id == null" class="form-group mb-4">
          <button type="submit" class=" bg-blue-500 text-white font-bold py-2 px-4 rounded opacity-50 cursor-not-allowed">Вы не авторизованы</button>
        </div>
      </form>
    </div>
    <div class=" ml-10">
<!--      <img src="@/assets/media/test.jpg" alt="logo" class="w-200">-->
      <video width="300%" height="30%" preload="auto" autoplay="true" loop="true" muted="muted"  src="@/assets/media/video//buy.mp4"  ></video>

    </div>
  </div>
</template>

<script>
import $ from "jquery";
import Swal from "sweetalert2";
export default {
  name: "TestdriveForm",
  data() {
    return {
      auto: '',
      date: '',
      user: '',
      model:'',
      user_id: null,
    }
  },
  created() {
    $.ajaxSetup({
      headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
    });
    this.loadModel();
    this.loadUser();

  },
  methods: {
    loadModel() {
      console.log("modeli")
      $.ajax({
        url: "http://127.0.0.1:8000/api/models/",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.auto = response.data;
          console.log(this.auto)
        }
      })
    },


    loadUser() {
      console.log("user")
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/me/",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.user = response.data;
          this.user_id = response.data.id;
          console.log(response.data);
          console.log(this.user.id)
        }
      })
    },
    testdrive: function (event) {
      event.preventDefault();
      console.log(this.auto, this.date);
      $.ajax({
        url: "http://127.0.0.1:8000/api/inquiry/new/",
        type: "POST",
        data: {
          user: this.user.id,
          model: this.model,
          date_inquiry: this.date
        },
        success: (response) => {
          Swal.fire({
            type: 'success',
            title: 'Спасибо что выбрали нас. Мы ответим вам на почту',
            showConfirmButton: false,
            timer:2000
          })
        },
        error: (response) => {
          if (response.status === 400) {
            Swal.fire({
              type: 'error',
              title: 'Вам нужно выбрать автомобиль и дату.',
              showConfirmButton: false,
              timer:2000
            })
          }
        }
      })
    }
  }
}
</script>

<style scoped>
</style>