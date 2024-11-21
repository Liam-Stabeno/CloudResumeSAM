import os
import boto3
import pytest
import requests
import toml
import sys

# Add the parent directory to the module search path (as it is in test_handler.py)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def get_stack_name_from_config():
    """Retrieve the stack name from samconfig.toml"""
    try:
        # Get the absolute path to the current test file
        test_file_path = os.path.abspath(__file__)
        
        # Get the directory of the test file
        test_dir = os.path.dirname(test_file_path)
        
        # Define the relative path to samconfig.toml from the test file
        config_path = os.path.join(test_dir, "../../samconfig.toml")
        
        # Normalize the path to ensure it resolves correctly
        config_path = os.path.abspath(config_path)
        
        # Load the config file
        config = toml.load(config_path)
        
        # Extract stack name from the [default.deploy.parameters] section
        stack_name = config['default']['deploy']['parameters']['stack_name']
        
        if not stack_name:
            raise ValueError("Stack name is not specified in the samconfig.toml file.")
        
        return stack_name
    
    except Exception as e:
        raise Exception(f"Failed to retrieve stack name from samconfig.toml: {str(e)}")


class TestApiGateway:

    @pytest.fixture()
    def api_gateway_url(self):
        """ Get the API Gateway URL from CloudFormation Stack outputs """
        
        # Get the stack name from samconfig.toml
        stack_name = get_stack_name_from_config()
        
        print(f"Using stack name: {stack_name}")
        
        client = boto3.client("cloudformation", region_name='us-west-2')

        try:
            # Describe the stack using the fetched stack name
            response = client.describe_stacks(StackName=stack_name)
        except Exception as e:
            raise Exception(
                f"Cannot find stack {stack_name} \n" f'Please make sure a stack with the name "{stack_name}" exists'
            ) from e

        stacks = response["Stacks"]
        stack_outputs = stacks[0]["Outputs"]
        
        # Find the API endpoint from the outputs
        api_outputs = [output for output in stack_outputs if output["OutputKey"] == "APIEndpoint"]

        if not api_outputs:
            raise KeyError(f"APIEndpoint not found in stack {stack_name}")

        return api_outputs[0]["OutputValue"]  # Extract URL from stack outputs

    def test_api_gateway(self, api_gateway_url):
        """ Call the API Gateway endpoint and check the response """
        response = requests.get(api_gateway_url)

        # Validate the response status and body
        assert response.status_code == 200
        assert response.json().get('TotalVisits') is not None
