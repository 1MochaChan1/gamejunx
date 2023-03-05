<template>
  <div class="tile-container">
    <div class="img-container">
      <!-- <img
        src="https://fs-prod-cdn.nintendo-europe.com/media/images/08_content_images/games_6/nintendo_switch_7/nswitch_darksouls/CI_NSwitch_DarkSoulsRemastered_phantom04.jpg"
        alt=""
      /> -->
    </div>
    <div class="content-container">
      <h1>{{ this.title }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "GameCarouselTile",
  props: {
    title: {
      type: String,
      default: "N/A",
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
        "https://fs-prod-cdn.nintendo-europe.com/media/images/08_content_images/games_6/nintendo_switch_7/nswitch_darksouls/CI_NSwitch_DarkSoulsRemastered_phantom04.jpg",
        "https://cdn.akamai.steamstatic.com/steam/apps/570940/capsule_616x353.jpg?t=1668145065",
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
}

.img-container {
  background-color: blue;
  width: 100%;
  height: 100%;
}

/* .img-container img{

} */

.content-container {
  background-color: pink;
  width: 100%;
  height: 100%;
}
</style>
