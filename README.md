# giflist

How to install a package into the src dir for deployment
```
 cd MyPythonLambda/
 pip install redis -t .
 zip -r MyPythonLambda.zip *
```

Deploy the contents of `src/` zipped


## API 

<url>/parameter?query-string

### Set up resources
```
PS C:\Users\dylan> aws apigateway get-resources  --rest-api-id w4d51zfknl --region us-east-1
{
    "items": [
        {
            "id": "hivf40vse7",
            "path": "/"
        }
    ]
}

PS C:\Users\dylan> aws apigateway create-resource  --rest-api-id w4d51zfknl --region us-east-1 --parent-id hivf40vse7 --path-part user
{
    "id": "8ee5zf",
    "parentId": "hivf40vse7",
    "pathPart": "user",
    "path": "/user"
}

PS C:\Users\dylan> aws apigateway create-resource  --rest-api-id w4d51zfknl --region us-east-1 --parent-id hivf40vse7 --path-part gif
{
    "id": "yp1qa0",
    "parentId": "hivf40vse7",
    "pathPart": "gif",
    "path": "/gif"
}

PS C:\Users\dylan> aws apigateway create-resource  --rest-api-id w4d51zfknl --region us-east-1 --parent-id hivf40vse7 --path-part list
{
    "id": "8knjza",
    "parentId": "hivf40vse7",
    "pathPart": "list",
    "path": "/list"
}

PS C:\Users\dylan> aws apigateway create-resource  --rest-api-id w4d51zfknl --region us-east-1 --parent-id 8ee5zf --path-part '{username}'
{
    "id": "2ctonp",
    "parentId": "8ee5zf",
    "pathPart": "{username}",
    "path": "/user/{username}"
}
```
### Setup method

```
PS C:\Users\dylan> aws apigateway put-method  --rest-api-id w4d51zfknl --region us-east-1 --resource-id 8ee5zf --http-method GET --authorization-type "NONE"
{
    "httpMethod": "GET",
    "authorizationType": "NONE",
    "apiKeyRequired": false
}

PS C:\Users\dylan> aws apigateway put-method  --rest-api-id w4d51zfknl --region us-east-1 --resource-id 2ctonp --http-method GET --authorization-type "NONE" --request-parameters method.request.path.username=true
{
    "httpMethod": "GET",
    "authorizationType": "NONE",
    "apiKeyRequired": false,
    "requestParameters": {
        "method.request.path.username": true
    }
}

```

