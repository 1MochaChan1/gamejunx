<template>
  <header class="app-header">
    <AppLogo/>
  </header>
</template>

<script>
import AppLogo from './AppLogo.vue';
export default {
  components: { AppLogo },
  name: "AppHeader",
};
</script>

<style>


.app-header {
  position: fixed;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0px 16px;
}
</style>
