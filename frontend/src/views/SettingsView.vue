<template>
  <div class="parent-container">
    <div class="account-settings-container">
      <h2>Account Settings</h2>
      <div class="fields-container">
        <div>
          <AppTextFieldEdit
            v-model="this.name"
            label="Display Name"
            class="field-width"
          />
          <span class="error-message" v-if="v$.name.$error"> something </span>
        </div>
        <div class="field-row">
          <div>
            <AppTextFieldEdit
              v-model="this.username"
              label="Username"
              class="field-width"
            />

            <span class="error-message" v-if="v$.username.$error">
              {{ this.v$.username.$errors[0].$message }}
            </span>
          </div>
          <AppTextFieldEdit
            v-model="this.email"
            label="Email"
            class="field-width"
          />
        </div>
        <AppButton
          label="Save Changes"
          style="width: max-content"
          @click="this.saveNameChanged"
        />
        <br />
        <h6>Change Password</h6>
        <div class="field-row">
          <AppTextFieldEdit
            label="Old Password"
            hint="•••••••••"
            class="field-width"
          />
          <p class="link1">Forgot Password?</p>
        </div>

        <div class="field-row">
          <AppTextFieldEdit
            label="New Password"
            hint="•••••••••"
            class="field-width"
          />
          <AppTextFieldEdit
            label="Confirm Password"
            hint="•••••••••"
            class="field-width"
          />
        </div>
        <AppButton
          label="Save Changes"
          style="width: max-content"
          @click="this.savePasswordChanged"
        />
        <br />
        <AppButton
          label="Terminate Account"
          style="width: max-content"
          :background_color="'var(--semantics-error-color)'"
          :foreground_color="'var(--neutral-text-color)'"
        />
      </div>
    </div>
  </div>
</template>

<script>
import useVuelidate from "@vuelidate/core";
import { required, email, helpers } from "@vuelidate/validators";
import AppButton from "../components/AppButton.vue";
import AppTextFieldEdit from "../components/AppTextFieldEdit.vue";
import { delay, titalize } from "../global";
export default {
  components: { AppTextFieldEdit, AppButton },
  name: "SettingsView",

  setup() {
    return { v$: useVuelidate() };
  },

  created() {
    this.name = titalize(this.name);
  },

  validations() {
    return {
      name: { required },
      username: {
        required,
        unique: helpers.withMessage("Username is already taken", function () {
          return this.async_errors.is_username_unique;
        }),
      },
      email: { required, email },
      passwords: {
        old_password: { required },
        new_password: { required },
        confirmed_password: { required },
      },
    };
  },

  data() {
    return {
      name: localStorage.getItem("name"),
      username: localStorage.getItem("username"),
      email: localStorage.getItem("email"),
      passwords: {
        old_password: "",
        new_password: "",
        confirmed_password: "",
      },
      id: localStorage.getItem("id"),

      async_errors: {
        is_username_unique: true,
        is_email_unique: true,
        is_password_unique: true,
      },
    };
  },

  methods: {
    edited() {
      //   console.log("edit called");
    },

    uniqueUsernameError() {
      return;
    },

    async saveNameChanged() {
      this.v$.name.$touch();
      this.v$.username.$touch();
      this.v$.email.$touch();

      await delay(2000);
      // if response.status === error =---- then -> async_errors.is_username_unique = response.error
      // else _username.error = ''
      if (this.username === "leinadd") {
        this.async_errors.is_username_unique = false;
      }else{
        this.async_errors.is_username_unique = true;
      }
      await this.v$.username.$touch();
    },
    savePasswordChanged() {
      this.v$.passwords.old_password.$touch();
      this.v$.passwords.new_password.$touch();
      this.v$.passwords.confirmed_password.$touch();
    },
  },
};
</script>

<style scoped>
h2 {
  margin: 0px;
}

h6 {
  margin: 0px;
}
.link1 {
  margin-top: 36px;
}

.parent-container {
  display: flex;
  flex-direction: column;
  gap: 32px;
  padding-left: 4px;
}

.account-settings-container {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.fields-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.field-row {
  display: flex;
  align-items: center;

  gap: 24px;
}

.field-width {
  width: 536px;
}
</style>
