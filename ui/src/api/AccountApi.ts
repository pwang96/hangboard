import { Api } from "../gensrc/api/Api";
import {
  CreateAccountRequest,
  CreateAccountResponse,
  LoginRequest,
  LoginResponse,
} from "../gensrc/api/data-contracts";

const serviceBaseUrl = `${window.location.origin}`;
console.log(serviceBaseUrl);

const api = new Api({
  baseUrl: "http://127.0.0.1:5000",
});

export class AccountApi {
  static async createAccount(
    request: CreateAccountRequest,
  ): Promise<CreateAccountResponse> {
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
}
