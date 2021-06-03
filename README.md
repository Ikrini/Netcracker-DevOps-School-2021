# <img src="http://www.pipelinepub.com/1011/OSS_BSS/info/NetCracker_480x240-3.gif"  align="right" width="500" height="225">
# Netcracker-DevOps-school-2021 


## ⭐ _TASK_ ⭐ 
 - _As part of the training group, create a project with a complete deployment workflow._
 - _For this task, our team wrote a telegram bot with the ability to learn in the process of conducting a dialogue with it_
 
 **_A little about telegram bots:_**
 
 <image src="https://3dnews.ru/assets/external/illustrations/2021/02/26/1033659/1.jpg" align="right" width="300" height="130">
 
- Telegram is about freedom and openness – our code is open for everyone, as is our API. Today we’re making another step towards openness by launching a Bot API and platform for third-party developers to [create bots.](https://core.telegram.org/bots)
- Contact bot: ```@netcrakerChatBot```
 
 ### _What are we using_:
- 🐳   **Docker**   🐳 
<img src="https://miro.medium.com/max/1000/1*E8IgOSkMTpBRs0w0-Zsx2g.gif" align="right" width="300" height="120">

- Python version 3.7
 
 1. - _Create Dockerfile_ 
 2. - _Create docker-compose file_
 3. - _Build and push container_
 
 - ☁️    **GOOGLE CLOUD PLATFORM**   ☁️  
 
 <img src="https://cdn.dribbble.com/users/57858/screenshots/2292590/jeshie_dribbble_cloud.gif" align="right" width="300" height="180">
 
```diff 
Google Cloud Platform (GCP), offered by Google, is a suite of cloud computing
services that runs on the same infrastructure  that Google uses internally for
its end-user  products, such as Google Search, Gmail, file storage, and YouTube.
Alongside a set of management tools, it provides a series of modular cloud 
services including computing,  data storage,data analytics and machine learning.
Registration requires a credit card or bank account details. Google Cloud
Platform provides infrastructure as a service, platform as a service, and 
serverless computing environments.
```
 - To get started, you need to install [Cloud SDK](https://cloud.google.com/sdk/docs/quickstart):
 
1.
   
   Add the Cloud SDK distribution URI as a package source:
 ```console
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
 ```
   2. Make sure you have apt-transport-https installed:
 ```console
    sudo apt-get install apt-transport-https ca-certificates gnupg
  ```
   _Note_: If your distribution does not support the signed-by option run this command instead:
 ```console
    echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
 ```
   3. Import the Google Cloud public key:
 ```console
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
  ```
 _Note_: If your distribution does not support the signed-by option run this command instead:
 ```console
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
 ```
   4. Update and install the Cloud SDK:
 
 ```console
    sudo apt-get update && sudo apt-get install google-cloud-sdk
  ```
   5. For additional ```apt-get``` options, such as disabling prompts or dry runs, refer to the [apt-get man pages](https://linux.die.net/man/8/apt-get).
Docker Tip: If installing the Cloud SDK inside a Docker image, use a single RUN step instead:
  ```console
    RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y
 ```
   6. Run ```gcloud init``` to get started
 ```console
 gcloud init
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
Cloud Run takes any container images and pairs great with the container ecosystem: 
Cloud Build,Artifact Registry, Docker. ... Integration with Cloud Code and Cloud
Build for continuous deployments. Fully managed. No infrastructure to manage: once
deployed, Cloud Run manages your services so you can sleep well.
```

2. - _Deploy our docker container in `CLOUR RUN`_

```console
gcloud run deploy --image  gcr.io/netcracker-devops/telebot23
```











