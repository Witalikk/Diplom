<template>
  <div class="flex flex-col ">
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8 ">
      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
        <div class="grid grid-cols-2 mr-2 ml-2 gap-4 ">
          <div>
            <h1 class="text-center text-xl font-bold">Покупка</h1>
          <table class="mr-4 min-w-full divide-y divide-gray-200 shadow overflow-hidden border-b border-gray-400 sm:rounded-lg bg-gradient-to-br from-red-500 to-red-700">
            <thead class="bg-gray-50">
            <tr>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                Автомобиль
              </th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                Пользователь
              </th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                Действие
              </th>
              <th scope="col" class="relative px-6 py-3">
                <span class="sr-only">Edit</span>
              </th>
            </tr>
            </thead>
            <tbody v-for="date in inquiry" :key="date.id"  class="bg-white divide-y divide-gray-200">
            <tr v-if="date.attributes.date_inquiry === null" >
              <td class="px-2 py-4 whitespace-nowrap">
                <div class="flex items-center">
                  <div class="ml-2">
                    <div class="text-sm font-medium text-gray-900">
                      {{date.attributes.model.marka.marka}}: {{date.attributes.model.model}}
                    </div>
                    <div class="text-sm font-medium text-gray-900">
                      Тип кузова: {{date.attributes.model.body_type }}
                    </div>
                    <div class="text-sm font-medium text-gray-900">
                      Цена: {{date.attributes.model.price }}$
                    </div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">
                  {{date.attributes.user.username }}
                </div>
                <div class="text-sm text-gray-900">
                  {{date.attributes.user.email}}
                </div>
                <div class="text-sm text-gray-500">{{date.attributes.user.phone}}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                <button @click="buy_car(date.attributes.user.id, date.attributes.model.id, date.id)" type="submit" class="mb-1 mr-2 inline-flex justify-center py-1 px-5 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                  Принять
                </button>
                <button @click="cancel_buy(date.id)" type="submit" class="inline-flex justify-center py-1 px-3 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                  Отклонить
                </button>
              </td>

              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">

              </td>
            </tr>
            </tbody>
          </table>
          </div>

          <div>
            <h1 class="text-center text-xl font-bold">Тест-драйв</h1>
          <table class="mr-4 min-w-full divide-y divide-gray-200 shadow overflow-hidden border-b border-gray-400 sm:rounded-lg bg-gradient-to-br from-gray-600 to-gray-700">
            <thead class="bg-gray-50">
            <tr >
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                Автомобиль
              </th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                Пользователь
              </th>
              <th scope="col" class="px-8 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                Дата
              </th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                Действие
              </th>
              <th scope="col" class="relative px-6 py-3">
                <span class="sr-only">Edit</span>
              </th>
            </tr>
            </thead>
            <tbody v-for="date in inquiry" :key="date.id"  class="bg-white divide-y divide-gray-200">
            <tr v-if="date.attributes.date_inquiry != null" >
              <td class="px-2 py-4 whitespace-nowrap">
                <div class="flex items-center">
                  <div class="ml-2">
                    <div class="text-sm font-medium text-gray-900">
                      {{date.attributes.model.marka.marka}}: {{date.attributes.model.model}}
                    </div>
                    <div class="text-sm font-medium text-gray-900">
                      Тип кузова: {{date.attributes.model.body_type }}
                    </div>
                    <div class="text-sm font-medium text-gray-900">
                      Цена: {{date.attributes.model.price }}$
                    </div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">
                  {{date.attributes.user.username }}
                </div>
                <div class="text-sm text-gray-900">
                  {{date.attributes.user.email}}
                </div>
                <div class="text-sm text-gray-500">{{date.attributes.user.phone}}</div>
              </td>
              <td class=" py-2 whitespace-nowrap">
                {{date.attributes.date_inquiry }}
              </td>
              <td class="px-4 py-4 whitespace-nowrap text-sm text-gray-500">
                <button @click="test_drive(date.attributes.user.id, date.attributes.model.id, date.id, date.attributes.date_inquiry)" type="submit" class="mb-1 mr-2 inline-flex justify-center py-1 px-5 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                  Принять
                </button>
                <button @click="cancel_test_drive(date.id)" type="submit" class="inline-flex justify-center py-1 px-3 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                  Отклонить
                </button>
              </td>

              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">

              </td>
            </tr>
            </tbody>
          </table>
          </div>
        </div>
      </div>
    </div>
  </div>


</template>

<script>
  import $ from 'jquery'
  export default {
    name: 'AdminPage',
    data() {
      return {
        inquiry: [],
        buy: {
          user: null,
          model: null
        },
        testDrive: {
          user: null,
          model: null,
          date_inquiry: null
        },
      }
    },
    created() {
      this.loadInquiry()
    },
    methods: {
      loadInquiry() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/inquiry/",
          contentType: 'application/vnd.api+json',
          type: "GET",
          success: (response) => {
            this.inquiry = response.data;
            console.log(this.inquiry)
          }
        })
      },
      buy_car(id_user, id_model, id_inquiry){
        this.buy.user = id_user;
        this.buy.model = id_model;
        $.ajax({
          url: "http://127.0.0.1:8000/api/sold-car/new/",
          type: "POST",
          data: this.buy,
          success: (response) => {
            console.log("SUCCESS",response)
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Что-то нетак'+ this.model)
            }
          }
        }),
        $.ajax({
          url: "http://127.0.0.1:8000/api/inquiry/" + id_inquiry,
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
      },
      cancel_buy(id_inquiry){
        $.ajax({
          url: "http://127.0.0.1:8000/api/inquiry/" + id_inquiry,
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
      },
      test_drive(id_user, id_model, id_inquiry, data_inquiry){
        this.testDrive.user = id_user;
        this.testDrive.model = id_model;
        this.testDrive.date_inquiry = data_inquiry;
        $.ajax({
          url: "http://127.0.0.1:8000/api/test-drive/new/",
          type: "POST",
          data: this.testDrive,
          success: (response) => {
            console.log("SUCCESS",response)
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Что-то нетак'+ this.testDrive)
            }
          }
        }),
        $.ajax({
          url: "http://127.0.0.1:8000/api/inquiry/" + id_inquiry,
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
      },
      cancel_test_drive(id_inquiry){
        $.ajax({
          url: "http://127.0.0.1:8000/api/inquiry/" + id_inquiry,
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
      },
      show() {
        this.$modal.show('modal')
        // this.$modal.hide('modal')
      },
      hide(){
        this.$modal.hide('modal');
      },
      show_auto() {
        this.$modal.show('modal-auto')
      }
    }
  }
</script>

<style scoped>

</style>