<template>
  <div>
    <div class="min-h-screen flex items-center justify-center bg-green-200 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-md w-full space-y-8">
        <div>
          <h1 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Список комнат</h1>
        </div>

    <div class="rounded-md shadow-sm -space-y-px">
      <form>
        <div>
          <input v-model="room" type="text" id="room" name="room" class="mb-2 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-600 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Название комнаты" />
        </div>

        <div class="form-group mb-4">
          <button @click="AddRoom" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-800 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
            Добавить
          </button>
        </div>
      </form>
<div v-for="r in rooms" :key="r.id">
      <h1 class="font-bold">Комната: {{r.attributes.name}} {{r.id}}  </h1>
  <div>
    <button @click="deleteChat(r.id)" type="submit" class=" mb-8 group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-800 hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">Удалить</button>
  </div>
</div>
    </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import $ from "jquery";
import Swal from "sweetalert2";

export default {
  name: "AdminChat",
  data(){
    return{
        room:'',
        rooms:[]

    }
  },
  created(){
    this.LoadRooms();
  },
  methods:{
    AddRoom(){
      const fd = new FormData();
      fd.append('name',this.room )

      axios.post('http://127.0.0.1:8000/api/room/new/',fd)
          .then(res => {
            console.log(res)
            Swal.fire({
              type: 'success',
              title: 'Комната добавлена',
              showConfirmButton: false,
              timer:2000
            })
          })
    },
    deleteChat(id_room){
      $.ajax({
        url: "http://127.0.0.1:8000/api/room/destroy/" + id_room,
        type: "DELETE",
        success: (response) => {
          console.log("SUCCESS",response)
          Swal.fire({
            type: 'success',
            title: 'Комната удалена',
            showConfirmButton: false,
            timer:1000
          })
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Что-то нетак')
          }
        }
      })
    },
    LoadRooms(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/room/",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.rooms = response.data;
          this.id_room = response.data.id;
          console.log(this.id_room)
        }
      })
    }
  }
}
</script>

<style scoped>

</style>