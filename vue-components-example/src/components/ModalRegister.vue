<template>
  <div class="normal-case tracking-normal">
    <a href="/#register" @click.prevent="show" class="text-copy-primary uppercase hover:text-gray-600">Регистрация</a>
    <modal name="modal-register" @opened="opened" :adaptive="true" :height="800" :width="400" class="bg-green-200">
      <div class="px-10 py-8">
        <h2 class="mb-4 uppercase tracking-wide text-xl">Форма регистрации</h2>
        <form @submit.prevent="register">
          <div class="form-group required mb-4">
            <label for="username" class="block font-normal uppercase tracking-wide text-xs mb-1">Никнейм</label>
            <input type="text"
                   v-model="username"
                   id="username"
                   class="border px-4 py-2 w-full rounded bg-gray-200"
                   @keydown.shift.tab.prevent=""
                   :class="{invalid: ($v.username.$dirty && !$v.username.required) || ($v.username.$dirty && !$v.username.minLength)}">
            <small
                class="text-red-800"
                v-if="$v.username.$dirty && !$v.username.required"
            >Поле Логина не должно быть пустым</small>
            <small
                class="text-red-800 text-xs "
                v-else-if="$v.username.$dirty && !$v.username.minLength"
            >Поле Логина не менее 5 символов. Сейчас оно {{username.length}}</small>
            <p><small class="text-muted text-xs font-normal">Минимальная длина логина 5 символов</small></p>
          </div>
          <div class="form-group required mb-4">
            <label for="first_name" class="block font-normal uppercase tracking-wide text-xs mb-1">Имя</label>
            <input type="text"
                   :class="{invalid: ($v.first_name.$dirty && !$v.first_name.required)}"
                   v-model="first_name" id="first_name" name="first_name" class="border px-4 py-2 w-full rounded bg-gray-200" ref="first_name" @keydown.shift.tab.prevent="">
            <small
                class="text-red-800"
                v-if="$v.first_name.$dirty && !$v.first_name.required"
            >Поле имени не должно быть пустым</small>
          </div>
          <div class="form-group required mb-4">
            <label for="last_name" class="block font-normal uppercase tracking-wide text-xs mb-1">Фамилия</label>
            <input type="text"
                   :class="{invalid: ($v.last_name.$dirty && !$v.last_name.required)}"
                   v-model="last_name" id="last_name" name="last_name" class="border px-4 py-2 w-full rounded bg-gray-200" ref="last_name" @keydown.shift.tab.prevent="">
            <small
                class="text-red-800"
                v-if="$v.last_name.$dirty && !$v.last_name.required"
            >Поле фамилии не должно быть пустым</small>
          </div>
          <div class="form-group required mb-4">
            <label for="email" class="block font-normal uppercase tracking-wide text-xs mb-1">Почта</label>
            <input type="email"
                   :class="{invalid: ($v.email.$dirty && !$v.email.required)}"
                   v-model="email" id="email" name="email" class="border px-4 py-2 w-full rounded bg-gray-200" ref="email" @keydown.shift.tab.prevent="">
            <small
                class="text-red-800"
                v-if="$v.email.$dirty && !$v.email.required"
            >Поле почты не должно быть пустым</small>
          </div>
          <div class="form-group required mb-4">
            <label for="phone" class="block font-normal uppercase tracking-wide text-xs mb-1">Телефон</label>
            <input type="text"
                   :class="{invalid: ($v.phone.$dirty && !$v.phone.required)}"

            v-model="phone" id="phone" v-imask="phoneNumberMask" placeholder="+375(33)123-45-67" maxlength="17" name="phone" class="border px-4 py-2 w-full rounded bg-gray-200"
                   ref="phone" @keydown.shift.tab.prevent="">
            <small
                class="text-red-800"
                v-if="$v.phone.$dirty && !$v.phone.required"
            >Поле телефона не должно быть пустым</small>
          </div>
          <div class="form-group required required mb-4">
            <label for="password" class="block font-normal uppercase tracking-wide text-xs mb-1">Пароль</label>
            <input type="password"
                   v-model="password"
                   id="password"
                   class="border px-4 py-2 w-full rounded bg-gray-200"
                   :class="{invalid: ($v.password.$dirty && !$v.password.required) || ($v.password.$dirty && !$v.password.minLength)}">
            <small
                class="text-red-800"
                v-if="$v.password.$dirty && !$v.password.required"
            >Поле пароля не должно быть пустым</small>
            <small
                class="text-red-800 text-xs"
                v-else-if="$v.password.$dirty && !$v.password.minLength"
            >Поле пароля не менее 8 символов. Сейчас оно {{password.length}}</small>
            <p><small class="text-muted text-xs font-normal">Минимальная длина пароля 8 символов</small></p>
          </div>
          <div class="form-group required mb-8">
            <label for="confirm_password" class="block font-normal uppercase tracking-wide text-xs mb-1">Повторите пароль</label>
            <input type="password"
                   v-model="confirm_password"
                   id="confirm_password"
                   class="border px-4 py-2 w-full rounded bg-gray-200"
                   :class="{invalid: ($v.confirm_password.$dirty && !$v.confirm_password.required) || ($v.confirm_password.$dirty && !$v.confirm_password.sameAs)}">
            <small
                class="text-red-800 text-xs"
                v-if="$v.confirm_password.required && !$v.confirm_password.sameAs"
            >Введенные пароли не совпадают</small>
          </div>


          <div class="form-group mb-4">
            <button  type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-800 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Зарегистрироваться</button>
          </div>
          <p class="mt-2"><small class="text-muted">Все поля отмеченные <span class="text-danger">*</span> обязательны для заполнения</small></p>
        </form>
        <div class="text-sm font-normal text-center">
          <p>Уже есть аккаунт? <a href="#" class="text-blue-600 hover:text-blue-800" @click.prevent="showLogin" @keydown.tab.exact.prevent="">Войти</a></p>
        </div>

      </div>
    </modal>
  </div>
