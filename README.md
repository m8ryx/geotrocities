## General

Button Claimed in us-west-2 rrezinas@gmail.com account

geotrocities.com is my toy domain

## Services

### IOT 1-Click

#### Project ButtonFun

- Template - emailFromButron (typo - fix)

- Placement 0 home

- added attribute dest_email

### Lambda

Automatically created a lambda function from the 1-click template. It kicks off an email via SES.

Modified the Lambda function so that it could see the dest_email attribute I added to the IoT template

The function already had that, just didn't read the parameter

### SES

- let's get email working from my account
- configured geotrocities.com with SES

#### Setting up SES

1. get a domain
2. setup
  - used DKIM which does some sort of authentication
3. setup MAIL FROM using smtp.geotrocities.com
4. in general AWS was able to do all the DNS and verifications automatically since it's hosted there


### S3

#### Geotrocities static website

#### Buckets
- geotrocities.com - content
- www.geotrocities.com - HTTP redirect

#### Policies

- policy applied to bucket under s3/geotrocities.com-bucket-policy.json

### Route53

#### A records
- geotrocities. com -> bucket alias
- www.geotrocities.com -> bucket alias

#### MX
- inbound-
