<template>
  <div>
    <aside>
      <div>
        <router-link class="sidebar-button body1" to="/home">
          <span><fa-icon icon="home" /></span>
          <div><p>Home</p></div>
        </router-link>

        <router-link class="sidebar-button body1" to="/wishlist">
          <span><fa-icon icon="heart" /></span>
          <div><p>Wishlsit</p></div>
        </router-link>

        <router-link class="sidebar-button body1" to="/games">
          <span><fa-icon icon="tag" /></span>
          <div><p>Games</p></div>
        </router-link>

        <router-link class="sidebar-button body1" to="/libraries">
          <span><fa-icon icon="gamepad" /></span>
          <div><p>Libraries</p></div>
        </router-link>
      </div>

      <div>
        <div class="divider"></div>
        <router-link class="sidebar-button body1" to="/profile">
          <span><fa-icon icon="user" /></span>
          <div><p>Profile</p></div>
        </router-link>

        <router-link class="sidebar-button body1" to="/settings">
          <span><fa-icon icon="gear" /></span>
          <div><p>Settings</p></div>
        </router-link>

        <router-link @click="this.clearStorage()" class="sidebar-button body1" to="/login">
          <span><fa-icon icon="sign-out" /></span>
          <div><p>Sign Out</p></div>
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
  methods: {
    clearStorage(){
      localStorage.clear();
    }
  }
};
</script>

<style scoped>
:root {
  ---sidebar-width: 240px;
}

aside {
  position: fixed;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-top: 80px;
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

.sidebar-button {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 8px 0px;
  text-decoration: none;
  cursor: pointer;
  color: var(--neutral-unfocused-color);
}

.sidebar-button:hover {
  padding: 8px;
  transition: 0.2s;
}

.router-link-exact-active {
  font-family: var(--font-family);
  font-weight: var(--font-weight-medium);
  font-size: 14px;
  color: var(--secondary-color);
}
</style>