</template>

<script>
  import Swal from 'sweetalert2'
  import { required, minLength, sameAs} from 'vuelidate/lib/validators'
  import { IMaskDirective } from 'vue-imask';
  import $ from 'jquery'

export default {
  data() {
 return {
        username: "",
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        phone: "",
        confirm_password: "",
        userPhone: "",
        phoneNumberMask: {
        mask: '+{375}(00)000-00-00',
        lazy: true
},
     err: ''
 };
  },
  validations: {
    username: {
    required,
    minLength:minLength(5)
},
    last_name:{
      required
    },
    first_name:{
      required
    },
    email:{
  required,
    },
password: {
  required,
  minLength: minLength(8)
},
confirm_password: {
required,
     sameAs: sameAs('password')
},
phone: {
required
}
 },
  methods: {
    show() {
      this.$modal.show('modal-register')
    },
    register: function (event) {
      if(this.$v.$invalid){
        this.$v.$touch()
        return
      }
      event.preventDefault();
      console.log(this.form);
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/",
        type: "POST",
        data:{
          username:this.username,
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          password: this.password,
          phone: this.phone,
          confirm_password: this.confirm_password,
          userPhone: this.userPhone,

        } ,
        success: (response) => {
          Swal.fire({
            type: 'success',
            title: 'Вы успешно зарегистрировались, сейчас вы отправитесь на главную страницу',
            showConfirmButton: false,
          })
          setTimeout(() => {   window.location.href = "/" }, 1000);
        },
        error: (response) => {
          console.log(error)
          if (response.status === 400) {
            alert('Логин или пароль не верны')
          }
        }
      })
    },
    showLogin() {
      this.$modal.show('modal-login')
      this.$modal.hide('modal-register')
    },
    opened() {
      this.$refs.email.focus()
    },
    hide() {
      this.$modal.hide('modal-register')
    },
    onAccept(e) {
 const maskRef = e.detail
 this.phone = maskRef.value
 },
 onComplete(e) {
 const maskRef = e.detail
 this.userPhone = maskRef.unmaskedValue
 },
 isNumber(e) {
 let regex = /[0-9]/

 if (!regex.test(e.key)) {
 e.returnValue = false;
 if (e.preventDefault) e.preventDefault();
 }
 }
  },
  directives: {
    imask: IMaskDirective
  },
}
</script>

<style>
  .form-group.required:after{
    content: " *";
    color:red;
  }
</style>

