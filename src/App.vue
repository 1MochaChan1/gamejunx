<template>
  <AppHeader />
  
  <div class="app">
    <AppSidebar />
    <router-view class="router-style"/>
  </div>
</template>

<script>
import AppHeader from "./components/AppHeader.vue";
import AppSidebar from "./components/AppSidebar.vue";

export default {
  name: "App",
  components: {
    AppHeader,
    AppSidebar,
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

.router-style{
  margin: 0px;
}
</style>
