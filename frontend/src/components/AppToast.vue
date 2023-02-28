<template>
  <div class="toast-parent-container">
    <div
      :class="{
        'toast-container-success': success,
        'toast-container-error': !success,
      }"
    >
      <h6>{{ this.content }}</h6>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppToast",
  props: {
    content: {
      type: String,
      default: "Toast Content",
    },
    success: {
      type: Boolean,
      default: true,
    },
  },
};
</script>

<style>
.toast-parent-container {
    margin-top: 12px;
  position: fixed;
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: center;
}

h6 {
  margin: 0px;
}
.toast-container-success {
  z-index: 1;
  display: flex;
  align-items: center;
  align-self: center;
  justify-content: center;
  background-color: var(--semantics-success-dark-color);
  padding: 12px;
  border-radius: 12px;
}
.toast-container-error {
  z-index: 1;
  display: flex;
  align-items: center;
  align-self: center;
  justify-content: center;
  background-color: var(--semantics-error-dark-color);
  padding: 12px;
  border-radius: 12px;
}
</style>
