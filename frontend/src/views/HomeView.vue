<template>
  <div class="container">
    <GameCarouselSlider/>
    <h3>Free</h3>
    <div class="horizontal-games-container">
      <div v-for="game in get_free_games" :key="game.index">
        <GameTile
          :title="game.title"
          :description="game.description"
          :genre="game.genre"
          :platform="game.platform"
          :price="game.price.toUpperCase()"
          :img="game.img"
          :link="game.link"
        />
      </div>
    </div>

    <div class="heightbox-container" style="height:16px"></div>
    <h3>On Sale</h3>
    <div class="horizontal-games-container">
      <div v-for="game in get_sale_games" :key="game.index">
        <GameTile
          :title="game.title"
          :description="game.description"
          :genre="game.genre"
          :platform="game.platform"
          :price="game.price.toUpperCase()"
          :img="game.img"
          :link="game.link"
        />
      </div>
    </div>
    <div class="heightbox-container"></div>
  </div>
</template>

<script>
import axios from "axios";
import GameTile from "../components/GameTile.vue";
import { APIEndpoints } from "../global";
import GameCarouselSlider from '../components/GameCarouselSlider.vue';

export default {
  name: "HomeView",
  components: {
    GameTile,
    GameCarouselSlider,
  },

  computed: {
    get_free_games() {
      return this.free_games;
    },
    get_sale_games() {
      return this.sale_games;
    },
  },

  data: () => {
    return {
      free_games: [],
      sale_games: [],
    };
  },

  methods: {
    async getData() {
      let result  = null
      await axios
        .get(this.baseUrl + APIEndpoints.get_games)
        .then((res) => {
          console.log(res);
          result = res
          this.free_games = res.data.free_games;
          this.sale_games = res.data.sale_games;
        })
        .catch(() => {});
      if (result.status == 200) {
        console.log(result.data);
        this.free_games = result.data.free_games;
      }
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style scoped>
.horizontal-games-container {
  display: flex;
  gap: 16px;
  padding: 8px;
  overscroll-behavior-inline: contain;
  overflow-x: hidden;
}

.horizontal-games-container:hover {
  overflow-x: auto;
}

.heightbox-container {
  height: 50px;
  width: 0px;
}

.container {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 8px;
}

.textfield-parent {
  display: flex;
  flex-direction: column;
  width: 360px;
  gap: 8px;
}
</style>
