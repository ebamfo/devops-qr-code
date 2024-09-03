# QR Code Generator

This project is a simple yet powerful application that generates QR codes from input text. It leverages modern technologies, including Vue.js for the frontend and FastAPI for the backend, and is deployed within a Kubernetes infrastructure. The project also incorporates CI/CD pipelines using GitHub Actions to ensure the robustness of the API before deployment.

## Key Features
- **Text-to-QR Code Conversion:** Converts user-provided text into QR codes.
- **Real-time Feedback:** The QR code is generated and displayed instantly on the frontend.
- **Scalable Deployment:** The application is containerized and deployed in a Kubernetes cluster, ensuring scalability and reliability.
- **Automated Testing and Deployment:** CI/CD pipelines test and deploy the application, guaranteeing high-quality code in production.

## Technologies Used

### 1. Vue.js
Vue.js is a progressive JavaScript framework used for building the user interface of this application. It provides a reactive and component-based architecture, making the frontend dynamic and responsive.

### 2. FastAPI
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+. It’s used to develop the backend of the application, handling the logic of QR code generation and providing the API endpoints that the frontend consumes.

### 3. Kubernetes
Kubernetes is a container orchestration platform that automates the deployment, scaling, and management of containerized applications. This project uses Kubernetes to deploy and manage the entire application, ensuring it can handle varying loads and maintain high availability.

### 4. GitHub Actions
GitHub Actions is used to implement Continuous Integration and Continuous Deployment (CI/CD) pipelines. These pipelines automatically test the FastAPI endpoints and deploy the application to the Kubernetes cluster whenever changes are pushed to the repository.

## Getting Started
To get started with the project, clone the repository and follow the instructions to set up the development environment, including the necessary tools and dependencies.
