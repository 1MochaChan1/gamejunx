<template>
  <AppHeader/>
  <AppToggleSwitch />
  <!-- <img alt="Vue logo" src="./assets/images/logo.png"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  
</template>

<script>
import AppToggleSwitch from './components/AppToggleSwitch.vue'
import AppHeader from './components/AppHeader.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppToggleSwitch,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center;
  color: #2c3e50;
  margin-top: 0px !important;
  padding: 8px; */
} 
</style>
