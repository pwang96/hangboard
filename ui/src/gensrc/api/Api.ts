/* eslint-disable */
/* tslint:disable */
/*
 * ---------------------------------------------------------------
 * ## THIS FILE WAS GENERATED VIA SWAGGER-TYPESCRIPT-API        ##
 * ##                                                           ##
 * ## AUTHOR: acacode                                           ##
 * ## SOURCE: https://github.com/acacode/swagger-typescript-api ##
 * ---------------------------------------------------------------
 */

import {
  CreateAccountRequest,
  CreateAccountResponse,
  Error,
  LoginRequest,
  LoginResponse,
  TestResponse,
  Users,
} from "./data-contracts";
import { ContentType, HttpClient, RequestParams } from "./http-client";

export class Api<SecurityDataType = unknown> extends HttpClient<SecurityDataType> {
  /**
   * @description Return the test response
   *
   * @name GetHello
   * @request GET:/api/hello
   */
  getHello = (params: RequestParams = {}) =>
    this.request<TestResponse, Error>({
      path: `/api/hello`,
      method: "GET",
      format: "json",
      ...params,
    });
  /**
   * No description
   *
   * @name CreateAccount
   * @request POST:/api/join
   */
  createAccount = (data: CreateAccountRequest, params: RequestParams = {}) =>
    this.request<CreateAccountResponse, Error>({
      path: `/api/join`,
      method: "POST",
      body: data,
      type: ContentType.Json,
      format: "json",
      ...params,
    });
  /**
   * No description
   *
   * @name Login
   * @request POST:/api/login
   */
  login = (data: LoginRequest, params: RequestParams = {}) =>
    this.request<LoginResponse, Error>({
      path: `/api/login`,
      method: "POST",
      body: data,
      type: ContentType.Json,
      format: "json",
      ...params,
    });
  /**
   * No description
   *
   * @name GetUsers
   * @request GET:/api/users
   */
  getUsers = (params: RequestParams = {}) =>
    this.request<Users, Error>({
      path: `/api/users`,
      method: "GET",
      format: "json",
      ...params,
    });
}
