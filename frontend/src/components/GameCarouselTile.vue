<template>
  <div class="tile-container" @click="this.openLink(this.link)">
    <div class="img-container">
      <Transition name="game-image" mode="in-out">
        <img :src="this.getCurrentPicture" alt="" :key="this.currentImgIdx" />
      </Transition>
    </div>
    <div class="content-container">
      <h1>{{ this.title }}</h1>
      <div class="genre-container">
        <p class="button1">MMO</p>
      </div>
      <p class="body2">
        {{ this.description }}
      </p>
      <div class="spacer"></div>
      <div class="image-row-container">
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
      return this.images[this.currentImgIdx];
    },
  },

  data() {
    return {
      currentImgIdx: 0,
    };
  },

  methods: {
    async cycleThroughImages(index) {
      let len = this.images.length();
      this.currentImgIdx = index;
      if (index >= len - 1) {
        this.currentImgIdx = 0;
      }

      return this.currentImgIdx;
    },
    openLink(urlStr) {
      window.open(urlStr);
    },
  },

  props: {
    link: {
      type: String,
      default: "",
    },
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
      default: () => [],
    },
  },
};
</script>

<style scoped>
.tile-container {
  cursor: pointer;
  display: flex;
  width: 1016px;
  height: 280px;
  border-radius: 24px;
  background-color: var(--neutral-tile-color);
  overflow: hidden;
  border-radius: 24px;
  scroll-snap-align: start;
}

.img-container {
  flex: 0.9;
  width: 100%;
  height: 100%;
  transition: var(--tile-transition-time);
  /* animation: anim 200ms; */
}

.img-container img {
  object-fit: cover;
}

@keyframes anim {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.image-row-container {
  display: flex;
  gap: 4px;
}

.image-row-container img:hover {
  cursor: pointer;
  width: 120px;
  height: 90px;
  transition: var(--tile-transition-time);
}

.image-row-container img {
  cursor: pointer;
  object-fit: cover;
  width: 116px;
  height: 90px;
  transition: var(--tile-transition-time);
  border-radius: 8px;
  margin-bottom: 24px;
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
  justify-content: space-between;
  gap: 8px;
}

.content-container p.button1 {
  margin: 0px;
}

.content-container h1 {
  margin: 0px;
}
</style>
