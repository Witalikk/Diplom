<template>
  <div class="flex flex-col ">
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8 ">
      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
        <div class=" mr-2 ml-2 gap-4 ">
          <div>
            <h1 class="text-center text-xl font-bold mb-6">Управление пользователями</h1>
            <table class="mr-4 min-w-full divide-y divide-gray-200 shadow overflow-hidden border-b border-gray-400 sm:rounded-lg bg-gradient-to-br from-red-500 to-red-700">
              <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="block h-90 overflow-auto px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                  Никнейм
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                  Имя
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                  Фамилия
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                  Почта
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                  Телефон
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                  Дата регистрации
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                  Последний раз заходил
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                  Действие
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <span class="sr-only">Edit</span>
                </th>
              </tr>
              </thead>
              <tbody v-for="date in users" :key="date.id"   class="bg-white divide-y divide-gray-200">
              <tr v-if="date.attributes.username != 'admin'" >
                <td class="px-2 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="ml-2">
                      <div class="text-sm font-medium text-gray-900">
                        {{date.attributes.username}}
                      </div>

                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">
                    {{date.attributes.first_name}}
                  </div>

                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">
                    {{date.attributes.last_name}}
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">
                    {{date.attributes.email}}
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">
                    {{date.attributes.phone}}
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">
                    {{date.attributes.date_joined}}
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div v-if="date.attributes.last_login != null" class="text-sm text-gray-900">
                    {{date.attributes.last_login}}
                  </div>
                  <div v-else class="text-sm text-gray-900">
                    Еще не заходил
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  <button @click="deleteUser(date.id)" type="submit" class="inline-flex justify-center py-1 px-3 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    Удалить
                  </button>
                </td>

                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">

                </td>
              </tr>
              </tbody>
            </table>
          </div>
          <div>
          </div>
        </div>
      </div>
    </div>
  </div>


</template>

<script>
import $ from "jquery";
import Swal from "sweetalert2";

export default {
  name: "UserManagement",
  data(){
    return {
      users:[],
    }
  },
  created(){
    this.allUser();
  },
  methods: {
    deleteUser(id_user){
      $.ajax({
        url: "http://127.0.0.1:8000/api/user/destroy/" + id_user,
        type: "DELETE",
        success: (response) => {
          console.log("SUCCESS",response)
          Swal.fire({
            type: 'success',
            title: 'Пользователь удален',
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
    allUser() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/allUsers",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.users = response.data;
          console.log(this.users,"ПОЛУЧЕНЫ ПОЛЬЗОВАТЕЛИ")
        }
      })
    }
  }
}
</script>

<style scoped>

</style>