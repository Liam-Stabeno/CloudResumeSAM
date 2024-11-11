import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import json
import pytest
from visitor_data import app


@pytest.fixture()
def apigwPOST_event():
    """Generates API GW Event based on real-world HTTP API event structure for POST"""
    return {
        "version": "2.0",
        "routeKey": "ANY /",
        "rawPath": "/",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "content-length": "117",
            "content-type": "application/json",
            "host": "a7zp3gtd03.execute-api.us-west-2.amazonaws.com",
            "origin": "http://cr-sam-app-s3-hosting-bucket.s3-website-us-west-2.amazonaws.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "http://cr-sam-app-s3-hosting-bucket.s3-website-us-west-2.amazonaws.com/",
            "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "x-amzn-trace-id": "Root=1-67326b39-1e627ec774a15a6951ba862d",
            "x-forwarded-for": "50.47.153.27",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https"
        },
        "requestContext": {
            "accountId": "952977564466",
            "apiId": "a7zp3gtd03",
            "domainName": "a7zp3gtd03.execute-api.us-west-2.amazonaws.com",
            "domainPrefix": "a7zp3gtd03",
            "http": {
                "method": "POST",
                "path": "/",
                "protocol": "HTTP/1.1",
                "sourceIp": "50.47.153.27",
                "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
            },
            "requestId": "BGWxCjxQPHcESng=",
            "routeKey": "ANY /",
            "stage": "$default",
            "time": "11/Nov/2024:20:38:17 +0000",
            "timeEpoch": 1731357497410
        },
        "body": "{\"userAgent\":\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36\"}",
        "isBase64Encoded": False
    }


@pytest.fixture()
def apigwGET_event():
    """Generates API GW Event based on real-world HTTP API event structure for GET"""
    return {
        "version": "2.0",
        "routeKey": "ANY /",
        "rawPath": "/",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "content-length": "0",
            "content-type": "application/json",
            "host": "a7zp3gtd03.execute-api.us-west-2.amazonaws.com",
            "origin": "http://cr-sam-app-s3-hosting-bucket.s3-website-us-west-2.amazonaws.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "http://cr-sam-app-s3-hosting-bucket.s3-website-us-west-2.amazonaws.com/",
            "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "x-amzn-trace-id": "Root=1-673277ba-6e66d00951157c0e59f3f32a",
            "x-forwarded-for": "50.47.153.27",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https"
        },
        "requestContext": {
            "accountId": "952977564466",
            "apiId": "a7zp3gtd03",
            "domainName": "a7zp3gtd03.execute-api.us-west-2.amazonaws.com",
            "domainPrefix": "a7zp3gtd03",
            "http": {
                "method": "GET",
                "path": "/",
                "protocol": "HTTP/1.1",
                "sourceIp": "50.47.153.27",
                "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
            },
            "requestId": "BGelNiT9PHcEMQA=",
            "routeKey": "ANY /",
            "stage": "$default",
            "time": "11/Nov/2024:21:31:38 +0000",
            "timeEpoch": 1731360698521
        },
        "isBase64Encoded": False
    }
@pytest.fixture()
def apigwOPTIONS_event():
    """Generates API GW Event based on real-world HTTP API event structure for OPTIONS"""
    return {
        "version": "2.0",
        "routeKey": "ANY /",
        "rawPath": "/",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "content-length": "0",
            "content-type": "application/json",
            "host": "a7zp3gtd03.execute-api.us-west-2.amazonaws.com",
            "origin": "http://cr-sam-app-s3-hosting-bucket.s3-website-us-west-2.amazonaws.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "http://cr-sam-app-s3-hosting-bucket.s3-website-us-west-2.amazonaws.com/",
            "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "x-amzn-trace-id": "Root=1-673277ba-6e66d00951157c0e59f3f32a",
            "x-forwarded-for": "50.47.153.27",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https"
        },
        "requestContext": {
            "accountId": "952977564466",
            "apiId": "a7zp3gtd03",
            "domainName": "a7zp3gtd03.execute-api.us-west-2.amazonaws.com",
            "domainPrefix": "a7zp3gtd03",
            "http": {
                "method": "OPTIONS",
                "path": "/",
                "protocol": "HTTP/1.1",
                "sourceIp": "50.47.153.27",
                "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
            },
            "requestId": "BGelNiT9PHcEMQA=",
            "routeKey": "ANY /",
            "stage": "$default",
            "time": "11/Nov/2024:21:31:38 +0000",
            "timeEpoch": 1731360698521
        },
        "isBase64Encoded": False
    }

def test_lambda_handler_post(apigwPOST_event):
    """Test for POST request to Lambda function"""
    ret = app.lambda_handler(apigwPOST_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"].startswith("Updated total visits:")


def test_lambda_handler_get(apigwGET_event):
    """Test for GET request to Lambda function"""
    ret = app.lambda_handler(apigwGET_event, "")

    assert ret["statusCode"] == 200
    assert "TotalVisits" in ret["body"]

def test_lambda_handler_options(apigwOPTIONS_event):
    """Test for OPTIONS request to Lambda function"""
    ret = app.lambda_handler(apigwOPTIONS_event, "")

    assert ret["statusCode"] == 200
    assert "Access-Control-Allow-Origin" in ret["headers"]
    assert "Access-Control-Allow-Methods" in ret["headers"]
    assert "Access-Control-Allow-Headers" in ret["headers"]
    assert "OPTIONS,POST,GET" in ret["headers"]["Access-Control-Allow-Methods"]
    assert "*" in ret["headers"]["Access-Control-Allow-Origin"]
