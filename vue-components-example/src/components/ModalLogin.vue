<template>
  <div class="normal-case tracking-normal">
    <a href="/#login" @click.prevent="show" class="text-copy-primary uppercase hover:text-gray-600">Вход</a>
    <modal name="modal-login" :adaptive="true" :height="440" :width="400" class="bg-green-200">
      <div class="px-10 py-8">
        <h2 class="mb-4 uppercase tracking-wide text-xl">Вход</h2>
        <form @submit.prevent="login">
          <div class="form-group mb-4">
            <label for="username" class="block font-normal uppercase tracking-wide text-xs mb-1">Логин</label>
            <input v-model="username"
                   id="username"
                   type="text"
                   class="border px-4 py-2 w-full rounded bg-gray-200"
                   :class="{invalid: ($v.username.$dirty && !$v.username.required)}">
            <small
              class="text-red-800"
              v-if="$v.username.$dirty && !$v.username.required"
              >Введите логин</small>
          </div>
          <div class="form-group mb-4">
            <label for="password" class="block font-normal uppercase tracking-wide text-xs mb-1">Пароль</label>
            <input v-model="password"
                   type="password"
                   class="border px-4 py-2 w-full rounded bg-gray-200"
                   :class="{invalid: ($v.password.$dirty && !$v.password.required) || ($v.password.$dirty && !$v.password.minLength)}">
            <small
                class="text-red-800"
                v-if="$v.password.$dirty && !$v.password.required"
            >Введите пароль</small>
          </div>
          <div class="form-group mb-8">
            <label class="text-sm font-normal"><input type="checkbox" name="remember" class="mr-2">Запомнить меня</label>
          </div>
          <div class="form-group mb-4">
            <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-800 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Войти</button>
          </div>
        </form>

        <div class="text-sm font-normal text-center">
          <p><a href="/login/vk-oauth2" class="text-blue-600 hover:text-blue-800" @keydown.tab.exact.prevent="">VK</a></p>
        </div>
        <div class="text-sm font-normal text-center">
<!--          <el-button :plain="true" @click="login_succes">success</el-button>-->
          <p>Нету учетной записи? <a href="#" class="text-blue-600 hover:text-blue-800" @click.prevent="showRegister" @keydown.tab.exact.prevent="">Зарегистрироваться</a></p>
        </div>
      </div>
    </modal>
  </div>
</template>

<script>
  import $ from 'jquery'
  import Swal from 'sweetalert2'
  import { required, minLength} from 'vuelidate/lib/validators'

export default {
  data() {
 return {
 username: '',
 password: ''
 };
 },
  validations:{
    username:{required},
    password:{required}
  },
  methods: {
    show() {
      this.$modal.show('modal-login')
    },
    login: function (event) {
      if(this.$v.$invalid){
        this.$v.$touch()
        return
      }
      event.preventDefault();
      //console.log(this.username, this.password);
      $.ajax({
        url: "http://127.0.0.1:8000/auth/token/login/",
        type: "POST",
        data: {
          username: this.username,
          password: this.password
        },
        success: (response) => {
         // console.log(response.data.attributes.auth_token)
          localStorage.setItem('auth_token', response.data.attributes.auth_token);
              // Swal.fire({
              //   position: 'top-end',
              //   icon: 'success',
              //   title: 'Your work has been saved',
              //   showConfirmButton: false,
              //   timer: 1500
              // })
          Swal.fire({
            type: 'success',
            title: 'Вы успешно авторизовались, сейчас вы отправитесь на главную страницу',
            showConfirmButton: false,
          })
          setTimeout(() => {   window.location.href = "/" }, 1000);
        },
        error: (response) => {
          if (response.status === 400) {
            Swal.fire({
              position: 'bottom',
              type: 'error',
              title: 'Логин или пароль введены не верно',
              showConfirmButton: false,
            })
          }
        }
      })
    },
 /***    this.axios
              .post(`http://127.0.0.1:8000/auth/token/login/`, {
                headers: {'Content-type': 'application-json'},
                'username': this.username, 'password': this.password
              })
              .then(response => {
                console.log(response.data.attributes.auth_token);
                this.setLogined(response.data.attributes.auth_token);
                this.$router.push("/contact");
              })
              .catch(err => {
                console.error(err)
              })
    },
    setLogined(token) {
      localStorage.setItem('token', token);
      console.log(token);
    },***/
    showRegister() {
      this.$modal.show('modal-register')
      this.$modal.hide('modal-login')
    },
    hide() {
      this.$modal.hide('modal-login')
    }
  }
}
</script>

