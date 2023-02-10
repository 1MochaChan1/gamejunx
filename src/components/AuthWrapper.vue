<template>
  <div>chup kar be kutte</div>
</template>

<script>
import { authfields } from "../global.js";
export default {
  name: "AuthWrapper",
  mounted: function () {
    let curRoute = console.log(this.$router.currentRoute.value.name);
    if (authfields.indexOf(curRoute) != -1) {
      this.$emit("isAuthScreen");
    } else {
      this.$emit("isNotAuthScreen");
    }
    // console.log("Message from wrapper class");
    // this.$router.push({ name: "login" });
  },
};
</script>

<style>
</style>