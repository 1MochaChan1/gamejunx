<template>
  <div class="parent">
    <input
      class="custom-textfield"
      type="text"
      :placeholder="hint"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    />
    <!-- <div class="textfield-icon" @click="edit()">
    </div> -->
  </div>
</template>

<script>
export default {
  name: "AppTextField",
  emits: ["update:modelValue"],
  props: {
    modelValue: {},
    hint: {
      type: String,
    },
    label: {
      type: String,
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
