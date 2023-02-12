<template>
  <div v-if="!isAuthScreen">
    <AppHeader />
    <div class="app">
      <AppSidebar />
      <router-view class="router-style" />
    </div>
  </div>
  <div v-else-if="isAuthScreen">
    <router-view class="router-style" />
  </div>
</template>

<script>
import { authfields } from "../global.js";
import AppHeader from "../components/AppHeader.vue";
import AppSidebar from "../components/AppSidebar.vue";

export default {
  name: "AuthWrapper",
  components: {
    AppHeader,
    AppSidebar,
  },
  data: () => ({
    isAuthScreen: false,
  }),

  methods: {
    _navigate(route) {
      return new Promise(() => {
        this.$router.push({ name: route });
      });
    },
  },


  mounted(){
    this._navigate('login');
  },

  watch: {
    $route() {
      let curRoute = this.$router.currentRoute.value.name;
      if (authfields.indexOf(curRoute) != -1) {
        this.isAuthScreen = true;
      } else {
        this.isAuthScreen = false;
      }
    },
  },
};
</script>

<style></style>
