<template>
  <div v-if="shouldShowSidebar">
    <AppHeader />
    <div class="app">
      <AppSidebar />
      <div class="router-container-with-sidebar">
        <router-view class="router-style" />
      </div>
    </div>
  </div>
  <div v-else-if="!shouldShowSidebar">
    <router-view class="router-style" />
  </div>
</template>

<script>
import AppHeader from "../components/AppHeader.vue";
import AppSidebar from "../components/AppSidebar.vue";

export default {
  name: "AuthWrapper",
  components: {
    AppHeader,
    AppSidebar,
  },
  data: () => ({}),



  created() {
    if (localStorage.getItem("token") != null) {
      this.$router.push("home");
    }
  },

  computed: {
    shouldShowSidebar() {
      return this.$route.meta.sidebar !== false;
    },
  },
};
</script>

<style>
.router-container-with-sidebar {
  margin-left: 140px;
  margin-top: 80px;
  width: 100%;
  height: 650px;
  overflow-y: scroll;
}
.router-container {
  margin-top: 80px;
  width: 100%;
}
</style>
