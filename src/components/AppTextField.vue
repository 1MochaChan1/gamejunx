<template>
  <input type="text" v-model="value">
  <h4> Value: {{value}}</h4>
</template>

<script>
export default {
    name:'AppTextField',
   data(){
    return {
        value:''
    }
   }
}
</script>

<style>

</style>