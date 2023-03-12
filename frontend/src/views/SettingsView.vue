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
          <span class="error-message" v-if="v$.name.$error">
            {{ this.v$.name.$errors[0].$message }}
          </span>
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
          <div>
            <AppTextFieldEdit
              v-model="this.email"
              label="Email"
              class="field-width"
            />
            <span class="error-message" v-if="v$.email.$error">
              {{ this.v$.email.$errors[0].$message }}
            </span>
          </div>
        </div>
        <AppButton
          label="Save Changes"
          style="width: max-content"
          @click="this.saveNameChanged"
        />
        <br />
        <h6>Change Password</h6>
        <div class="field-row">
          <div>
            <AppTextFieldPassword
              v-model="this.passwords.old_password"
              label="Old Password"
              hint="•••••••••"
              class="field-width"
            />
            <span
              class="error-message"
              v-if="v$.passwords.old_password.$error"
              >{{ this.v$.passwords.old_password.$errors[0].$message }}</span
            >
          </div>
          <p class="link1">Forgot Password?</p>
        </div>

        <div class="field-row">
          <div>
            <AppTextFieldPassword
              v-model="this.passwords.new_password"
              label="New Password"
              hint="•••••••••"
              class="field-width"
            />
            <span
              class="error-message"
              v-if="v$.passwords.new_password.$error"
              >{{ this.v$.passwords.new_password.$errors[0].$message }}</span
            >
          </div>
          <div>
            <AppTextFieldPassword
              v-model="this.passwords.confirmed_password"
              label="Confirm Password"
              hint="•••••••••"
              class="field-width"
            />
            <span
              class="error-message"
              v-if="v$.passwords.confirmed_password.$error"
              >{{
                this.v$.passwords.confirmed_password.$errors[0].$message
              }}</span
            >
          </div>
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
import { required, email, minLength, helpers } from "@vuelidate/validators";
import AppButton from "../components/AppButton.vue";
import AppTextFieldEdit from "../components/AppTextFieldEdit.vue";
import { APIEndpoints, titalize } from "../global";
import axios from "axios";
import AppTextFieldPassword from "../components/AppTextFieldPassword.vue";
export default {
  components: { AppTextFieldEdit, AppButton, AppTextFieldPassword },
  name: "SettingsView",

  setup() {
    return { v$: useVuelidate() };
  },

  created() {
    this.name = titalize(this.name);
  },

  computed: {
    getUsernameErrorStatus() {
      return this.async_errors.is_username_unique;
    },
    getEmailErrorStatus() {
      return this.async_errors.is_email_unique;
    },
    getPasswordErrorStatus() {
      return this.async_errors.is_password_valid;
    },
  },

  validations() {
    return {
      name: {
        required: helpers.withMessage("Display name can't be empty", required),
      },
      username: {
        required,
        unique: helpers.withMessage(
          "Username is already taken",
          () => this.getUsernameErrorStatus
        ),
      },
      email: {
        required,
        email,
        unique: helpers.withMessage(
          "Email is already taken",
          () => this.getEmailErrorStatus
        ),
      },
      passwords: {
        old_password: {
          required: helpers.withMessage("Old password is required.", required),
          valid: helpers.withMessage(
            "Given password doesn't match",
            () => this.getPasswordErrorStatus
          ),
        },
        new_password: {
          required: helpers.withMessage("New password is required.", required),
          minLength: minLength(8),
        },
        confirmed_password: {
          required,
          match: helpers.withMessage(
            "The password does not match",
            () => this.passwords.new_password === this.passwords.old_password
          ),
        },
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
        is_password_valid: true,
      },
    };
  },

  methods: {
    async saveNameChanged() {
      this.v$.name.$touch();
      this.v$.username.$touch();
      this.v$.email.$touch();

      // if response.status === error =---- then -> async_errors.is_username_unique = response.error
      // else _username.error = ''
      let data = null;
      await axios
        .put(this.baseUrl + APIEndpoints.basic_user_details, {
          id: localStorage.id,
          name: this.name,
          username: this.username,
          email: this.email,
        })
        .then((res) => {
          data = res.data;
        })
        .catch((res) => {
          data = res.response.data;
        });
      console.log(data);
      if (data.status === "error") {
        if (data.message.toLowerCase().includes("username")) {
          this.async_errors.is_username_unique = false;
          await this.v$.username.$touch();
        } else if (data.message.toLowerCase().includes("email")) {
          this.async_errors.is_email_unique = false;
          await this.v$.email.$touch();
        }
      } else {
        this.populateStorage(data);
      }
    },

    savePasswordChanged() {
      this.v$.passwords.old_password.$touch();
      this.v$.passwords.new_password.$touch();
      this.v$.passwords.confirmed_password.$touch();

      
    },

    populateStorage(data) {
      localStorage.setItem("id", data.user.id);
      localStorage.setItem("name", data.user.name);
      localStorage.setItem("username", data.user.username);
      localStorage.setItem("email", data.user.email);
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
