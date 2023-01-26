import boto3
import re

# Set up the client for Lambda
lambda_client = boto3.client('lambda')

# Function to check for injection attacks
def check_injection_attacks(function_name):
    try:
        response = lambda_client.get_function(FunctionName=function_name)
    except Exception as e:
        print(f'An error occurred while getting the function: {e}')
        return
    # Check for SQL injection
    if re.search(r'(SELECT|INSERT|UPDATE|DELETE|DROP|ALTER|TRUNCATE)', response['Code']['Text']):
        print(f'Possible SQL injection found in function {function_name}')
    # Check for command injection
    if re.search(r'(system|exec|eval|os\.system|os\.exec|os\.popen)', response['Code']['Text']):
        print(f'Possible command injection found in function {function_name}')

# Function to check for unauthorized access
def check_unauthorized_access(function_name):
    try:
        response = lambda_client.get_policy(FunctionName=function_name)
    except Exception as e:
        print(f'An error occurred while getting the policy: {e}')
        return
    # Check for public access
    if 'Allow' in response['Policy'] and '*' in response['Policy']['Allow']:
        print(f'Function {function_name} allows public access')

# Function to check for third-party dependencies
def check_dependencies(function_name):
    try:
        response = lambda_client.get_function(FunctionName=function_name)
    except Exception as e:
        print(f'An error occurred while getting the function: {e}')
        return
    dependencies = response['Configuration']['Environment']['Variables']
    for key, value in dependencies.items():
        if key.startswith('npm_package_dependencies_') or key.startswith('npm_package_devDependencies_'):
            dependency = key.split('_')[-1]
            if 'dependencycheck' in response['Code']['Text']:
                print(f'Third-party dependency {dependency} is out of date')
            else:
                print(f'Third-party dependency {dependency} is up-to-date')

# Test the functions
check_injection_attacks('my_lambda_function')
check_unauthorized_access('my_lambda_function')
check_dependencies('my_lambda_function')
####END###
