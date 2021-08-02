<template>
  <div>
  <div class="quiz-over-modal">
    <div class="content">
      <h1>Хороший результат!</h1>
      <p>Ты ответил на
        <span id="correct-answer"></span> из
        <span id="number-of-all-questions-2"></span> вопросов
      </p>
      <button id="btn-try-again">Попробуй снова</button>
    </div>
  </div>
  <div class="quiz-container">
    <div class="question-number">
      <h2>Вопросы на знание марки Audi</h2>
      <h3>Вопрос
        <span id="number-of-question"></span>
        из
        <span id="number-of-all-questions"></span>
      </h3>
    </div>
    <div id="question"></div>
    <div class="options">
      <div data-id="0" class="option option1"></div>
      <div data-id="1" class="option option2"></div>
      <div data-id="2" class="option option3"></div>
      <div data-id="3" class="option option4"></div>
    </div>
    <div class="flex flex-row">
    <div class="button">
      <button id="btn-next">Следующий вопрос</button>
    </div>
      <div class="button">
    <router-link :to="`/`" class="font-bold text-xl flex items-end">
      <button id="btn-next" class="ml-4">
        Вернуться на главную
      </button>
    </router-link>
      </div>
    </div>
    <div id="answers-tracker">

    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: "Quiz",
  created(){
    this.load()
    load()
  },
  methods:{

  },
  mounted(){
    //Константы вариантов ответов
    const option1 = document.querySelector('.option1'),
        option2 = document.querySelector('.option2'),
        option3 = document.querySelector('.option3'),
        option4 = document.querySelector('.option4');

//Массив div options с его элементами
    const optionElements = document.querySelectorAll('.option');

//Константа заданого вопроса
    const question = document.getElementById('question');

//Константы количества вопросов и какой по счету идет вопрос
    const numberOfQuestion = document.getElementById('number-of-question'),
        numberOfAllQuestions = document.getElementById('number-of-all-questions');

// переменные страницы и вопроса
    let indexOfQuestion,
        indexOfPage = 0;

//Константа просмотра количества вопросов, и правильных или не правельных ответов
    const answersTracker = document.getElementById('answers-tracker');

//Кнопка перехода к следующему вопросу
    const btnNext = document.getElementById('btn-next');

//Переменная правильных ответов
    let score = 0;

// количество правильных ответов и кнопка "начать заново"
    const correctAnswer = document.getElementById('correct-answer'),
        numberOfAllQuestions2 = document.getElementById('number-of-all-questions-2'),
        btnTryAgain = document.getElementById('btn-try-again');

//Массив вопросов и вариантов ответа
    const questions = [
      {
        question: 'Кто является основателям Audi?',
        options: [
          'Леброн Джеймс',
          'Густав Отто',
          'Август Хорьх',
          'Карл Бенц',
        ],
        rightAnswer: 2
      },
      {
        question: 'Как слово Audi переводится с латинского языка?',
        options: [
          'Смотри',
          'Знай',
          'Слушай',
          'Доминируй',
        ],
        rightAnswer: 2
      },
      {
        question: 'В каких сегментах представлены автомобили марки Audi?',
        options: [
          'Представительские автомобили',
          'Спортивные и гоночные автомобили',
          'Автомобили бизнес-класса',
          'Все перечисленные',
        ],
        rightAnswer: 3
      },
      {
        question: 'В каком году Автомобильный завод Audi выпустил свой первый автомобиль?',
        options: [
          'В 1910 году',
          'В 1890 году',
          'В 1932 году',
          'В 1930 году',
        ],
        rightAnswer: 0
      },
      {
        question: 'Какая марка автомобиля лучше?',
        options: [
          'BMW',
          'Audi',
          'Mercedes-Benz',
          'Vaz',
        ],
        rightAnswer: 1
      }

    ];

    numberOfAllQuestions.innerHTML = questions.length; // Выводим количество вопросов

// Функция подставляет в indexOfQuestion значение из массива qestions
// и заполняет строки вопроса и вариантов ответа
    const load = () => {
      question.innerHTML = questions[indexOfQuestion].question;// Сам вопрос

      option1.innerHTML = questions[indexOfQuestion].options[0];
      option2.innerHTML = questions[indexOfQuestion].options[1];
      option3.innerHTML = questions[indexOfQuestion].options[2];
      option4.innerHTML = questions[indexOfQuestion].options[3];

      numberOfQuestion.innerHTML = indexOfPage + 1;// Установка номера текущей страницы
      indexOfPage++;// Увеличение индекса
    }

    const completedAnswers = [];// Массив для уже заданых вопросов

//Функция геренирует случайное число для случайного вопроса
    const randomQuestion = () => {
      let randomNumber = Math.floor(Math.random() * questions.length);//Math.random генерирует - рандомное число, Math.floor - делает число целым
      let hitDuplicate = false; // Якорь для проверки одинаковых вопросов

      if (indexOfPage == questions.length) {
        quizOver() //если количество indexOfPage(страниц) равно questions.length(колличеству вопросов) функция выдает конец игры
      } else {
        if(completedAnswers.length > 0) {
          completedAnswers.forEach(item => {
            if(item == randomNumber){
              hitDuplicate = true;
            }//Функция перебирает завершенные ответы и не дает им повторяться
          });
          if(hitDuplicate){
            randomQuestion();//Если число уже было функция запускается снова и генерирует другое число
          }else {
            indexOfQuestion = randomNumber;
            load(); //Если номер вопроса равен индексу и не повторялся функция load подставляет значения массива
          }
        }
        if(completedAnswers.length == 0) {
          indexOfQuestion = randomNumber;
          load();//Если еще не был дан ни один ответ функция load подставляет значения массива
        }
      }
      completedAnswers.push(indexOfQuestion);// push - Заполнение массива
    }

//Функция добавляет класс к правильному или не правильному ответу
    const checkAnswer = el => {
      if(el.target.dataset.id == questions[indexOfQuestion].rightAnswer){
        el.target.classList.add('correct');
        updateAnswerTracker('correct');
        score++;
      } else {
        el.target.classList.add('wrong');
        updateAnswerTracker('wrong');
      }
      disabledOptions();
    }

//просматривает событие клика на варианты ответов
    for(let option of optionElements){
      option.addEventListener('click', e => checkAnswer(e));
    }

// Функция блокирует нажатие кнопки после первого нажатия и подсвечивает правильный ответ
    const disabledOptions = () => {
      optionElements.forEach(item =>{
        item.classList.add('disabled');
        if(item.dataset.id == questions[indexOfQuestion].rightAnswer){
          item.classList.add('correct');
        }
      })
    }

//Функция удаляет все классы для новой страницы
    const enableQptions = () => {
      optionElements.forEach(item =>{
        item.classList.remove('disabled','correct','wrong');
      })
    }

//Функция создания трекеров (нижних кружков)
    const answerTracker = () => {
      questions.forEach(() =>{
        //document.createElement('div') - создает в нутри документа елемент
        const div = document.createElement('div');
        //Добавляем созданный элемент в div как дочерний
        answersTracker.appendChild(div);
      })
    }

//Функция добавления функционала цвета к трекерам
    const updateAnswerTracker = status => {
      answersTracker.children[indexOfPage - 1].classList.add(`${status}`);// Обращаемся ко всем дочерним элементам и добовляем им класс который получили из ответа
    }

//Функция которая не дает пройти дальше если ответ не выбран
    const validate = () => {
      if(!optionElements[0].classList.contains('disabled')){
        alert('Введите вариант ответа');
      } else {
        randomQuestion();
        enableQptions();
      }
    }

//Функция выполняется когда количество ответов совпало с количеством вопросов
    const quizOver = () => {
      document.querySelector('.quiz-over-modal').classList.add('active');//добавляем класс к модальному окну
      correctAnswer.innerHTML = score; //innerHTML свойство что б положить во внутрь какое-то значение, score - правильные ответы
      numberOfAllQuestions2.innerHTML = questions.length;// вставляем количесто вопросов через questions.length
    }

// Функция которая возвращает нас на начало опросника
    const tryAgain = () => {
      window.location.reload();// Перезагружает страницу HTML
    }

//Добавляем событие при нажатии на кнопку
    btnTryAgain.addEventListener('click', () => {
      tryAgain();
    })

//Добовляет событие что при нажатии на кнопку будет работать функция переходящая к другому вопросу
    btnNext.addEventListener('click', () => {
      validate();
    })

//Значение которое позволяет в начале загрузить всю информацию и потом начать функцию
    window.addEventListener('load', () => {
      randomQuestion();
      answerTracker();
    })
  }
}
</script>

