# aws-labs-ecs-microservices

## Step 1
### Create ECR Repository
- Go to ECR Console
- Create Repo for all docker images. I created 5 repos in this case for my 5 simple APIs using Python Flask and can be found in `./apis/` folder.
- Build all APIs to docker images using following cmd.

  - Login to AWS ECR
  ~~~
  aws ecr get-login-password --region <Region> | docker login --username AWS --password-stdin <AccountId>.dkr.ecr.<Region>.amazonaws.com
  ~~~
  - Build docker image
  ~~~
  docker build -t <AccountId>.dkr.ecr.<Region>.amazonaws.com/<api-name>:latest .
  ~~~
  - Push image to ECR repos
  ~~~
  docker push <AccountId>.dkr.ecr.<Region>.amazonaws.com/<api-name>:latest
  ~~~
- Repeat the step for all APIs.
