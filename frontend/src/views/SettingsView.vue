<template>
  <div>
    <div class="local-toast-container">
      <Transition name="toast">
        <div v-if="this.showToast">
          <AppToast :content="this.message" :success="this.isSuccess" :screenWidth="'1300px'"/>
        </div>
      </Transition>
    </div>
    <div class="page-parent-container">
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
                v-model="this.passwords.oldPassword"
                label="Old Password"
                hint="•••••••••"
                class="field-width"
              />
              <span
                class="error-message"
                v-if="v$.passwords.oldPassword.$error"
                >{{ this.v$.passwords.oldPassword.$errors[0].$message }}</span
              >
            </div>
            <p class="link1">Forgot Password?</p>
          </div>

          <div class="field-row">
            <div>
              <AppTextFieldPassword
                v-model="this.passwords.newPassword"
                label="New Password"
                hint="•••••••••"
                class="field-width"
              />
              <span
                class="error-message"
                v-if="v$.passwords.newPassword.$error"
                >{{ this.v$.passwords.newPassword.$errors[0].$message }}</span
              >
            </div>
            <div>
              <AppTextFieldPassword
                v-model="this.passwords.confirmedPassword"
                label="Confirm Password"
                hint="•••••••••"
                class="field-width"
              />
              <span
                class="error-message"
                v-if="v$.passwords.confirmedPassword.$error"
                >{{
                  this.v$.passwords.confirmedPassword.$errors[0].$message
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
import AppToast from "../components/AppToast.vue";

export default {
  components: { AppTextFieldEdit, AppButton, AppTextFieldPassword, AppToast },
  name: "SettingsView",

  setup() {
    return { v$: useVuelidate() };
  },

  created() {
    this.name = titalize(this.name);
  },

  computed: {
    getUsernameErrorStatus() {
      return this.asyncErrors.isUsernameUnique;
    },
    getEmailErrorStatus() {
      return this.asyncErrors.isEmailUnique;
    },
    getPasswordErrorStatus() {
      return this.asyncErrors.isPasswordValid;
    },
    getPasswordMatchStatus() {
      return this.passwords.newPassword === this.passwords.confirmedPassword;
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
        oldPassword: {
          required: helpers.withMessage("Old password is required.", required),
          valid: helpers.withMessage(
            "Given password doesn't match",
            () => this.getPasswordErrorStatus
          ),
        },
        newPassword: {
          required: helpers.withMessage("New password is required.", required),
          minLength: minLength(8),
        },
        confirmedPassword: {
          required,
          match: helpers.withMessage(
            "The password does not match",
            () => this.getPasswordMatchStatus
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
        oldPassword: "",
        newPassword: "",
        confirmedPassword: "",
      },

      asyncErrors: {
        isUsernameUnique: true,
        isEmailUnique: true,
        isPasswordValid: true,
      },
      message: "",
      showToast: false,
      isSuccess: false,
    };
  },

  methods: {
    async saveNameChanged() {
      this.v$.name.$touch();
      this.v$.username.$touch();
      this.v$.email.$touch();

      // if response.status === error =---- then -> asyncErrors.isUsernameUnique = response.error
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
          this.showToastMessage(data.message, data.status);
        })
        .catch((res) => {
          data = res.response.data;
          this.showToastMessage(data.message, data.status);
        });

      this.asyncErrors.isUsernameUnique = !data.message
        .toLowerCase()
        .includes("username");
      await this.v$.username.$touch();

      this.asyncErrors.isEmailUnique = !data.message
        .toLowerCase()
        .includes("email");
      await this.v$.email.$touch();

      if (!(data.status === "error")) {
        this.populateStorage(data);
      }
    },

    async savePasswordChanged() {
      this.v$.passwords.oldPassword.$touch();
      this.v$.passwords.newPassword.$touch();
      this.v$.passwords.confirmedPassword.$touch();

      let data = null;
      await axios
        .put(this.baseUrl + APIEndpoints.change_user_password, {
          id: localStorage.id,
          oldPassword: this.passwords.oldPassword,
          newPassword: this.passwords.newPassword,
        })
        .then((res) => {
          data = res.data;
          this.showToastMessage(data.message, data.status);
        })
        .catch((res) => {
          data = res.response.data;
          this.showToastMessage(data.message, data.status);
        });

      this.asyncErrors.isPasswordValid = !data.message
        .toLowerCase()
        .includes("old password");
      await this.v$.passwords.oldPassword.$touch();
    },

    populateStorage(data) {
      localStorage.setItem("id", data.user.id);
      localStorage.setItem("name", data.user.name);
      localStorage.setItem("username", data.user.username);
      localStorage.setItem("email", data.user.email);
    },

    showToastMessage(msg, status) {
      this.message = msg;
      this.isSuccess = status != "error";

      this.showToast = true;
      setTimeout(() => (this.showToast = false), 3000);
    },
  },
};
</script>

<style scoped>
/* .local-toast-container{
  width: 80%;
} */

h2 {
  margin: 0px;
}

h6 {
  margin: 0px;
}
.link1 {
  margin-top: 36px;
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
