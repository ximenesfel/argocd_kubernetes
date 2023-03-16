#!/bin/bash

# Define as variáveis necessárias para autenticar com o ECR
AWS_ACCOUNT_ID=127012818163
AWS_REGION=us-east-1
AWS_CLI_VERSION=2

aws ecr --region $AWS_REGION get-authorization-token --output text --query 'authorizationData[].authorizationToken' | base64 -d

