<template>
  <header class="app-header">
    <div class="logo">
      <img src="../assets/svg/app_bar_logo.svg" alt="" />
      <h4>Gamejunx</h4>
    </div>
    <div>
      <!-- <ul class="actions">
       
        <li>
          <img src="../assets/svg/app_bar_search.svg" alt="" />
        </li>
        <li>
          <img src="../assets/svg/app_bar_notification.svg" alt="" />
        </li>
        <li>
          <img src="../assets/svg/app_bar_gamepad.svg" alt="" />
        </li>
      </ul> -->
    </div>
  </header>
</template>

<script>
export default {
  name: "AppHeader",
};
</script>

<style>

.logo{
  display: inline-flex;
  justify-content: center;
  align-content: center;
  gap: 4px;
  color: var(--primary-color);
}

.logo img{
  margin-bottom: 0px;
}

.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0px 16px;
  
}

/* .actions {
  list-style: none;
}

.actions li {
  display: inline-block;
  margin-right: 24px; 
  cursor: pointer;
} */

</style>
