<template>
  <div class="component-container">
    <div class="carousel-container">
      <img src="../assets/svg/app_left_arrow.svg" alt="" @click="this.prev()" />

      <div
        v-for="(game, index) in games"
        :key="(game, index)"
        class="game-tile-container"
      >
        <!-- TODO: add transition -->
        <GameCarouselTile
          :key="index"
          v-show="this.getCurrentVisibleIndex === index"
          :link="game.link"
          :title="game.title"
          :images="game.images"
          :description="game.description"
          :category="game.category"
        />
      </div>

      <img
        src="../assets/svg/app_right_arrow.svg"
        alt=""
        @click="this.next()"
      />
    </div>
    <div class="slider-nav">
      <div
        :class="{
          'selected-anchor': this.visibleIndex === index,
          'unselected-anchor': this.visibleIndex !== index,
        }"
        v-for="(game, index) in games"
        :key="(game, index)"
        @click="this.visibleIndex = index"
      ></div>
    </div>
  </div>
</template>

<script>
import GameCarouselTile from "./GameCarouselTile.vue";
export default {
  name: "GameCarouselSlider",
  components: { GameCarouselTile },
  computed: {
    getCurrentVisibleIndex() {
      return this.visibleIndex;
    },
  },
  data() {
    return {
      visibleIndex: 0,
    };
  },
  props: {
    games: {
      type: Array,
      default: () => [
        {
          title: "Dark Souls: Remastered",
          category: "RPG",
          description:
            "Dark Souls Remastered is a remastered version of the first game in FromSoftware's Dark Souls series, it also marks the first appearance of any games from the series on a Nintendo platform. The remastered version also comes with the DLC, 'Arotias of the Abyss', in the base game.",
          images: [
            "https://cdn.akamai.steamstatic.com/steam/apps/570940/capsule_616x353.jpg?t=1668145065",
            "https://fs-prod-cdn.nintendo-europe.com/media/images/08_content_images/games_6/nintendo_switch_7/nswitch_darksouls/CI_NSwitch_DarkSoulsRemastered_phantom04.jpg",
            "https://live.mrf.io/statics/i/ps/www.muycomputer.com/wp-content/uploads/2018/01/Dark-Souls-Remastered.jpg?width=1200&enable=upscale",
            "https://win.gg/wp-content/uploads/2021/08/streamer-flawlessly-beats-dark-souls-boss-blindfolded-on-a-piano.jpg",
          ],
          link: "https://store.steampowered.com/app/570940/DARK_SOULS_REMASTERED/",
        },
        {
          title: "Dark Souls: Remastered",
          category: "RPG",
          description:
            "Dark Souls Remastered is a remastered version of the first game in FromSoftware's Dark Souls series, it also marks the first appearance of any games from the series on a Nintendo platform. The remastered version also comes with the DLC, 'Arotias of the Abyss', in the base game.",
          images: [
            "https://cdn.akamai.steamstatic.com/steam/apps/570940/capsule_616x353.jpg?t=1668145065",
            "https://fs-prod-cdn.nintendo-europe.com/media/images/08_content_images/games_6/nintendo_switch_7/nswitch_darksouls/CI_NSwitch_DarkSoulsRemastered_phantom04.jpg",
            "https://live.mrf.io/statics/i/ps/www.muycomputer.com/wp-content/uploads/2018/01/Dark-Souls-Remastered.jpg?width=1200&enable=upscale",
            "https://win.gg/wp-content/uploads/2021/08/streamer-flawlessly-beats-dark-souls-boss-blindfolded-on-a-piano.jpg",
          ],
          link: "https://store.steampowered.com/app/570940/DARK_SOULS_REMASTERED/",
        },
        {
          title: "Dark Souls: Remastered",
          category: "RPG",
          description:
            "Dark Souls Remastered is a remastered version of the first game in FromSoftware's Dark Souls series, it also marks the first appearance of any games from the series on a Nintendo platform. The remastered version also comes with the DLC, 'Arotias of the Abyss', in the base game.",
          images: [
            "https://cdn.akamai.steamstatic.com/steam/apps/570940/capsule_616x353.jpg?t=1668145065",
            "https://fs-prod-cdn.nintendo-europe.com/media/images/08_content_images/games_6/nintendo_switch_7/nswitch_darksouls/CI_NSwitch_DarkSoulsRemastered_phantom04.jpg",
            "https://live.mrf.io/statics/i/ps/www.muycomputer.com/wp-content/uploads/2018/01/Dark-Souls-Remastered.jpg?width=1200&enable=upscale",
            "https://win.gg/wp-content/uploads/2021/08/streamer-flawlessly-beats-dark-souls-boss-blindfolded-on-a-piano.jpg",
          ],
        },
      ],
    },
  },

  methods: {
    next() {
      if (!(this.visibleIndex >= this.games.length - 1)) {
        console.log("incremented");
        this.visibleIndex++;
      } else {
        this.visibleIndex = 0;
      }
    },

    prev() {
      if (!(this.visibleIndex <= 0)) {
        this.visibleIndex--;
      } else {
        this.visibleIndex = this.games.length - 1;
      }
    },
  },
};
</script>

<style scoped>
.component-container {
  display: flex;
  flex-direction: column;
}

.carousel-container {
  position: relative;
  display: flex;
  width: 100%;
  /* overflow: hidden; */
  align-items: center;
  justify-content: center;
}
img {
  flex: 1;
  height: 80px;
  cursor: pointer;
  /* width: 40px; */
}

.slider-nav {
  display: flex;
  flex-direction: row;
  height: 20px;
  width: 100%;
  column-gap: 1rem;
  left: 50%;
  top: 50%;
  align-items: center;
  justify-content: center;
}

.unselected-anchor {
  height: 8px;
  width: 8px;
  border-radius: 20px;
  background-color: var(--neutral-indicator-color);
  transition: 200ms;
}
.selected-anchor {
  height: 10px;
  width: 10px;
  border-radius: 20px;
  background-color: var(--primary-color);
  transition: 200ms;
}
</style>
