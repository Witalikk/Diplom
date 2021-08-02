<template>
  <div class="swiper">
    <h2 class="mt-6 mb-4 text-left ml-16 text-4xl font-extrabold text-gray-900">
      Проложите путь по любому <br> маршруту
    </h2>
    <h3 class="mb-6 text-left ml-16 text-l text-gray-900">
      Будущее современной мобильности уже сегодня: испытайте интеллектуальные системы <br> помощи водителю и функции автономного вождения новой эры. Сделайте шаг навстречу <br> новому ощущению от вождения в век цифровых технологий.
    </h3>
  <div class="swiper-container">
  <el-carousel indicator-position="outside" :interval="30000" height="750px" class="mb-64">
    <el-carousel-item label="Все">
      <video preload="auto" autoplay="true" loop="true" muted="muted"  src="@/assets/media/video/all.mp4"  width="100%" controls></video>
    </el-carousel-item>
    <el-carousel-item label="Лазерный сканер">
      <img src="https://www.audi.by/content/dam/nemo/models/a8/a8-l/my-2018/1920x1080-feature-gallery/1920x1080_06_FeatureGalleryFullWidth_ai_Laserscanner.jpeg?output-format=webp&downsize=1920px:*"/>
    </el-carousel-item>
    <el-carousel-item label="Ультразвук">
      <img src="https://www.audi.by/content/dam/nemo/models/a8/a8-l/my-2018/1920x1080-feature-gallery/1920x1080_06_FeatureGalleryFullWidth_ai_Ultraschall.jpeg?output-format=webp&downsize=1920px:*"/>
    </el-carousel-item>
    <el-carousel-item label="Камера">
      <img src="https://www.audi.by/content/dam/nemo/models/a8/a8-l/my-2018/1920x1080-feature-gallery/1920x1080_06_FeatureGalleryFullWidth_ai_Kameras.jpeg?output-format=webp&downsize=1920px:*"/>
    </el-carousel-item>
    <el-carousel-item label="Радар">
      <img src="https://www.audi.by/content/dam/nemo/models/a8/a8-l/my-2018/1920x1080-feature-gallery/1920x1080_06_FeatureGalleryFullWidth_ai_Radar.jpeg?output-format=webp&downsize=1920px:*"/>
    </el-carousel-item>
<!--    <el-carousel-item label="Радар">-->
<!--      <img src="@/assets/media/scaner.jpeg"/>-->
<!--    </el-carousel-item>-->
  </el-carousel>
  </div>
  </div>
</template>

<script>
export default {
  name: 'swiper-radar',
  props: {
    swiperListRadar: Array
  },
}
</script>

<style>
.el-carousel__item h3 {
  color: #fcba03;
  font-size: 28px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}
.swiper {
  background-color:#dad7d2
}

/*.el-carousel__item:nth-child(2n) {*/
/*  background-color: #99a9bf;*/
/*}*/

/*.el-carousel__item:nth-child(2n+1) {*/
/*  background-color: #d3dce6;*/
/*}*/
</style>