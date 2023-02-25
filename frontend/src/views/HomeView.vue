<template>
  <div class="container">
    <h3>Free</h3>
    <div class="horizontal-games-container">
      <GameTile />
      <GameTile />
      <GameTile />
      <GameTile />
      <GameTile />
      <GameTile />
      <GameTile />
      <GameTile />
      <GameTile />
      <GameTile />
      <GameTile />
      <GameTile />
      <GameTile />
    </div>
    <h3>On Sale</h3>
    <div class="horizontal-games-container">
      <GameTile />
    </div>
  </div>
</template>

<script>
// import AppTextFieldPassword from "../components/AppTextFieldPassword.vue";
// import AppTextFieldEdit from "../components/AppTextFieldEdit.vue";
// import AppTextField from "../components/AppTextField.vue";
import GameTile from "../components/GameTile.vue";

export default {
  name: "HomeView",
  components: {
    // AppTextFieldPassword,
    // AppTextFieldEdit,
    // AppTextField,
    GameTile,
  },

  methods: {
    edit() {
      console.log("Edit event called");
    },
  },
};
</script>

<style scoped>

.horizontal-games-container{
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 11%;
  padding: 8px;
  overscroll-behavior-inline: contain;
  overflow-x:auto;
  /* margin-top: 8px;
  margin-bottom: 24px;
  gap: 8px;
  overflow: auto;
  white-space: nowrap; */
}

.container {
  display: inline-block;
  width: 100%;
}

.textfield-parent {
  display: flex;
  flex-direction: column;
  width: 360px;
  gap: 8px;
}
</style>
