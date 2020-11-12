import json
import boto3

params = {
     'region' : 'us-east-1',
     'database' : 'giflistdb',
     'bucket' : 'gif-list-database-3b8cb02a',
     'path'  : 'queries',
     'query': 'SELECT * FROM "giflistdb"."users" limit 30;'
    }

def lambda_handler(event, context):
    client = boto3.client('athena')
    response_query_execution_id = client.start_query_execution(
        QueryString = params['query'],
        QueryExecutionContext = {
            'Database' : params['database']
        },
        ResultConfiguration = {
            'OutputLocation': 's3://' + params['bucket'] + '/' + params['path']
        }
    )
    response_get_query_details = client.get_query_execution(
        QueryExecutionId = response_query_execution_id['QueryExecutionId']
    )

    print(response_get_query_details)
    return {
        'statusCode': 200,
        'response': str(response_get_query_details)
    }