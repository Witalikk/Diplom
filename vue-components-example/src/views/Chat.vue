<template>
  <div v-model="mode" :class="(mode === 'dark') ? 'dark' : ''" @toggle="toggle" >
  <div id="chat" class="bg-gradient-to-br from-green-600 to-cyan-600 to-green-300 flex-1 p:2 sm:p-6 justify-between flex flex-col h-screen ml-32 mr-32 ">

    <div class="flex sm:items-center justify-between py-3 border-b-2 border-gray-200">
        <h1>{{roomName}}</h1>
      <Toggle :mode="mode" @toggle="toggle"></Toggle>
    </div>

    <div id="messages" ref="block" class="flex flex-col space-y-4 p-3 overflow-y-auto scrollbar-thumb-blue scrollbar-thumb-rounded scrollbar-track-blue-lighter scrollbar-w-2 scrolling-touch">
      <h1 class="text-center">Начало чата</h1>
      <div   v-for="s in smsList" ref="smsList"  class="chat-message">
        <template v-model="smsList" >
        <div class="flex items-end" v-bind:class="{ owner: user_id == s.attributes.user.id}">

          <div v-if="username === 'admin'">
            <button @click="deleteSms(s.id)" type="submit">
              <img src="https://img.icons8.com/plumpy/24/4a90e2/delete-sign--v2.png"/>
            </button>
          </div>
          <div v-if="user_id == s.attributes.user.id && username !='admin' ">
            <button @click="deleteSms(s.id)" type="submit">
              <img  src="https://img.icons8.com/plumpy/24/4a90e2/delete-sign--v2.png"/>
            </button>
          </div>

          <span  class="font-medium text-xs ">{{s.attributes.user.username}}</span>
          <div class="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-1 items-end">

            <div><span class="break-words w-64 px-4 py-2 rounded-lg inline-block rounded-br-none bg-blue-600 text-white" v-bind:class="[{bgadmin: s.attributes.user.id == 1}, {bg: s.attributes.user.id != 1},{bgme: s.attributes.user.id == user_id}]" >{{s.attributes.sms}}</span></div>

          </div>

<!--          <img src="https://images.unsplash.com/photo-1590031905470-a1a1feacbb0b?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=3&amp;w=144&amp;h=144" alt="My profile" class="w-6 h-6 rounded-full order-2">-->
        </div>
        </template>
      </div>
    </div>
    <div class="border-t-2 border-gray-200 px-4 pt-4 mb-2 sm:mb-0">
      <div class="relative flex">
        <form>
        <input
            v-model="sms" id="sms" name="sms" type="text" placeholder="Написать" class="w-full focus:outline-none focus:placeholder-gray-400 text-gray-600 placeholder-gray-600 pl-12 pr-8 bg-gray-200 rounded-full py-3"
            :class="{invalid: ($v.sms.$dirty && !$v.sms.maxLength)}">
          <small
              class="text-red-800 text-sm font-bold"
              v-if="$v.sms.$dirty && !$v.sms.maxLength"
          >Cообщение должно иметь не более 150 символов Сейчас оно {{sms.length}} символов</small>

        </form>
          <div class="absolute right-0 items-center inset-y-0 hidden sm:flex">
            <div v-if="user_id != null" class="form-group mb-4">
              <button @click="AddSms" class="inline-flex items-center justify-center rounded-full h-12 w-12 transition duration-500 ease-in-out text-white bg-black hover:bg-gray-600 focus:outline-none">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-6 w-6 transform rotate-90">
                  <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z"></path>
                </svg>
              </button>
            </div>
            <div v-if="user_id == null" class="form-group mb-4 inline-flex items-end">
              <h1 class="mb-3 mr-2">Нужно авторизоваться</h1>
          <button  @click="AddSms" class="inline-flex items-center justify-center rounded-full h-12 w-12 transition duration-500 ease-in-out text-white bg-black hover:bg-gray-600 focus:outline-none opacity-50 cursor-not-allowed">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-6 w-6 transform rotate-90">
              <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z"></path>
            </svg>
          </button>

            </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>
<script>
import $ from "jquery";
import axios from "axios";
import Swal from "sweetalert2";
import Toggle from '@/components/Toggle.vue'
import  {maxLength } from 'vuelidate/lib/validators';

