import { Api } from "../gensrc/api/Api";
import {
  CreateAccountRequest,
  LoginRequest,
  LoginResponse,
  User,
} from "../gensrc/api/data-contracts";

const serviceBaseUrl = `${window.location.origin}`;
console.log(serviceBaseUrl);

const api = new Api({
  baseUrl: "http://127.0.0.1:5000",
});

export class AccountApi {
  static async createAccount(
    request: CreateAccountRequest,
  ): Promise<LoginResponse> {
    return await api
      .createAccount(request)
      .then((resp) => resp.data)
      .catch((err) => {
        console.log(err);
        return { success: false, message: "Could not create account" };
      });
  }

  static async login(request: LoginRequest): Promise<LoginResponse> {
    return await api
      .login(request)
      .then((resp) => resp.data)
      .catch((err) => {
        console.log(err);
        return { success: false };
      });
  }

  static async getUser(username: string): Promise<User> {
    return await api
      .getUser(username)
      .then((resp) => resp.data)
      .catch((err) => {
        console.log(err);
        return { username: "", first_name: "", last_name: "", email: "" };
      });
  }

  static async getProfile(): Promise<User> {
    return await api
      .getProfile()
      .then((resp) => resp.data)
      .catch((err) => {
        console.log(err);
        return { username: "", first_name: "", last_name: "", email: "" };
      });
  }
}
