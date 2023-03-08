<template>
  <div>
    <h2>Account Settings</h2>
    <div class="name-container">
        <AppTextFieldEdit/>        
    </div>
  </div>
</template>

<script>
import AppTextFieldEdit from '../components/AppTextFieldEdit.vue';
export default {
  components: { AppTextFieldEdit },
  name: "SettingsView",
};
</script>

<style scoped>
.name-container{
    display: flex;
    flex-wrap: wrap;

}
</style>
