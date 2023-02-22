<template>
  <div class="tile-container">
    <div class="image-container">
      <img :src="img" alt="" />
    </div>
    <div class="content-container"></div>
  </div>
</template>

<script>
export default {
  props: {
    name: {
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
      default: "MMORPG",
    },
    platform: {
      type: String,
      default: "pc",
    },
    price: {
      type: String,
      default: "Free",
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

<style>
:root {
  --tile-rad-12: 12px;
}

.tile-container {
  display: flex;
  flex-direction: column;
  border-radius: var(--tile-rad-12);
  width: 142px;
  height: 172px;
  background-color: pink;
}

.image-container {
  flex: 1.25;
  width: 100%;
  height: 100%;
  border-top-left-radius: var(--tile-rad-12);
  border-top-right-radius: var(--tile-rad-12);
  background-color: white;
}

.image-container > img{
  flex: 1.25;
  height: 100%;
  width: 100%;
  object-fit: cover;
  /* border-top-left-radius: cal(var(--tile-rad-12)); */
  /* border-top-right-radius: var(--tile-rad-12); */
  background-color: white;
}

.content-container {
  flex: 1;
  width: 100%;
  border-bottom-left-radius: var(--tile-rad-12);
  border-bottom-right-radius: var(--tile-rad-12);
  background-color: blue;
}
</style>
