# -*- coding: utf-8 -*-
"""Utility module for generating curl command examples for API endpoints."""


def generate_curl_example(endpoint_context, api_name, schema_names):
    """
    Generate a curl command example for an API endpoint.
    
    Args:
        endpoint_context: The endpoint context object containing action, url, params, etc.
        api_name: The name of the API (e.g., 'User', 'Order')
        schema_names: List of schema names like ['User', 'UserCreate', 'UserUpdate']
        
    Returns:
        A string containing the curl command example
    """
    action = endpoint_context.action.upper()
    url = endpoint_context.url
    params = endpoint_context.params
    
    # Build the curl command
    curl_parts = ['curl']
    
    # Add HTTP method if not GET
    if action != 'GET':
        curl_parts.append(f'-X {action}')
    
    # Separate params by location (Path, Query, Body)
    path_params = {}
    query_params = {}
    body_params = {}
    
    for param_name, param in params.items():
        param_type = param.type
        # Determine if param is in body (schema type), path (in URL), or query
        if param_type in schema_names:
            # This is a body parameter
            body_params[param_name] = param
        elif f'{{{param_name}}}' in url:
            # This is a path parameter
            path_params[param_name] = param
        else:
            # This is a query parameter
            query_params[param_name] = param
    
    # Build URL with path parameters replaced
    example_url = url
    for param_name, param in path_params.items():
        example_value = _get_example_value(param)
        example_url = example_url.replace(f'{{{param_name}}}', str(example_value))
    
    # Add query parameters
    if query_params:
        query_string_parts = []
        for param_name, param in query_params.items():
            example_value = _get_example_value(param)
            query_string_parts.append(f'{param_name}={example_value}')
        example_url += '?' + '&'.join(query_string_parts)
    
    # Add the URL
    curl_parts.append(f'"http://localhost:8000{example_url}"')
    
    # Add body if present
    if body_params:
        curl_parts.append('-H "Content-Type: application/json"')
        # Generate a simple example body
        body_example = _generate_body_example(body_params, api_name)
        curl_parts.append(f"-d '{body_example}'")
    
    return ' \\\n  '.join(curl_parts)


def _get_example_value(param):
    """Generate an example value for a parameter based on its type."""
    param_type = param.type
    
    # If there's an enum, use the first value
    if param.enum and len(param.enum) > 0:
        return param.enum[0]
    
    # Generate example based on type
    if param_type == 'int':
        return '1'
    elif param_type == 'str':
        if 'id' in param.name.lower():
            return '1'
        return f'example_{param.name}'
    elif param_type == 'bool':
        return 'true'
    elif param_type in ['date', 'datetime']:
        return '2024-01-01'
    elif param_type == 'time':
        return '12:00:00'
    elif param_type == 'float':
        return '1.0'
    else:
        # Default for unknown types
        return 'value'


def _generate_body_example(body_params, api_name):
    """Generate a JSON body example for POST/PUT requests."""
    # For schema types, generate a simple example
    body_parts = []
    for param_name, param in body_params.items():
        # Assuming the body parameter is a schema type
        # Generate a simple placeholder
        body_parts.append(f'"field1": "value1", "field2": "value2"')
        break  # Usually there's only one body parameter
    
    return '{' + ', '.join(body_parts) + '}'
