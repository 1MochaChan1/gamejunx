<template>
  <form @submit.prevent="this.signup" method="POST">
    <div class="container">
      <img src="../assets/images/signup.jpg" alt="" />
      <div >
        <AppLogo />

        <div class="signup-container-wrapper">
          <div class="big-logo-wrapper">
            <img src="../assets/svg/app_bar_logo.svg" alt="" />
          </div>
          <div class="textfield-container">
            <AppTextFieldEdit
              class="no-icon-field"
              v-model="username"
              :hint="'Username'"
            />
            <AppTextFieldEdit
              class="no-icon-field"
              v-model="email"
              :hint="'Email'"
            />
            <AppTextFieldPassword
              v-model="password"
              :hint="'•••••••'"
              :showIcon="true"
            />
            <AppTextFieldPassword
              v-model="c_password"
              :hint="'•••••••'"
              :showIcon="true"
            />
          </div>
          <div class="vertical-space"></div>

          <AppButton :label="'Sign Up'"/>

          <router-link class="login-wrapper" to="/login">
            <span> <p>Already have an account?</p> </span>
            <span> <p class="link2">Login Instead</p> </span>
          </router-link>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
// import axios from "axios";
import AppLogo from "../components/AppLogo.vue";
import AppTextFieldEdit from "../components/AppTextFieldEdit.vue";
import AppTextFieldPassword from "../components/AppTextFieldPassword.vue";
import AppButton from "../components/AppButton.vue";
export default {
  name: "SignupView",

  data: () => ({
    username: "",
    email: "",
    password: "",
    c_password: "",
  }),

  methods: {
    signup() {},
  },
  components: {
    AppLogo,
    AppTextFieldEdit,
    AppTextFieldPassword,
    AppButton,
  },
};
</script>

<style scoped>
.container {
  display: flex;
  gap: 16px;
  flex-direction: row;
}

.textfield-container {
  display: flex;
  flex-direction: column;
  width: var(--textfield-width);
  gap: 16px;
}

.textfield-container > .no-icon-field {
  width: calc(var(--textfield-width) - 25px);
}

.login-wrapper {
  margin-top: 32px;
  display: flex;
  gap: 8px;
  text-decoration: none;
  color: var(--neutral-text-color);
  justify-content: center;
}

.signup-container-wrapper {
  margin-top: 16vh;
  margin-left: 25vh;
}

.big-logo-wrapper > img {
  height: 12vh;
  width: 12vh;
}
.big-logo-wrapper {
  display: flex;
  justify-content: center;
  margin-bottom: 5vh;
}

.vertical-space{
  height: 24px;
}

label {
  cursor: pointer;
}

img {
  width: 50%;
  height: 100vh;
  object-fit: cover;
}
</style>
