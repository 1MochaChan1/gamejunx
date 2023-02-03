<template>
    <div class="toggle-container">
        <button @click='toggle()' > {{text}} </button>
    </div>
</template>

<script>
export default {
    name:'AppToggleSwitch',
    data(){
        return{
            toggled:true,
            text:'Light'
        }
    },
    methods:{
        toggle(){
            this.toggled=!this.toggled;
            this.text = this.toggled? 'Light':'Dark';
            return this.toggled;
        }
    }
}
</script>

<style>

</style>