export default {
  name: "Chat",
  components:{
    Toggle
  },
  props: {
    id: String,
    roomName:String
  },
  data(){
    return{
      room:'',
      sms:'',
      user_id:null,
      smsList:[],
      room_id:'',
      username:'',
      mode: 'light'

    }
  },
  validations: {
    sms: {
      maxLength: maxLength(150),
    },
  },
  created(){
    // const el = document.getElementById('messages')
    // el.scrollTop = el.scrollHeight
    this.LoadRooms();
    // localStorage["myData"] = this.$route.params.id
    this.LoadUser();
    this.LoadSms();
    this.room_id = this.$route.params.id
    this.mode =  localStorage.getItem('mode')
  },

  methods:{
    toggle () {
      if (this.mode === "dark") {
        this.mode = "light"
        localStorage.setItem('mode', this.mode)
      } else {
        this.mode = "dark"
        localStorage.setItem('mode', this.mode)

      }
    },
    deleteSms(id_sms){
      $.ajax({
        url: "http://127.0.0.1:8000/api/sms/destroy/" + id_sms,
        type: "DELETE",
        success: (response) => {
          console.log("SUCCESS",response)
          Swal.fire({
            type: 'success',
            title: 'Сообщение удалено',
            showConfirmButton: false,
            timer:1000
          })
          // setTimeout(() => {   window.location.reload(); }, 1000);
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Что-то нетак')
          }
        }
      })
    },

    AddSms: function (event){
      if(this.$v.$invalid){
        this.$v.$touch()
        return
      }
      const fd = new FormData();
      const datestr = new Date().toLocaleString();
      fd.append('sms', this.sms )
      fd.append('room', this.$route.params.id )
      fd.append('user', this.user_id )
      fd.append('date', datestr )

      axios.post('http://127.0.0.1:8000/api/sms/new/',fd)

          .then(res => {
            console.log(res,"POST SMS")
            Swal.fire({
              type: 'success',
              title: 'Отправлено',
              showConfirmButton: false,
              timer:1000
            })
            setTimeout(() => {   window.location.reload(); }, 1000);
            console.log(this.smsList,"SMOTRET")
          })
          .catch(function (error) {
            console.log(datestr);
            console.log(fd);

          });
    },
    LoadRooms(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/room/",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.room = response.data;
          console.log(this.id,"IDSHKA")
        },
        error: (response) => {
          if (response.status === 400) {

            alert('Что-то не так')
          }
        }
      })
    },
    LoadUser() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/me/",
        contentType: 'application/vnd.api+json',
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')},
        type: "GET",
        success: (response) => {
          this.user_id = response.data.id;
          this.username = response.data.attributes.username;


        }
      })
    },
    LoadSms(){
      $.ajax({
        url: `http://127.0.0.1:8000/api/sms?room= ${this.id}` ,
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.smsList = response.data;
          this.$nextTick(() => {
            this.$refs.block.scrollTop = this.$refs.block.scrollHeight;
          });
          console.log(this.smsList,"SMSList")
        }
      })
    }
  }
}
</script>

<style scoped>
.dark {
  background: black;
  color: black;
  transition: background 0.3s ease-in;
}
.dark div{
  background: #1f1e1e;
  color: #c7c5c5;
  transition: background 0.3s ease-in;
}

.light {
  background: white;
  color: white;
  /*transition: background 0.8s ease-in-out;*/
}





.scrollbar-w-2::-webkit-scrollbar {
  width: 0.25rem;
  height: 0.25rem;
  overflow-y:auto;
}

.owner {
  color: #2a2a2a;
  display: flex;
  /*justify-items: end;*/
  justify-content: flex-end;
}
.bg {
  /*background: #2c2d30;*/
  background: #3a3a3a;
}
.bgme {
  /*background: #2c2d30;*/
  background: #344feb;
}
.bgadmin {
  /*background: #2c2d30;*/
  background: #f50a0a;
}
.scrollbar-track-blue-lighter::-webkit-scrollbar-track {
  --bg-opacity: 1;
  background-color: #f7fafc;
  background-color: rgba(247, 250, 252, var(--bg-opacity));
}

.scrollbar-thumb-blue::-webkit-scrollbar-thumb {
  --bg-opacity: 1;
  background-color: #edf2f7;
  background-color: rgba(237, 242, 247, var(--bg-opacity));
}

.scrollbar-thumb-rounded::-webkit-scrollbar-thumb {
  border-radius: 0.25rem;
}
</style>