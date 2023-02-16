<template>
  <div v-if="shouldShowSidebar">
    <AppHeader />
    <div class="app">
      <AppSidebar />
      <router-view class="router-style" />
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

  computed: {
    shouldShowSidebar() {
      return this.$route.meta.sidebar !== false;
    },
  },
};
</script>

<style></style>
