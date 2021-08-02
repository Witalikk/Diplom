<template>
  <div class="flex-wrapper bg-green-200">
<!--      <img :src="logo" alt="logo">-->

    <div class="calculator-content">
      <div class="calculator-content-title">
        <h1>Рассчитайте кредит</h1>
      </div>
      <div class="calculator-content-body">
        <div class="calculator-content-body-left">
          <div class="calculator-content-body-left-inputs">
            <div class="input-wrapper">
              <div class="title">Стоимость Автомобиля $</div>
              <div class="input">
                <input type="number" readonly id="total-cost" v-model="price" name="price">
              </div>
<!--              <div class="input">-->
<!--                <input type="range" min="0" max="250000" id="total-cost-range" v-model="price" name="price" class="input-range">-->
<!--              </div>-->
            </div>
            <div class="input-wrapper">
              <div class="title">Первоначальный взнос</div>
              <div class="input">
                <input type="number" id="an-initial-fee" value="0">
              </div>
<!--              <div class="input">-->
<!--                <input type="range" min="5000" max="100000" id="an-initial-fee-range" value="0" class="input-range">-->
<!--              </div>-->
            </div>
            <div class="input-wrapper">
              <div class="title">Срок кредита</div>
              <div class="input">
                <input type="number" id="credit-term" value="0">
              </div>
              <div class="input">
                <input type="range" min="1" max="20" id="credit-term-range" value="0" class="input-range">
              </div>
            </div>
          </div>
          <div class="calculator-content-title">
            <h2>Выбрать банк</h2>
          </div>
          <div class="calculator-content-body-left-btns">
            <button data-name="alfa" class="bank active">
              <div class="text">Альфа-банк</div>
              <div class="value">8,7%</div>
            </button>
            <button data-name="sberbank" class="bank">
              <div class="text">Сбербанк</div>
              <div class="value">8,4%</div>
            </button>
            <button data-name="pochta" class="bank">
              <div class="text">Почта-банк</div>
              <div class="value">7,9%</div>
            </button>
            <button data-name="tinkoff" class="bank">
              <div class="text">Тинькофф-банк</div>
              <div class="value">9,2%</div>
            </button>
          </div>
        </div>
        <div class="calculator-content-body-right">
          <div class="final-results-wrapper">
            <div class="final-result-item">
              <div class="title">Сумма кредита</div>
              <div class="value" id="amount-of-credit">0<span>$</span></div>
            </div>
            <div class="final-result-item">
              <div class="title">Ежемесячный платеж</div>
              <div class="value" id="monthly-payment">0<span>$</span></div>
            </div>
            <div class="final-result-item">
              <div class="title">Рекомендуемый доход</div>
              <div class="value" id="recommended-income">0<span>$</span></div>
            </div>
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
  name: "Credit",
  data() {
    return{
      price: null,
      logo: null,
    }
  },
  created(){
    this.loadMod()
  },
  methods:{
    loadMod() {
      $.ajax({
        url: `http://127.0.0.1:8000/api/models/${this.$route.params.id}`,
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.price = response.data.attributes.price;
          this.logo = response.data.attributes.logo;
        }
      })
    }
  },

  mounted(){
    Swal.fire({
      type: 'info',
      title: 'Рассчет кредита.',
      text: 'Здравствуйте, для рассчета кредита вам' +
          `ужно ввести первоначальный взнос, срок кредита и выбрать подходящий банк.` +
          'А мы рассчитаем ежемесячный платеж и рекумендуемый доход.',
      showConfirmButton: false,
    })
    /* Стоимость */
    const totalCost = document.getElementById('total-cost');
    var totalCostRange = document.getElementById('total-cost');

    /* Первоначальный взнос */
    var anInitialFee = document.getElementById('an-initial-fee');
    var anInitialFeeRange = document.getElementById('an-initial-fee');

    /* Срок кредита */
    var creditTerm = document.getElementById('credit-term');
    var creditTermRange = document.getElementById('credit-term-range');

    /* Вывод итоговых значений */
    var totalAmountOfCredit = document.getElementById('amount-of-credit');
    var totalMonthlyPayment = document.getElementById('monthly-payment');
    var recommendedIncome = document.getElementById('recommended-income');

    /* Все range */
    var inputsRange = document.querySelectorAll('.input-range');

    /* Все банки */
    var bankBtns = document.querySelectorAll('.bank');

    var assignValue = () => {
      totalCost.value = totalCostRange.value;
      anInitialFee.value = anInitialFee.value;
      creditTerm.value = creditTermRange.value;
    };

    assignValue();

    var banks = [
      {
        name: 'alfa',
        percent: 8.7
      },
      {
        name: 'sberbank',
        percent: 8.4
      },
      {
        name: 'pochta',
        percent: 7.9
      },
      {
        name: 'tinkoff',
        percent: 9.2
      },
    ];

    /* По умолчанию выбран первый банк */
    let currentPrecent = banks[0].percent;

    for(let bank of bankBtns) {
      bank.addEventListener('click', () => {
        for(let item of bankBtns) {
          item.classList.remove('active');
        }
        bank.classList.add('active');
        takeActiveBank(bank);
      });
    };

    var takeActiveBank = currentActive => {
      var dataAttrValue = currentActive.dataset.name;
      var currentBank = banks.find(bank => bank.name === dataAttrValue);

      currentPrecent = currentBank.percent;
      calculation(totalCost.value, anInitialFee.value, creditTerm.value)
    };

    for(let input of inputsRange) {
      input.addEventListener('input', () => {
        assignValue();
        calculation(totalCost.value, anInitialFee.value, creditTerm.value);
      });
    };

    var calculation = (totalCost = 0, anInitialFee = 100000, creditTerm = 1) => {
      /*
          ЕП - ежемесячныплатёж
          РК - размер кредита
          ПС - процентная ставка
          КМ - количество месяцев
          ЕП = (РК + ((( РК / 100) * ПС) *КМ) / КМ;
      */

      let monthlyPayment; // Ежемесячны платёж
      let lountAmount = totalCost - anInitialFee; // Размер кредита
      let interestRate = currentPrecent; // Процентная ставка
      let amountOfYears = creditTerm; //Количество лет
      let amountOfMoths = 12 * amountOfYears; // Количество месяцев

      monthlyPayment = (lountAmount + (((lountAmount / 100) * interestRate) / 12) * amountOfMoths) / amountOfMoths;

      var monthlyPaymentArounded = Math.round(monthlyPayment);

      if(monthlyPaymentArounded < 0) {
        return false;
      } else {
        totalAmountOfCredit.innerHTML = `${lountAmount} $`;
        totalMonthlyPayment.innerHTML = `${monthlyPaymentArounded} $`;
        recommendedIncome.innerHTML = `${monthlyPaymentArounded + monthlyPaymentArounded * 0.4} $`;
      }
    };
  }
  }

