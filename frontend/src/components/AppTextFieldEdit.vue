<template>
  <div class="parent">
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
  
</template>

<script>
export default {
  name: "AppTextFieldEdit",
  emits: ["update:modelValue"],
  props: {
    modelValue: {
      
    },
    hint: {
      type: String,
    },
    showIcon: {
      type: Boolean,
      default: false,
    },
    label: {
      type: String,
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
