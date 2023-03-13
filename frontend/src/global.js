/* eslint-disable no-unused-vars */


export class APIEndpoints {
  static login = "login";
  static signup = "signup";
  static get_games = "get-games";
  static basic_user_details = "user-details/basic"
  static change_user_password = "user-details/password"
}

export function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export function titalize(text){
  if(text){
    return `${text[0].toUpperCase()}${text.slice(1)}`
  }
  return text;
}

/* eslint-enable no-unused-vars */
