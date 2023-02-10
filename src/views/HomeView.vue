<template>
  <div class="container">
    
    <h3>HomeView</h3>
    <div class="textfield-parent">
      <AppTextFieldPassword hint="Enter Password"/>
      <AppTextFieldEdit @edit="edit" hint="Edit Field"/>
      <AppTextField hint="Edit Field"/>
    </div>
  </div>
 
</template>

<script>
import AppTextFieldPassword from "../components/AppTextFieldPassword.vue";
import AppTextFieldEdit from "../components/AppTextFieldEdit.vue";
import AppTextField from "../components/AppTextField.vue";
export default {
  name: "HomeView",
  components: { AppTextFieldPassword,AppTextFieldEdit, AppTextField },

  methods:{
    edit(){
      console.log("Edit event called");
    }
  }
};
</script>

<style scoped>
.container {
  display: inline-block;
  width: 100vw;
}

.textfield-parent{
  display: flex;
  flex-direction: column;
  width:360px;
  direction: column;
  gap:8px;
}
</style>