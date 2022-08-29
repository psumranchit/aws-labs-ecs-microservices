# aws-labs-ecs-microservices

## Step 1
### Create ECR Repository
- Go to ECR Console
- Create Repo for all docker images. I created 5 repos in this case for my 5 simple APIs using Python Flask and can be found in `./apis/` folder.
- Build and push all APIs to docker images using following cmd.

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
- Repeat the `docker build` and `docker push` step for all APIs.

## Step 2
### Provision resources with CloudFormation Stack
- The following resources will be created
  - VPC, 2 Public Subnets, IGW
  - Security Groups for ALB and EC2 Container Instances
  - Roles required for ECS, EC2
  - AutoScalingGroup for EC2 Container Instances
  - ALB and TargetGroups. Each TargetGroups for each ECS Services
  - TaskDefinitions for all API
  - Services for all API

  > TaskDefinition Name parameters provided during the CloudFormation creating **must be the same as** ECR Repositories Name created in `Step 1`
