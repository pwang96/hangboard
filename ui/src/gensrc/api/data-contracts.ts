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
  first_name: string;
  last_name: string;
  password: string;
  username: string;
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
  jwt?: string;
  success: boolean;
}

/**
 * TestResponse
 * Test response
 */
export interface TestResponse {
  message?: string;
}

/**
 * User
 * User
 */
export interface User {
  email: string;
  first_name: string;
  last_name: string;
  username: string;
}

/**
 * Users
 * List of users
 */
export interface Users {
  users: User[];
}
