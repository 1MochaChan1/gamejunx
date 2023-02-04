<template>
  <!-- show light theme -->
  <div v-show="toggled" @click="toggle()" class="toggle-container">
    <div class="toggle-switch"></div>
    <img src="../assets/svg/toggle_switch_night.svg" alt="" />
  </div>
  <div v-show="!toggled" @click="toggle()" class="toggle-container">
    <img src="../assets/svg/toggle_switch_sun.svg" alt="" />
    <div class="toggle-switch"></div>
  </div>
</template>

<script>
export default {
  name: "AppToggleSwitch",
  data() {
    return {
      toggled: true,
      text: "Light",
    };
  },
  methods: {
    toggle() {
      this.toggled = !this.toggled;
      this.text = this.toggled ? "Light" : "Dark";
      return this.toggled;
    },
  },
};
</script>

<style>
.toggle-container {
  cursor: pointer;
  display: inline-flex;
  flex-direction: row;
  border-radius: 24px;
  padding: 4px;
  gap: 4px;
  background-color: grey;
}

.toggle-switch {
  height: 24px;
  width: 24px;
  border-radius: 80px;
  background-color: white;
}
</style>