<template>
  <div class="parent">
    <input
      class="custom-textfield"
      :type="inputType"
      :placeholder="hint"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    />
    <div class="textfield-icon" @click="toggle()">
      <fa-icon v-if="showPassword" icon="eye-slash" />
      <fa-icon v-else-if="!showPassword" icon="eye" />
    </div>
  </div>
</template>

<script>
export default {
  name: "AppTextFieldPassword",
  data() {
    return {
      showPassword: false,
      inputType: "password",
    };
  },
  emits: ["update:modelValue"],
  props: {
    hint: {
      type: String,
    },
    modelValue: {},
  },

  methods: {
    toggle() {
      this.showPassword = !this.showPassword;
      this.inputType = this.showPassword ? "text" : "password";
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
