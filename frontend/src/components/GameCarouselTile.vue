<template>
  <div class="tile-container">
    <div class="img-container">
      <Transition name="game-image">
        <img :src="this.getCurrentPicture" alt="" :key="this.currentImgIdx"/>
      </Transition>
    </div>
    <div class="content-container">
      <h1>{{ this.title }}</h1>
      <div class="genre-container">
        <p class="button1">MMO</p>
      </div>
      <p class="body2">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
        velit esse cillum dolore eu fugiat nulla pariatur.
      </p>
      <div class="image-carousel-container">
        <div
          v-for="(url, index) in this.images"
          :key="(url.index, index.index)"
        >
          <img :src="url" alt="" @click="this.currentImgIdx = index" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { delay } from "../global";
export default {
  name: "GameCarouselTile",

  computed: {
    getCurrentPicture() {
      console.log(this.currentImgIdx);
      console.log(this.images[this.currentImgIdx]);
      return this.images[this.currentImgIdx];
    },
  },

  data() {
    return {
      currentImgIdx: 0,
    };
  },

  method: {
    async cycleThroughImages(index) {
      let len = this.images.length();
      this.currentImgIdx = index;
      if (index >= len - 1) {
        this.currentImgIdx = 0;
      }

      return this.currentImgIdx;
    },
  },

  props: {
    title: {
      type: String,
      default: "Dark Souls: Remastered",
    },
    category: {
      type: String,
      default: "RPG",
    },
    description: {
      type: String,
      default: "N/A",
    },
    images: {
      type: Array,
      default: () => [
        "https://cdn.akamai.steamstatic.com/steam/apps/570940/capsule_616x353.jpg?t=1668145065",
        "https://fs-prod-cdn.nintendo-europe.com/media/images/08_content_images/games_6/nintendo_switch_7/nswitch_darksouls/CI_NSwitch_DarkSoulsRemastered_phantom04.jpg",
        "https://live.mrf.io/statics/i/ps/www.muycomputer.com/wp-content/uploads/2018/01/Dark-Souls-Remastered.jpg?width=1200&enable=upscale",
        "https://win.gg/wp-content/uploads/2021/08/streamer-flawlessly-beats-dark-souls-boss-blindfolded-on-a-piano.jpg",
      ],
    },
  },
};
</script>

<style scoped>
.tile-container {
  display: flex;
  width: 1016px;
  height: 280px;
  border-radius: 24px;
  background-color: var(--neutral-tile-color);
  overflow: hidden;
  border-radius: 24px;
}

.img-container {
  flex: 0.9;
  width: 100%;
  height: 100%;
  transition: var(--tile-transition-time);
  /* animation: anim 200ms; */
}

@keyframes anim{
  from{
    opacity: 0;
  }
  to{
    opacity: 1;
  }
}

.image-carousel-container {
  display: flex;
  gap: 4px;
}

.image-carousel-container img:hover {
  cursor: pointer;
  width: 124px;
  height: 100px;
  transition: var(--tile-transition-time);
}

.image-carousel-container img {
  cursor: pointer;
  object-fit: cover;
  width: 120px;
  height: 96px;
  transition: var(--tile-transition-time);
  border-radius: 8px;
}

.genre-container {
  padding: 8px;
}

img {
  object-fit: cover;
  width: 100%;
  height: 100%;
}

.content-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  padding: 16px 16px;
  gap: 8px;
}

.content-container p.button1 {
  margin: 0px;
}

.content-container h1 {
  margin: 0px;
}
</style>
