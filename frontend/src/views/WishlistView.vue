<template>
  <div class="container">
    <h2>Wishlist</h2>
    <div class="games-grid-container">
      <div
        style="margin-bottom: 8px"
        v-for="game in this.wishlistedGames"
        :key="game.index"
      >
        <GameTile
          :title="game.title"
          :description="game.description"
          :genre="game.genre"
          :platform="game.platform"
          :price="game.price.toUpperCase()"
          :img="game.img"
          :link="game.link"
          :isWishlisted="game.wishlisted"
          @wishlist-icon-clicked="this.addOrRemoveFromWishlist(game)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import GameTile from "../components/GameTile.vue";
import { APIEndpoints } from "../global";

export default {
  name: "WishlistView",
  components: { GameTile },
  data() {
    return {
      wishlistedGames: [],
    };
  },
  created() {
    axios
      .get(this.baseUrl + APIEndpoints.wishlist, {
        params: {
          user_id: localStorage.id,
        },
      })
      .then((res) => {
        this.wishlistedGames = res.data.games;
      })
      .catch(() => {});
  },
  methods: {
    addOrRemoveFromWishlist(gameToAddOrRemove) {
      axios
        .put(this.baseUrl + APIEndpoints.wishlist, {
          user_id: localStorage.id,
          game: gameToAddOrRemove,
        })
        .then(() => {})
        .catch(() => {});
    },
  },
};
</script>

<style>
.games-grid-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  flex-direction: row;
}
</style>
