# aws-labs-ecs-microservices

## Step 1
### Create ECR Repository
- Go to ECR Console
- Create Repo for all docker images. I created 5 repos in this case for my 5 simple APIs created using Python Flask and can be found in `./apis/` folder.
- Build all APIs to docker images using following cmd.
  - login to AWS ECR
    ~~~
    aws ecr get-login-password --region <Region> | docker login --username AWS --password-stdin <AccountId>.dkr.ecr.ap-southeast-1.amazonaws.com
    ~~~
~~~
# docker build -t country-capital-api .
~~~
