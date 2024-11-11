import os
import pytest

# This fixture will be applied to all tests
@pytest.fixture(autouse=True)
def set_env_variables():
    os.environ['DYNAMODB_TABLE_NAME'] = 'cr-sam-app-Table'
    os.environ['AWS_SAM_STACK_NAME'] = 'cr-sam-app'