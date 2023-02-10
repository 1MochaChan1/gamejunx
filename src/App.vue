<template>
  <div v-if="!isAuthScreen" @isNotAuthScreen="toggle(false)">
    <AppHeader />
    <div class="app">
      <AppSidebar />
      <router-view class="router-style" />
    </div>
  </div>
  <div v-else-if="isAuthScreen" @isAuthScreen="toggle(true)">
    <router-view class="router-style" />
  </div>
</template>

<script>
import AppHeader from "./components/AppHeader.vue";
import AppSidebar from "./components/AppSidebar.vue";

export default {
  name: "App",
  data:() => (
    {
      isAuthScreen: false,
    }),
  components: {
    AppHeader,
    AppSidebar,
  },
  method:{
    toggle(value){
      this.isAuthScreen=value;
    }
  },
  mounted: function () {
    
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

.router-style {
  margin: 0px;
}
</style>
