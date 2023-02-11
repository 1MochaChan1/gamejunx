<template>
  <div>
    <button class="button" @click="onClick()">
      <p class="button2">Login</p>
    </button>
  </div>
</template>

<script>
export default {
  name: "AppButton",
  methods: {
    onClick() {
      this.$emit("onClick");
    },
  },
};
</script>

<style>

</style>
