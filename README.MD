>> ### IF YOU ENJOY OUR REPOS, REACH OUT VIA EMAIL OR SOCIAL MEDIA FOR CUSTOMIZED SOLUTIONS 

>> ### DON'T FORGET TO RATE THIS REPO IF YOU FIND IT USEFUL!!!

<br/>

# Python Flask Simple API on Docker
This repo contains:
 - A python Flask simple API (/app) (/src)
 - A Dockerfile for running a Python application Image

This project is a Simple API using Python Flask for Docker containerization. It might be tested for GET, POST, PUT, PATCH and DELETE requests.

You might notice we have non used directories within, it is a folders structure based on our product SCA: An API builder that generates a full CRUD API with swagger definitions to map any relational database with a complete and secure AWS infrastructure. We're able to provide your project with several infrastrucutures with all the features contained within this project and other customizable resources such as: Cognito for Authentication/Authorization, WAF (Web Application Firewalls), ElastiCache (Redis or Memcached) for low latency applications and full logging capabilities powered by Cloudwatch or Centralized Logs features (S3 + Glue + Athena).
For more information, visit our page and send us an inquiry: [SevenTechnologies](https://seventechnologies.cloud/)


The steps needed to run this docker container will be explained below

## 1 - Build a Docker Image

### Requirements: 
* Have docker installed on machine

### Building the image
For running it locally you first need to build the docker image with the following command:
* docker build -t ${DOCKER_IMAGE_NAME} .

## 2 - Running it locally

### Docker Run:
The following command must be executed in order to test the docker app locally:
* docker run -p "3000:3000" ${DOCKER_IMAGE_NAME}

## 3 - Additional information about Docker
For more details about building a Dockerfile for a Python application image, you may take a look at [Docker Hub](https://hub.docker.com/_/python)

## Social Medias
* [Linkedin](https://www.linkedin.com/company/7community/)
* [Instagram-PTBR](https://www.instagram.com/7comtech/)

## Email
* sales@seventechnologies.cloud