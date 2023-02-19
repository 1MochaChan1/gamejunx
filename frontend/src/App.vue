<template>
  <AuthWrapper />
</template>

<script>
// import AppHeader from "./components/AppHeader.vue";
// import AppSidebar from "./components/AppSidebar.vue";
import AuthWrapper from "./components/AuthWrapper.vue";

export default {
  name: "App",
  data: () => ({}),
  components: {
    AuthWrapper,
  },
};
</script>

<style>
.app {
  display: flex;
  /* position: fixed; */
  gap: 24px;
  padding: 0px 16px;
}
</style>
