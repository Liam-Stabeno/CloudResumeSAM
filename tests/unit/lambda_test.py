import json
import time
from lambda_function import lambda_handler

# Test "POST, GET, OPTIONS" methods one at a time.

# POST Test
event1 = {
    "httpMethod" : "POST",
    "userAgent" : "...Test UserAgent passed thru...",
}

# Call the lambda_handler function
response = lambda_handler(event1, None)

# Print the response
print("Response: POST test succesful!")
print(json.dumps(response, indent=4))

time.sleep(2)

#GET Test
event2 = {
    "httpMethod" : "GET",
    "userAgent" : "...test userAgent passed thru...",
}

# Call the lambda_handler function
response = lambda_handler(event2, None)

# Print the response
print("Response: GET test succesful!")
print(json.dumps(response, indent=4))

time.sleep(2)


#OPTIONS Test - Our AWS API gateway is set up for CORS and will automatically send OPTIONS requests before the POST or GET requests. This test ensures that the lambda function can handle OPTIONS requests correctly.

event3 = {
    "httpMethod" : "OPTIONS",
    "userAgent" : "...test userAgent passed thru...",
}

response = lambda_handler(event3, None)

print("Response: OPTIONS test succesful!")
print(json.dumps(response, indent=4))
