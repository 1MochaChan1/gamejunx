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
    <!-- <div class="heightbox-container"></div> -->
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
  </div>
</template>

<script>
// import axios from "axios";
import GameTile from "../components/GameTile.vue";
// import { APIEndpoints } from "../global";
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
      free_games: [
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
      ],
      sale_games: [
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
        {
          description:
            "A hero-focused first-person team shooter from Blizzard Entertainment.",
          genre: "Shooter",
          id: null,
          img: "https://www.freetogame.com/g/540/thumbnail.jpg",
          link: "https://www.freetogame.com/overwatch-2",
          platform: "pc",
          price: "free",
          tags: null,
          title: "Overwatch 2",
        },
      ],
    };
  },

  methods: {
    async getData() {
      // await axios
      //   .get(this.baseUrl + APIEndpoints.get_games)
      //   .then((res) => {
      //     console.log(res);
      //     this.free_games = res.data.free_games;
      //     this.sale_games = res.data.sale_games;
      //   })
      //   .catch(() => {});
      // if (res.status == 200) {
      //   console.log(res.data);
      //   this.free_games = res.data.free_games;
      // }
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style scoped>
.horizontal-games-container {
  height: 230px;
  /* display: grid; */
  display: flex;
  /* grid-auto-flow: column; */
  gap: 16px;
  padding: 8px;
  overscroll-behavior-inline: contain;
  overflow-x: hidden;
}

.horizontal-games-container:hover {
  overflow-x: auto;
}

.heightbox-container {
  height: 8px;
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