<style scoped>
body {
  margin: 0;
  height: 1500px;
  background: linear-gradient(194deg, rgba(37,121,180,1) 0%, rgba(0,255,252,1) 100%);
  font-family: sans-serif;
}

* {
  box-sizing: border-box;
}

h2{
  text-align: center;
  font-family: 'Akaya Telivigala', cursive;
  font-size: 30px;
  margin: 5px 0;
}

.quiz-container {
  max-width: 700px;
  min-height: 497px;
  background-color: #ffffff;
  margin: 30px auto;
  border-radius: 10px;
  padding: 25px;
}

.question-number h3 {
  color: darkcyan;
  border-bottom: 1px solid #ccc;
  margin: 0;
  padding-bottom:  10px;
  text-align: right;
}

#question {
  text-align: center;
  font-size: 24px;
  color: #000000;
  padding: 15px 0;
  margin-bottom: 10px;
}

.options {
  margin-bottom: 15px;
}

.options div {
  background: linear-gradient(273deg, rgba(161,161,161,1) 0%, rgba(255,255,255,1) 100%);
  font-size: 16px;
  color: #000000;
  margin-bottom: 10px;
  border-radius: 50px;
  padding: 15px;
  cursor: pointer;
  transition: all .2s ease-in-out;
}

.options div:hover {
  background-color: #ccccccaf;
}

