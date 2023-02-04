<template>
  <header class="app-header">
    <div class="logo">
      <img src="../assets/svg/app_bar_logo.svg" alt="" />
      <h2>Gamejunx</h2>
    </div>
    <div>
      <ul class="actions">
       
        <li>
          <img src="../assets/svg/app_bar_search.svg" alt="" />
        </li>
        <li>
          <img src="../assets/svg/app_bar_notification.svg" alt="" />
        </li>
        <li>
          <img src="../assets/svg/app_bar_gamepad.svg" alt="" />
        </li>
      </ul>
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
  display: flex;
  justify-content: center;
  align-content: center;
  background-color: aqua;
}

.logo img{
  margin-bottom: 8px;
}

.app-header {
  display: flex;
  background-color: red;
  justify-content: space-between;
  align-items: center;
  padding: 0px 8px;
}

.actions {
  list-style: none;
  background-color: aqua;
}

.actions li {
  display: inline-block;
  margin-right: 24px; 
}

</style>
