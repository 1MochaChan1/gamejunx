<template>
 <div class="container">
    <h3>HomeView</h3>
 <AppTextField/>
 </div>
</template>

<script>
import AppTextField from "../components/AppTextField.vue";
export default {
    name:'HomeView',
    components:{AppTextField}
}
</script>

<style scoped>

.container{
    display: inline-block;
}

</style>