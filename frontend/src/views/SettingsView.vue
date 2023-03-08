<template>
  <div class="parent-container">
    <div class="account-settings-container">
      <h2>Account Settings</h2>
      <div class="fields-container">
        <AppTextFieldEdit
          label="Display Name"
          class="field-width"
          :showIcon="true"
        />
        <div class="field-row">
          <AppTextFieldEdit
            label="Username"
            class="field-width"
            :showIcon="true"
            @edit="this.edited"
          />
          <AppTextFieldEdit
            label="Email"
            class="field-width"
            :showIcon="true"
          />
        </div>
        <h6>Change Password</h6>
        <div class="field-row">
          <AppTextFieldEdit
            label="Old Password"
            hint="•••••••••"
            class="field-width"
            :showIcon="true"
          />
          <p class="link1">Forgot Password?</p>
        </div>

        <div class="field-row">
          <AppTextFieldEdit
            label="New Password"
            hint="•••••••••"
            class="field-width"
            :showIcon="true"
          />
          <AppTextFieldEdit
            label="Confirm Password"
            hint="•••••••••"
            class="field-width"
            :showIcon="true"
          />
        </div>
        <AppButton label="Terminate Account" style="width:133px "/>
      </div>
    </div>
  </div>
</template>

<script>
import AppButton from '../components/AppButton.vue';
import AppTextFieldEdit from "../components/AppTextFieldEdit.vue";
export default {
  components: { AppTextFieldEdit, AppButton },
  name: "SettingsView",
  methods: {
    edited() {
      console.log("edit called");
    },
  },
};
</script>

<style scoped>
h2 {
  margin: 0px;
}

h6 {
  margin: 4px 0px;
}
.link1 {
  margin-top: 34px;
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
