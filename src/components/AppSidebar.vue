<template>
  <div>
    <aside>
      
        <div>
          <router-link class="button" to="/">
            <span><fa-icon icon="home" /></span>
            <div>Home</div>
          </router-link>

          <router-link class="button" to="/wishlist">
            <span><fa-icon icon="heart" /></span>
            <div>Wishlist</div>
          </router-link>

          <router-link class="button" to="/games">
            <span><fa-icon icon="tag" /></span>
            <div>Games</div>
          </router-link>

          <router-link class="button" to="/libraries">
            <span><fa-icon icon="gamepad" /></span>
            <div>Libraries</div>
          </router-link>
        </div>

        <div>
          <div class="divider"></div>
          <router-link class="button" to="/profile">
            <span><fa-icon icon="user" /></span>
            <div>Profile</div>
          </router-link>

          <router-link class="button" to="/settings">
            <span><fa-icon icon="gear" /></span>
            <div>Settings</div>
          </router-link>

          <router-link class="button" to="/Sign Out">
            <span><fa-icon icon="sign-out" /></span>
            <div>Sign Out</div>
          </router-link>
        </div>
      
    </aside>
  </div>
</template>


<script>
export default {
  name: "AppSidebar",
  data() {
    return {
      selected: null,
    };
  },
};
</script>

<style  scoped>
:root {
  ---sidebar-width: 250px;
}

aside {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 85vh;
  color: var(--neutral-unfocused-color);
  /* background-color: white; */
  width: 148px;
}

aside .divider {
  
  height: 1.25px;
  background-color: var(--neutral-indicator-color);
  border-radius: 1em;
}

.button {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 8px 0px;
}
</style>