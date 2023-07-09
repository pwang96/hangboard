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

/**
 * CreateAccountRequest
 * Request to create an account
 */
export interface CreateAccountRequest {
  email: string;
  password: string;
  username: string;
}

/**
 * CreateAccountResponse
 * Response to account creation
 */
export interface CreateAccountResponse {
  message?: string;
  success?: boolean;
}

/** Error */
export interface Error {
  errors?: object;
  message: string;
}

/**
 * LoginRequest
 * Request to login
 */
export interface LoginRequest {
  password: string;
  username: string;
}

/**
 * LoginResponse
 * Response to login
 */
export interface LoginResponse {
  success?: boolean;
}

/**
 * TestResponse
 * Test response
 */
export interface TestResponse {
  message?: string;
}
