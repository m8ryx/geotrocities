import boto3
import json

class Button:
  def __init__(self):
    self.presses = []

  def press(self, click_type, click_time):
    self.presses.append([click_type, click_time])

  def presses(self):
    return self.presses

def encode_press(button):
  print("encoding")
  print(button)
  return({"click_type": button.click_type, "click_time": button.click_time})

def respond(err, res=None):
  print("in respond")

  return {
    "isBase64Encoded": 'false',
    'statusCode': '400' if err else '200',
#    'body': err.message if err else json.dumps(res.presses, default=encode_button),
    'body': err.message if err else json.dumps(res),
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': "*",
    },
  }

def lambda_handler(event, context):
  '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
  access to the request and response payload, including headers and
  status code.

  To scan a DynamoDB table, make a GET request with the TableName as a
  query string parameter. To put, update, or delete an item, make a POST,
  PUT, or DELETE request respectively, passing in the payload to the
  DynamoDB API as a JSON body.
  '''
  dynamo = boto3.client('dynamodb')

  button = Button()

  print("Received event: " + json.dumps(event, indent=2))

  operations = {
    'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
	  'GET': lambda dynamo, x: dynamo.scan(**x),
	  'POST': lambda dynamo, x: dynamo.put_item(**x),
	  'PUT': lambda dynamo, x: dynamo.update_item(**x),
  }

#    #operation = event['httpMethod']
  operation = 'GET'
  if operation in operations:
    print(event['queryStringParameters'])
#    payload = json.loads(event['queryStringParameters']) if operation == 'GET' else json.loads(event['body'])
    payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
    print(payload)
    res = operations[operation](dynamo, payload)
    print(res)
#    else:
#	print(respond(ValueError('Unsupported method "{}"'.format(operation))))
#	return respond(ValueError('Unsupported method "{}"'.format(operation)))
#
  clicks = res['Items']

  my_clicks = []

  for click in clicks:
    this_click = {}
    this_click['type'] = click['clickType']['S']
    this_click['time'] = click['reportedTime']['S']
#    button.press(clickType, time)

    my_clicks.append(this_click)


  print("Going to respond")
  response = respond(None, my_clicks)
  print("Finished responsd")

#  print(json.dumps(response))

#  body = json.loads(response['body'])


    #num_clicks = body['Count']
  return(response)


