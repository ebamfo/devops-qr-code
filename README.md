# QR Code Generator

This project is an application that generates QR codes from input text. It leverages technologies, including Vue.js for the frontend and FastAPI for the backend. This is deployed within Azure Kubernetes Service working in conjunction with other Azure servers and Terraform to deploy Azure infrastructure. The project also incorporates CI/CD pipelines using GitHub Actions to ensure the robustness of the API before deployment and also streamline kubernetes infrastructure changes.

## Key Features
- **Text-to-QR Code Conversion:** Converts user-provided text into QR codes.
- **Real-time Feedback:** The QR code is generated and displayed instantly on the frontend.
- **Scalable Deployment:** The application is containerized and deployed in a Kubernetes cluster, ensuring scalability and reliability.
- **Automated Testing and Deployment:** CI/CD pipelines test and deploy the application, guaranteeing high-quality code in production.

## Technologies Used

**1. Vue.js** 

The front-end is developed using VueJS.

**2. FastAPI** 

The API is developed using FastAPI. It receives a GET function with 2 parameters ie **url**(URL to be converted) and **dateTime**(Current time is hhmmss to name image). It stores the QR code in Azure Blob Storage and returns a url to access it.

**3. Kubernetes** 

The web-ui and API are deployed as pods in a deployment set in Azure Kubernetes Services. Loadbalalancer services are created for the web-ui and API. SecretProviderClass is used to pass connection string of Azure Blob Storage into API pod during deployment

**4. Terraform** 

Terraform is used as the IaC tool to deploy and manage Microsoft Azure services. 

**5. Microsoft Azure-** 

Microsoft Azure is used for the cloud deployments. Microsoft Azure tools used include Azure Kubernetes Service, Azure Key Vault and Azure Blob Storage

**5. GitHub Actions**

Five CI/CD Pipelines which carry out the following 4 main tasks;
- Test and Deploy changes made to API
- Deploy changes made to front end
- Deploy changes made to kubernetes manifest files
- Start the Azure Kubernetes Cluster at 7:50 AM UTC and Stopping at 6:00 PM UTC everyday
