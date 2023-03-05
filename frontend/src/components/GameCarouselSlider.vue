<template>
  <div class="component-container">
    <div class="carousel-container">
      <!-- <img src="../assets/svg/app_left_arrow.svg" alt="" />
      <div class="slider-container">
        <div class="tile-container"><GameCarouselTile id="slide-1" /></div>
        <div class="tile-container"><GameCarouselTile id="slide-2" /></div>
        <div class="tile-container"><GameCarouselTile id="slide-3" /></div>
      </div>
      <img src="../assets/svg/app_right_arrow.svg" alt="" /> -->
    </div>
    <div class="slider-nav"></div>
  </div>
</template>

<script>
// import GameCarouselTile from "./GameCarouselTile.vue";
export default {
  name: "GameCarouselSlider",
  //   components: { GameCarouselTile },
};
</script>

<style scoped>
.component-container {
  display: flex;
  flex-direction: column;
  /* background-color: red; */
}

.carousel-container {
  /* display: flex; */
  height: 100px;
  background-color: pink;
  /* width: 100%; */
  align-items: center;
  justify-content: center;
}
img {
  flex: 1;
  height: 80px;
  cursor: pointer;
  /* width: 40px; */
}

.slider-container {
  display: flex;
  width: 1016px;
  overflow: auto;
  scroll-behavior: smooth;
  scroll-snap-type: x mandatory;
}
/* .slider-container:hover {
  display: flex;
  width: 1016px;
  overflow: auto;
  scroll-behavior: smooth;
  scroll-snap-type: x mandatory;
} */

.tile-container {
  width: 1016px;
}

.slider-nav {
  /* flex: row; */
  height: 50px;
  width: 100px;
  color: purple;
  /* z-index: 1; */
  /* position: absolute; */
  /* left: 50%;
  transform: translateX(-50%); */
}

.slider-nav a {
  height: 8px;
  width: 8px;
  border-radius: 20px;
  background-color: white;
}
</style>
