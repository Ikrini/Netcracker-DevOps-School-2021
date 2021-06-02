# <img src="http://www.pipelinepub.com/1011/OSS_BSS/info/NetCracker_480x240-3.gif"  align="right" width="500" height="225">
# Netcracker-DevOps-school-2021 


## ⭐ _TASK_ ⭐ 
 - _As part of the training group, create a project with a complete deployment workflow._
 - _For this task, our team wrote a telegram bot with the ability to learn in the process of conducting a dialogue with it_
 
 
 ### _What are we using_:
- 🐳   **Docker**   🐳 
<img src="https://miro.medium.com/max/1000/1*E8IgOSkMTpBRs0w0-Zsx2g.gif" align="right" width="300" height="120">

 1. - _Create Dockerfile_ 
 2. - _Create docker-compose file_
 3. - _Build and push container_
 
 - ☁️    **GOOGLE CLOUD PLATFORM**   ☁️  
 
 <img src="https://cdn.dribbble.com/users/57858/screenshots/2292590/jeshie_dribbble_cloud.gif" align="right" width="300" height="180">
 
```diff 
Google Cloud Platform (GCP), offered by Google, is a suite of cloud computing services
that runs on the same infrastructure  that Google uses internally  for its end-user 
products, such as Google Search, Gmail, file storage, and YouTube.  Alongside a set of
management tools, it provides a series of modular cloud services including computing, 
data storage,data analytics and machine learning. Registration requires a credit card 
or bank account details. Google Cloud Platform provides infrastructure as a service, 
platform as a service, and serverless computing environments.
```


<img src="https://docs.signalfx.com/en/latest/_images/integration_googlecontainerengine.png" align="right" width="280" heigth="200" >

- ☁️    🐳 **Google Container Registry** 🐳   ☁️ 

```diff
Container Registry is a private container image registry that runs on Google Cloud.

This quickstart shows you how to:

- Configure Docker for authentication to Container Registry
- Tag and push an image to your registry
- Pull the image from your registry
```

1. - _Push docker container in `Google Container Registry (GCR)`_

First you need to enable GCR in console and next steps:
```console
docker tag gcr.io/netcracker-devops/telebot23

docker push gcr.io/netcracker-devops/telebot23
```

This quickstart focuses on integration with Docker. For general information about integration with other Google Cloud services, see [Using Container Registry with Google Cloud](https://cloud.google.com/container-registry/docs/using-with-google-cloud-platform)

<img src="https://seeklogo.com/images/G/google-cloud-run-logo-895F1305FF-seeklogo.com.png" align="right" width="240" heigth="200" >

- ☁️ 🏃   **GOOGLE CLOUD RUN**   🏃 ☁️ 

```diff
Cloud Run takes any container images and pairs great with the container ecosystem: Cloud Build,
Artifact Registry, Docker. ... Integration with Cloud Code and Cloud Build for continuous 
deployments. Fully managed. No infrastructure to manage: once deployed, Cloud Run manages your
services so you can sleep well.
```

2. - _Deploy our docker container in `CLOUR RUN`_

```console
gcloud run deploy --image  gcr.io/netcracker-devops/telebot23
```











