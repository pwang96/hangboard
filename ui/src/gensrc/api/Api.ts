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

import { Error, TestResponse } from "./data-contracts";
import { HttpClient, RequestParams } from "./http-client";

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
}
