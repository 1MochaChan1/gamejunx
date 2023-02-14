<template>
  <div class="container">
    <img src="../assets/images/login.jpg" alt="" />
    <div class="login-container">
      <AppLogo />

      <div class="login-container-wrapper">
        <div class="big-logo-wrapper">
          <img src="../assets/svg/app_bar_logo.svg" alt="" />
        </div>
        <div class="textfield-container">
          <AppTextFieldEdit class="no-icon-field" :hint="'Username'" />
          <AppTextFieldPassword :hint="'•••••••'" :showIcon="true" />
        </div>

        <div class="checkbox-wrapper">
          <input type="checkbox" name="remember" v-model="this.rememberMe" />
          <label for="remember" @click="toggle()">
            <p>Remember Me</p>
          </label>
        </div>
        <AppButton @onClick="login()" />

        <div class="login-wrapper">
          <p class="link2" @click="forgotPassword()">Forgot password</p>
        </div>
        <div class="signup-wrapper">
          <span> <p>Don't have an account?</p> </span>
          <span> <p class="link2">Signup Now</p> </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import AppLogo from "../components/AppLogo.vue";
import AppTextFieldEdit from "../components/AppTextFieldEdit.vue";
import AppTextFieldPassword from "../components/AppTextFieldPassword.vue";
import AppButton from "../components/AppButton.vue";
export default {
  data: () => ({
    rememberMe: true,
  }),
  name: "LoginView",
  methods: {
    toggle() {
      this.rememberMe = !this.rememberMe;
    },

    login() {
      console.log("Login button pressed!");
    },
    forgotPassword() {
      console.log("Forgot password link pressed");
    },
    getResponse() {
     
      axios.get();
      const path = "http://jsonplaceholder.typicode.com/posts";
      axios.get(path).then((res) => {
        console.log(res);
      }).catch((err)=>
      {
        console.error(err)
      });
    },
  },

  mounted () {
    console.log("something");
    axios
      .get('http://127.0.0.1:5000/users')
      .then(response => (console.log(response ))).catch((err)=> console.err(err));
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

.checkbox-wrapper {
  display: flex;
  margin-bottom: 16px;
}

.login-wrapper {
  display: flex;
  justify-content: flex-end;
}
.signup-wrapper {
  margin-top: 40px;
  display: flex;
  gap: 8px;
  justify-content: center;
}

.login-container-wrapper {
  margin-top: 18vh;
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

label {
  cursor: pointer;
}

img {
  width: 50%;
  height: 100vh;
  object-fit: cover;
}
</style>
