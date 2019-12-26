# General

Button Claimed in us-west-2 account

geotrocities.com is my toy domain

# Services

## IOT 1-Click

### Project ButtonFun

- Template - emailFromButron (typo - fix)

- Placement 0 home

- added attribute dest_email

- can I get it to send the deviceId?

### Commands

#### Device

- aws iot1click-devices list-devices
- aws iot1click-devices get-device-methods --device-id G030PM047405B285
- aws iot1click-devices invoke-device-method --device-id G030PM047405B285 --device-method <method> --device-method-parameters <string>

#### Project

- aws iot1click-projects list-projects
- aws iot1click-projects describe-project --project-name ButtonFun 


## Lambda

Automatically created a lambda function from the 1-click template. It kicks off an email via SES.

Modified the Lambda function so that it could see the dest_email attribute I added to the IoT template

The function already had that, just didn't read the parameter

- Lambda folder contains simple functions and tests

### Creating Lambda function

#### Setup
##### Basic Information
- Function name: get_button_clicks
- Execution role (create new from policy templates): iot_read_lambda_role
- Policy template: Simple microservice permissions (there by default)
##### API Gateway Trigger
- Create a new API: HTTP API (Beta)
- Security: Open
- API name: get_button_clicks-API
- Deployment stage: default
- CORS/detailed metrics: not checked



- Using the blueprint microservice-http-endpoint-python
-

### Lambda function ideas

- get_clicks - return how many clicks have been received in total

- read dynamo and get a count

## SES

- let's get email working from my account
- configured geotrocities.com with SES

### Setting up SES

1. get a domain
2. setup
  - used DKIM which does some sort of authentication
3. setup MAIL FROM using smtp.geotrocities.com
4. in general AWS was able to do all the DNS and verifications automatically since it's hosted there


## S3

### Geotrocities static website

URL: [widgets](http://geotrocities.com/widgets.html)

### Buckets
- geotrocities.com - content
- www.geotrocities.com - HTTP redirect

### Policies

- policy applied to bucket under s3/geotrocities.com-bucket-policy.json

## Route53

### A records
- geotrocities. com -> bucket alias
- www.geotrocities.com -> bucket alias

### MX
- inbound-

## CloudWatch

- Lambda logging enabled makes it easy to get a sample payload


## Dynamo

- Table name: IoTButtonClicks
- Partition Key: buttonId (String)

going to see about using deviceId as partition key

## AWS Certificate Manager (ACM)

Just created the certs for geotrocities and www.geotrocities.com - required for API Gateway

# Future

## Cognito
- create user pool to associate clicks

## API Gateway - get the number of clicks from lambda

- Looking at using the new HTTPS API

- need to create the Lambda first

## CloudFront
