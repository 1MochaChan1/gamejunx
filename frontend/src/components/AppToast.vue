<template>
  <div class="toast-parent-container">
    <div
      :class="{
        'toast-container-success': success,
        'toast-container-error': !success,
      }"
    >
      <p>{{ this.content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppToast",
  data() {
    return {
      screen_width: {
        type: String,
      },
    };
  },
  props: {
    content: {
      type: String,
      default: "Toast Content",
    },
    success: {
      type: Boolean,
      default: true,
    },

    screenWidth: {
      type: String,
      default: "99%",
    },
  },
  created() {
    this.screen_width = this.screenWidth;
  },
};
</script>

<style scoped>
.toast-parent-container {
  margin-top: 12px;
  position: fixed;
  display: flex;
  width: v-bind("screen_width");
  align-items: flex-end;
  justify-content: flex-end;
  /* background-color: pink; */
}

p {
  margin: 0px;
}
.toast-container-success {
  z-index: 1;
  background-color: var(--semantics-success-dark-color);
  padding: 12px;
  border-radius: 8px;
}
.toast-container-error {
  z-index: 1;
  background-color: var(--semantics-error-dark-color);
  padding: 12px;
  border-radius: 8px;
}
</style>
