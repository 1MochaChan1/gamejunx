<template>
  <div @click="this.doNavigate()" class="logo">
    <img src="../assets/svg/app_bar_logo.svg" alt="" />
    <h4>Gamejunx</h4>
  </div>
</template>

<script>
export default {
  name: "AppLogo",
  methods: {
    doNavigate() {
      this.$router.push("home");
    },
  },
};
</script>

<style>
.logo {
  cursor: pointer;
  display: inline-flex;
  justify-content: center;
  align-content: center;
  gap: 4px;
  color: var(--primary-color);
}

.logo img {
  margin-bottom: 0px;
}
</style>
