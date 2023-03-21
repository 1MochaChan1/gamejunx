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
          title: "Elden Ring",
          category: "Souls-like",
          description:
            "Elden Ring is a 2022 action role-playing game developed by FromSoftware and published by Bandai Namco Entertainment. Directed by Hidetaka Miyazaki with worldbuilding provided by fantasy writer George R. R. Martin, it was released for PlayStation 4, PlayStation 5, Windows, Xbox One, and Xbox Series X/S on February 25.",
          images: [
            "https://i.ytimg.com/vi/JldMvQMO_5U/maxresdefault.jpg",
            "https://assets.reedpopcdn.com/elden-ring-bosses-in-order-main-mandatory-8042-1647011924713.jpg/BROK/resize/1200x1200%3E/format/jpg/quality/70/elden-ring-bosses-in-order-main-mandatory-8042-1647011924713.jpg",
            "https://www.videogameschronicle.com/files/2022/02/sds5.jpg",
            "https://cdn.thewirecutter.com/wp-content/media/2022/03/elden-ring-2048px-0003.jpg?auto=webp&quality=75&width=1024",
          ],
          link: "https://store.steampowered.com/agecheck/app/1245620/",
        },
        {
          title: "Demon's Souls",
          category: "Adventure",
          description:
            "Demon's Souls is a 2020 action role-playing game developed by Bluepoint Games and published by Sony Interactive Entertainment for the PlayStation 5. The game was released as a launch title for the PlayStation 5 in November.",
          images: [
            "https://prod.assets.earlygamecdn.com/images/demons-souls-ps5-review-im-test.jpg?x=0.5&y=0.5",
            "https://assets.reedpopcdn.com/demons-souls-review-a-cult-classic-reborn-as-a-cinematic-spectacle-1605525141206.jpg/BROK/thumbnail/1600x900/quality/100/demons-souls-review-a-cult-classic-reborn-as-a-cinematic-spectacle-1605525141206.jpg",
            "https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/DPDZEQZX5NFNTAYVIRZ4JSCCGY.jpg",
            "https://www.denofgeek.com/wp-content/uploads/2020/11/demons-souls-review.jpg?fit=3840%2C2160",
          ],
          link: "https://www.playstation.com/en-in/games/demons-souls/",
        },
      ],
    },
  },

  methods: {
    next() {
      if (!(this.visibleIndex >= this.games.length - 1)) {
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