</script>

<style scoped>
h1, h2 {
  margin: 0;
  padding: 0;
  font-weight: 500;
  font-size: 30px;
  line-height: 37px;
  color: #071124;
}

h2 {
  font-size: 25px;
  line-height: 30px;
}

button {
  border: none;
  outline: none;
}

input[type='number'] {
  -moz-appearance:textfield;
}

input[type='range'] {
  width: 100%;
}

input[type=range] {
  -webkit-appearance: none;
  width: 100%;
}

input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
}

input[type=range]:focus {
  outline: none;
}

input[type='range'] {
  width: 100%;
  -webkit-appearance: none;
  background-color: #F9FAFC;
}

input[type='range']::-webkit-slider-thumb {
  -webkit-appearance: none;
  cursor: ew-resize;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #599FF1;
  margin-top: -25px;
}


input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.flex-wrapper {
  display: flex;
  justify-content: center;
  width: 100%;
}

.calculator-content {
  width: 100%;
  max-width: 950px;
  padding-top: 100px;
}

.calculator-content-title {
  padding-bottom: 14px;
  border-bottom: 2px solid #E4E6EE;
}

.calculator-content-body {
  display: flex;
}

.calculator-content-body-left,
.calculator-content-body-right {
  width: 50%;
  border-right: 2px solid #E4E6EE;
  padding-top: 40px;

}

.calculator-content-body-right {
  padding-right: 0;
  padding-left: 30px;
  border-right: none;

}

.calculator-content-body-left-inputs,
.calculator-content-body-left-btns {
  padding-right: 30px;


}

.calculator-content-body-left-inputs {
  margin-bottom: 100px;

}

.input-wrapper {
  margin-bottom: 43px;
}

.input-wrapper:last-child {
  margin-bottom: 0;
}

.input-wrapper .title {
  font-weight: 500;
  font-size: 18px;
  line-height: 22px;
  color: rgba(7, 17, 36, 0.5);
  margin-bottom: 8px;
}

.input-wrapper input[type="number"] {
  width: 100%;
  background-color: #ffffff;
  border: 2px solid #E4E6EE;
  height: 50px;
  font-weight: 500;
  font-size: 18px;
  line-height: 22px;
  color: #071124;
}

.calculator-content-body-left-btns {
  padding-top: 40px;
}

.calculator-content-body-left-btns button {
  width: 100%;
  display: flex;
  justify-content: space-between;
  background: #FFFFFF;
  border: 2px solid #E4E6EE;
  height: 50px;
  margin-bottom: 20px;
}

.calculator-content-body-left-btns button .text,
.calculator-content-body-left-btns button .value {
  font-weight: 500;
  font-size: 18px;
  line-height: 22px;
  color: #071124;

}

.final-result-item {
  margin-bottom: 35px;
}


.final-result-item:last-child {
  margin-bottom: 0;
}

.final-result-item .title {
  font-weight: 500;
  font-size: 18px;
  line-height: 22px;
  color: rgba(7, 17, 36, 0.5);
  margin-bottom: 8px;
}

.final-result-item .value {
  font-weight: 500;
  font-size: 30px;
  line-height: 37px;
  color: #071124;
}

.bank.active {
  border-color:#80f567
}

</style>