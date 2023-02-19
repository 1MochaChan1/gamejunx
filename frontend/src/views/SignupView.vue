<template>
  <form @submit.prevent="this.signup" method="POST">
    <div class="container">
      <img src="../assets/images/signup.jpg" alt="" />
      <div>
        <AppLogo />

        <div class="signup-container-wrapper">
          <div class="big-logo-wrapper">
            <img src="../assets/svg/app_bar_logo.svg" alt="" />
          </div>
          <div class="textfield-container">
            <div>
              <AppTextFieldEdit
                class="no-icon-field"
                v-model="name"
                :hint="'Name'"
              />
              <span v-if="v$.name.$error" class="error-message">{{
                v$.name.$errors[0].$message
              }}</span>
            </div>
            <div>
              <AppTextFieldEdit
                class="no-icon-field"
                v-model="username"
                :hint="'Username'"
              />
              <span v-if="v$.username.$error" class="error-message">{{
                v$.username.$errors[0].$message
              }}</span>
            </div>
            <div>
              <AppTextFieldEdit
                class="no-icon-field"
                v-model="email"
                :hint="'Email'"
              />
              <span v-if="v$.email.$error" class="error-message">
                {{ v$.email.$errors[0].$message }}
              </span>
            </div>

            <div>
              <AppTextFieldPassword
                v-model="this.formPassword.password"
                :hint="'Password'"
                :showIcon="true"
              />
              <span
                v-if="v$.formPassword.password.$error"
                class="error-message"
              >
                {{ v$.formPassword.password.$errors[0].$message }}
              </span>
            </div>

            <div>
              <AppTextFieldPassword
                v-model="this.formPassword.confirmed"
                :hint="'Confirm Password'"
                :showIcon="true"
              />
              <span
                v-if="v$.formPassword.confirmed.$error"
                class="error-message"
              >
                {{ v$.formPassword.confirmed.$errors[0].$message }}
              </span>
            </div>
          </div>
          <div class="vertical-space"></div>

          <AppButton :label="'Sign Up'" />

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
import useVuedilate from "@vuelidate/core";
import { required, email, minLength, helpers } from "@vuelidate/validators";
import AppLogo from "../components/AppLogo.vue";
import AppTextFieldEdit from "../components/AppTextFieldEdit.vue";
import AppTextFieldPassword from "../components/AppTextFieldPassword.vue";
import AppButton from "../components/AppButton.vue";
import axios from "axios";

export default {
  name: "SignupView",

  // use v$.email.$touch() to access field individually
  // use v$.$validate() to validate the entire form.
  setup: () => ({
    v$: useVuedilate(),
  }),

  data: () => ({
    name: "sda",
    username: "adads",
    email: "dsa@mail.com",
    formPassword: {
      password: "123456789",
      confirmed: "123456789",
    },
  }),

  validations: () => ({
    name: {
      required: helpers.withMessage("Name can't be empty", required),
    },
    username: {
      required: helpers.withMessage("Username can't be empty", required),
    },
    email: {
      required: helpers.withMessage("Email can't be empty", required),
      email: helpers.withMessage("Please provide a valid email", email),
    },
    formPassword: {
      password: {
        required: helpers.withMessage("Password can't be empty", required),
        minLength: minLength(8),
      },
      confirmed: {
        sameAs: helpers.withMessage("The password does not match", function () {
          return this.formPassword.password == this.formPassword.confirmed;
        }),
      },
    },
  }),

  methods: {
    async signup() {
      let isValid = await this.v$.$validate();
      if (isValid) {
        await axios
          .post(this.baseUrl + "/signup", {
            name: this.name,
            username: this.username,
            email: this.email,
            password: this.formPassword.password,
          })
          .then((e) => {
            if (e.data.status == "success") {
              this.$router.push("login");
            }
          })
          .catch((e) => {
            alert(e.response.data.message);
          });
      }
    },
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

.no-icon-field {
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

.vertical-space {
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
