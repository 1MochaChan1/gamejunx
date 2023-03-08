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

<style scoped>
.toast-parent-container {
  margin-top: 12px;
  position: fixed;
  display: flex;
  width: 99%;
  align-items: flex-end;
  justify-content: flex-end;
  /* background-color: pink; */
}

p {
  margin: 0px;
}
.toast-container-success {
  z-index: 1;
  display: flex;
  /* align-items: center;
  align-self: center;
  justify-content: flex-end; */
  background-color: var(--semantics-success-dark-color);
  padding: 12px;
  border-radius: 8px;
}
.toast-container-error {
  z-index: 1;
  display: flex;
  /* align-items: center; */
  /* align-self: center; */
  /* justify-content: flex-end; */
  background-color: var(--semantics-error-dark-color);
  padding: 12px;
  border-radius: 8px;
}
</style>
