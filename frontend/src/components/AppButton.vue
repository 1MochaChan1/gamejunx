<template>
  <div>
    <button class="button" @click="onClick()">
      <p class="button2">{{label}}</p>
    </button>
  </div>
</template>

<script>
export default {
  name: "AppButton",
  props:{
    label:{
      type:String
    },
  },
  methods: {
    onClick() {
      this.$emit("onClick");
    },
  },
};
</script>

<style>

</style>
