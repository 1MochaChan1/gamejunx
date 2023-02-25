<template>
  <div class="container">
    <h3>Games</h3>
  </div>
</template>

<script>
// import AppTextFieldPassword from "../components/AppTextFieldPassword.vue";
// import AppTextFieldEdit from "../components/AppTextFieldEdit.vue";
// import AppTextField from "../components/AppTextField.vue";
// import GameTile from "../components/GameTile.vue";

export default {
  name: "HomeView",
  components: {
    // AppTextFieldPassword,
    // AppTextFieldEdit,
    // AppTextField,
    // GameTile,
  },

  methods: {
    edit() {
      console.log("Edit event called");
    },
  },
};
</script>

<style scoped>
.container {
  display: inline-block;
  width: 100vw;
}

.textfield-parent {
  display: flex;
  flex-direction: column;
  width: 360px;
  gap: 8px;
}
</style>
