'use strict';
import { APIGatewayProxyEvent, APIGatewayProxyHandler, APIGatewayProxyResult } from 'aws-lambda';

export function makeResponse (statusCode: number, body?: object): APIGatewayProxyResult {
    const response = {
      statusCode: statusCode,
      body: body ? JSON.stringify(body) : "",
      headers: {
        "Access-Control-Allow-Origin": "*",
        'Access-Control-Allow-Credentials': true,
      },
    };
    return response;
};

export type Optional<T> = T | null;