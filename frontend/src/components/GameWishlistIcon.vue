<template>
  <span
    :class="{ 'wishlisted-game': this.wishlisted }"
    @click="this.changeColor()"
    ><fa-icon icon="heart"
  /></span>
</template>

<script>
export default {
  name: "GameWishlistIcon",

  created() {
    this.wishlisted = this.isWishlisted;
  },

  data() {
    return {
      wishlisted: false,
    };
  },

  props: {
    isWishlisted: {
      type: Boolean,
      default: false,
    },
  },

  methods: {
    changeColor() {
      this.wishlisted = !this.wishlisted;
    },
  },
};
</script>

<style scoped>
span {
  color: rgba(255, 255, 255, 0.75);
  transition: 300ms;
}
.wishlisted-game {
  color: var(--primary-color);
  transition: 300ms;
}
span:hover{
    filter: brightness(.75);
    transition: 300ms;    
}
</style>
