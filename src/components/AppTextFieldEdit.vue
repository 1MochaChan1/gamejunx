<template>
  <div class="parent">
    <input
      class="custom-textfield"
      type="text"
      :placeholder="hint"
      v-model="value"
    />
    <div class="textfield-icon" @click="edit()">
      <fa-icon icon="pen" />
    </div>
  </div>
</template>

<script>
export default {
  name: "AppTextFieldEdit",
  data() {
    return {
      value: "",
    };
  },
  props: ["hint",],
  methods: {
    edit() {
        this.$emit('edit');
    },
  },
};
</script>

<style scoped>
.parent {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 8px;
}

.textfield-icon {
  cursor: pointer;
}
</style>