.options div.correct {
  background: linear-gradient(273deg, rgba(100,217,81,1) 0%, rgba(255,255,255,1) 100%);
  color: black;
}

.options div.wrong {
  background: linear-gradient(273deg, rgba(251,34,34,1) 0%, rgba(255,255,255,1) 100%);
  color: black;
}

.options div.disabled {
  pointer-events: none;
}

.button #btn-next {
  padding: 10px 50px;
  background-color: darkcyan;
  font-size: 18px;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all .2s ease-in-out;
  margin-bottom: 15px;
}

.button #btn-next:hover {
  background-color: #009687b6;
}

#answers-tracker {
  border-top: 1px solid #cccccc;
  padding-top: 1px;
}

#answers-tracker div{
  height:  20px;
  width: 20px;
  background-color: #cccccc;
  display: inline-block;
  border-radius: 50%;
  margin-right: 10px;
}

#answers-tracker div.correct {
  background-color: #64d951;
}

#answers-tracker div.wrong {
  background-color: #fb2222;
}

.quiz-over-modal {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9);
  z-index: 10;
  display: none;
  align-items: center;
  justify-content: center;
}

.quiz-over-modal.active {
  display: flex;
}

.quiz-over-modal .content {
  background: linear-gradient(194deg, rgba(37,121,180,1) 0%, rgba(0,255,252,1) 100%);
  padding: 30px;
  border-radius: 10px;
  flex-basis: 700px;
  max-width: 700px;
  color: #ffffff;
  text-align: center;
}

.quiz-over-modal .content h1 {
  font-size: 36px;
  margin: 0 0 20px;
}

.quiz-over-modal .content button {
  padding: 15px 50px;
  border: none;
  background-color: #ff9800;
  transition: all .2s ease-in-out;
  border-radius: 50px;
  cursor: pointer;
  font-size: 20px;
  color: #ffffff;
}

.quiz-over-modal .content button:hover {
  background-color: #ff9900b4;
}
</style>