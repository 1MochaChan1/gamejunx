<template>
  <form @submit.prevent="this.login" method="POST">
    <Transition name="toast">
      <div v-if="this.showToast">
        <AppToast :content="this.message" :success="this.success"/>
      </div>
    </Transition>
    <div class="container">
      <img src="../assets/images/login.jpg" alt="" />
      <div>
        <AppLogo />

        <div class="login-container-wrapper">
          <div class="big-logo-wrapper">
            <img src="../assets/svg/app_bar_logo.svg" alt="" />
          </div>
          <div class="textfield-container">
            <div>
              <AppTextFieldEdit
                class="no-icon-field"
                v-model="username"
                :hint="'Username or Email'"
              />
              <span v-if="v$.username.$error" class="error-message">{{
                v$.username.$errors[0].$message
              }}</span>
            </div>

            <div>
              <AppTextFieldPassword
                v-model="password"
                :hint="'•••••••'"
                :showIcon="true"
              />
              <span v-if="v$.password.$error" class="error-message">{{
                v$.username.$errors[0].$message
              }}</span>
            </div>
          </div>

          <div class="checkbox-wrapper">
            <input type="checkbox" name="remember" v-model="this.rememberMe" />
            <label for="remember" @click="toggle()">
              <p>Remember Me</p>
            </label>
          </div>
          <AppButton :label="'Login'" />

          <div class="login-wrapper">
            <p class="link2" @click="forgotPassword()">Forgot password</p>
          </div>
          <router-link class="signup-wrapper" to="/signup">
            <span> <p>Don't have an account?</p> </span>
            <span> <p class="link2">Signup Now</p> </span>
          </router-link>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import axios from "axios";
import AppLogo from "../components/AppLogo.vue";
import AppTextFieldEdit from "../components/AppTextFieldEdit.vue";
import AppTextFieldPassword from "../components/AppTextFieldPassword.vue";
import AppButton from "../components/AppButton.vue";
import { required, helpers } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import AppToast from "../components/AppToast.vue";
export default {
  setup: () => ({
    v$: useVuelidate(),
  }),

  // computed: {
  //   getToastVal() {
  //     return this.showToast;
  //   },
  // },

  data: () => ({
    rememberMe: true,
    username: "",
    password: "",
    showToast: false,
    success: false,
    toastMessage: null,
  }),

  validations: () => ({
    username: {
      required: helpers.withMessage(
        "This field can't be left empty!",
        required
      ),
    },
    password: {
      required: helpers.withMessage(
        "This field can't be left empty!",
        required
      ),
    },
  }),

  name: "LoginView",
  methods: {
    toggle() {
      this.rememberMe = !this.rememberMe;
    },

    async login() {
      let isValid = await this.v$.$validate();

      if (isValid) {
        let response = await axios
          .post(this.baseUrl + "/login", {
            username: this.username,
            password: this.password,
          })
          .then(() => {})
          .catch((e) => {

            this.message = e.response.data.message;
            this.success = (e.response.data.status != 'error')

            console.log(this.message);
            this.showToast = true;
            setTimeout(() => (this.showToast = false), 2000);
          });

        switch (response.status) {
          case 200:
            localStorage.setItem("token", response.data.token);
            axios.defaults.headers.common["Authorization"] =
              "Bearer " + localStorage.getItem("token");
            this.$router.push("/home");
        }
      }
    },
    forgotPassword() {
      // console.log("Forgot password link pressed");
    },
  },

  components: {
    AppLogo,
    AppTextFieldEdit,
    AppTextFieldPassword,
    AppButton,
    AppToast,
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

.no-icon-field {
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
  margin-top: 32px;
  display: flex;
  gap: 8px;
  text-decoration: none;
  color: var(--neutral-text-color);
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
