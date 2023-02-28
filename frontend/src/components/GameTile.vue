<template>
  <div
    class="tile-container"
    style="cssProps"
    @click="openUrl(this.link)"
    @mouseenter="this.hover = true"
    @mouseleave="this.hover = false"
  >
    <div class="image-container">
      <div :class="{ 'image-holder-hover': hover, 'image-holder': !hover }">
        <img :src="this.img" alt="" />
        <p v-show="this.hover" class="subtitle1 title-container">
          {{ this.title }}
        </p>
      </div>
    </div>
    <div class="content-container">
      <p class="body2 price-tag-container">
        {{ this.price }}
      </p>
      <div v-show="!this.showSection">
        <p class="caption genre-container">
          {{ this.genre }}
        </p>
        <div class="platform-container" v-if="this.makePlatformList() != ''">
          <img
            :src="this.getImageUrl(this.makePlatformList())"
            alt="img"
          />
          <!-- <img :src="this.getImageUrl(this.makePlatformList())" :alt="item.alt" /> -->
          <!-- <div v-for="item in this.makePlatformList()" :key="item">
            <img :src="this.getImageUrl(item)" :alt="item.alt" />
          </div> -->
        </div>
      </div>
      <div v-show="this.showSection">
        <p class="body2">
          {{ this.description }}
        </p>
        <div class="platform-container">
          <!-- <img :src="this.getImageUrl()" :alt="item.alt" /> -->
          <!-- <div v-for="item in this.makePlatformList()" :key="item">
            <img :src="this.getImageUrl(item)" :alt="item.alt" />
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

  data() {
    return {
      hover: false,
      imgFromData: "https://www.freetogame.com/g/77/thumbnail.jpg",
    };
  },

  computed: {
    showSection() {
      return this.hover;
    },
    cssProps() {
      return {
        "--background-img": `url(${this.imgFromData})`,
        "--some-col": "#FFFFFF",
        "--is-hovering": this.hover,
      };
    },
  },

  methods: {
    getImageUrl(str) {
      return require("../assets/svg/" + str);
    },
    openUrl(urlStr) {
      window.open(urlStr);
    },
    makePlatformList() {
      switch (this.platform) {
        case "pc":
          return "windows-line.svg";
        // arr.push("windows-line.svg");
        // break;

        case "xbox":
          return "xbox-line.svg";
        // arr.push("xbox-line.svg");
        // break;

        case "ps":
          return "playstation-line.svg";
        // arr.push("playstation-line.svg");
        // break;

        case "switch":
          return "switch-line.svg";
        // arr.push("switch-line.svg");
        // break;

        case "browser":
          return "globe-line.svg";

        default:
          return "";
        // arr.push("windows-line.svg");
        // break;
      }
    },
  },
  props: {
    title: {
      type: String,
      default: "Revelation Online",
    },
    description: {
      type: String,
      default:
        "A free-to-play fantasy MMO developed by NetEase and published by My.com. ",
    },
    tags: {
      type: String,
    },
    genre: {
      type: String,
      default: "-",
    },
    platform: {
      type: String,
      default: "pc",
    },
    price: {
      type: String,
      default: "₹ 1399.00",
    },
    img: {
      type: String,
      default: "https://www.freetogame.com/g/77/thumbnail.jpg",
    },
    link: {
      type: String,
      default: "https://www.freetogame.com/open/revelation-online",
    },
  },
};
</script>

<style scoped>
.tile-container {
  cursor: pointer;
  display: flex;
  flex-direction: column;
  border-radius: var(--tile-rad-12); /* --tile-rad-12: 12px*/
  overflow: hidden;
  width: var(--tile-width);
  height: var(--tile-height);
  background-color: var(--neutral-tile-color);
  box-shadow: var(--shadow-tile);
  transition: var(--tile-transition-time);
}

.title-container {
  position: absolute;
  bottom: 0px;
  left: 2px;
  /*  ---- overflow ---- */
  display: inline-block;
  width: calc(var(--tile-width) - 4px);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* ---- x ---- */
  z-index: 1;
  transition: var(--tile-transition-time);
}

.tile-container:hover {
  transition: var(--tile-transition-time);
  height: var(--tile-height-hover);
}

/* Without Hover */
.image-container {
  width: 100%;
  height: 50%;
}

.image-holder {
  height: 100%;
  width: 100%;
  position: relative;
}

.image-holder img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}

/*  With Hover   */
.image-holder-hover {
  display: inline-block;
  position: relative;
  height: 100%;
  width: 100%;
}
.image-holder-hover img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}

.image-holder-hover::after {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  height: 100%;
  width: 100%;
  background: rgb(0, 0, 0);
  background: linear-gradient(
    0deg,
    rgba(0, 0, 0, 1) 0%,
    rgba(255, 255, 255, 0) 100%
  );
}

.content-container {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 8px 4px;
  width: 100%;
  border-bottom-left-radius: var(--tile-rad-12);
  border-bottom-right-radius: var(--tile-rad-12);
}
.price-tag-container {
  background-color: var(--primary-color);
  border-radius: 2px;
  padding: 0px 4px;
  height: fit-content;
  width: fit-content;
  flex-basis: min-content;
}

.genre-container {
  background-color: var(--neutral-dark-color);
  border-radius: 24px;
  width: fit-content;
  padding: 2px 8px;
  flex-basis: min-content;
}

.platform-container {
  display: flex;
  width: 90%;
  height: 60%;
  gap: 4px;
  margin-left: 2px;
  padding-bottom: 4px;
  align-items: flex-end;
}

.platform-container img {
  height: 12px;
  width: 12px;
}
</style>
