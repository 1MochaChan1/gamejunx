<template>
  <div class="parent">
    <p class="subtitle2" :v-show="this.label">{{ this.label }}</p>
    <div class="field-container">
      <input
        class="custom-textfield"
        type="text"
        :placeholder="hint"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
      />
      <div v-show="showIcon" class="textfield-icon" @click="edit()">
        <fa-icon icon="pen" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppTextFieldEdit",
  emits: ["update:modelValue", "edit"],
  props: {
    modelValue: {},
    hint: {
      type: String,
    },
    showIcon: {
      type: Boolean,
      default: false,
    },
    label: {
      type: String,
      default:null
    },
  },

  methods: {
    edit() {
      this.$emit("edit");
    },
  },
};
</script>

<style scoped>
.parent{
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.field-container {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 8px;
}

.textfield-icon {
  right: 8px;
  bottom: 5px;
  position: absolute;
  cursor: pointer;
}
</style>
