<template>
  <div>
    <button class="button" @click="onClick()">
      <p class="button2">{{label}}</p>
    </button>
  </div>
</template>

<script>
export default {
  name: "AppButton",
  data(){
    return {
      bg_color:"",
      fg_color:""
    }
  },
  props:{
    label:{
      type:String
    },
    background_color:{
      type:String,
      default: "var(--secondary-color)"
    },
    foreground_color:{
      type:String,
      default: "black"
    }
  },

  methods: {
    onClick() {
      this.$emit("onClick");
    },
  },

  created(){
    this.bg_color = this.background_color;
    this.fg_color = this.foreground_color;
  }
};
</script>

<style scoped>
.button{
  padding: 0px 8px;
  background-color: v-bind("bg_color");
  color: v-bind("fg_color");
}
.button:hover{
  filter: brightness(1.05);
  transition: 200ms;
}

.button:active{
  filter: brightness(.75);
  transition: 200ms;
}
</style>
