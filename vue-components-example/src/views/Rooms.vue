<template>
  <div>
    <div class="min-h-screen flex items-center justify-center bg-green-200 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-md w-full space-y-8">
        <div>
          <h1 class=" text-center text-3xl font-extrabold text-gray-900">Список комнат</h1>
        </div>

        <div class="rounded-md text-2xl shadow-sm -space-y-px">
          <div v-for="r in rooms" :key="r.id">
            <router-link :to="{name:'chatt', params:{id:r.id,roomName:r.attributes.name}}" class="font-bold text-xl flex items-end">
            <h1 class="mb-2">{{r.attributes.name}}</h1>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from "jquery";

export default {
  name: "Rooms",
  data(){
    return{
      rooms:[],
    }
  },
  created(){
    this.LoadRooms();
  },
  methods:{
    LoadRooms(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/room/",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.rooms = response.data;
          console.log(this.rooms)
        }
      })
    }
  }
}
</script>

<style scoped>

</style>