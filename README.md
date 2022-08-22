## SWAGGER for FAST API
http://18.216.0.26/docs

## FAST API
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features are:

·      Fast: Very high performance, on par with NodeJS and Go.

|·      Fast to code: Increase the speed to develop features by about 200% to 300%.

·      Fewer bugs: Reduce about 40% of human (developer) induced errors.

·      Intuitive: Great editor support. Completion everywhere. Less time debugging.

·      Easy: Designed to be easy to use and learn. Less time reading docs.

·      Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.

·      Robust: Get production-ready code. With automatic interactive documentation.

·      Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

# Requirements

Python 3.6+

FastAPI stands on the shoulders of giants:

·      Starlette for the web parts.

·      Pydantic for the data parts.

# Installation

 pip3 install fastapi    // For Python 3

 pip install fastapi     // For Python 2

 # We will also need an ASGI server, for production such as Uvicorn or Hypercorn.

`pip3 install uvicorn     // For Python 3

pip install uvicorn      // For Python 2
`
With that, we have FastAPI and Uvicorn installed and are ready to learn how to use them. FastAPI is the framework we will use to build our API, and Uvicorn is the server that we will use the API we build to serve requests.

# Run the First API App With Uvicorn

python3 -m uvicorn main:app --reload

## Create Docker Image

docker build -t delta-rs-api .

## Tag the Just Created Docker Image

docker tag delta-rs-api:latest <aws-account-id>.dkr.ecr.<region>.amasonaws.com/delta-api:latest

## Login to AWS ECR
aws ecr get-login-password --region <region> | docker login --username AWS --password -stdin <aws-account-id>.dkr.ecr.<region>.amazonaws.com

## Push the image to ECR (Elastic Container Registry)

docker push <aws-account-id>.dkr.ecr.us-<region>.amazonaws.com/delta-api:latest

## Deploye to ECS (Eelastic container Service)

I have done manual deployment for now, but we can do same automation as well.

Steps.

    1. Created Cluster in AWS ECS Named API
    2. Created Service in the newly creted Cluster and named API
    3. Created Task Denifitions for the Service.
    4. Tas has got public IP address enabled, so my UI can communicate to it.

### Data Base

1. Created mysql database in RDS service named delta.
2. Exposed endpoint for database on port 3306 and enabled public access
3. Adjusted security groups to allow all the tcp traffic to the database.
4. from FAST API wrote queries to access data.