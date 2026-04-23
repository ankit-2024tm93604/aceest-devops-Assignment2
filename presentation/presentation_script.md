# 🎤 ACEest DevOps Project – Presentation Script

---

## 🟢 Slide 1: Title [Dev OPS Assignment 1]

* I am presenting the end-to-end CI/CD pipeline built for the ACEest Fitness & Gym application.
* The goal was to  Version Control (Git/GitHub), Containerization (Docker), and the orchestration of Continuous Integration and Continuous Delivery (CI/CD) pipelines using GitHub Actions and Jenkins.
* I had added all the required screeshot in 
Postman --> Screenshot Folder (Local & Osha Portal)

---

## 🟢 Slide 2: Objective

The main objective of this project is to implement a complete DevOps lifecycle.

This includes:

* Automating build and testing
* Ensuring reliable deployments
* Maintaining scalability and consistency

---

## 🟢 Slide 3: Tech Stack

The project uses the following technologies:

* Flask for backend development
* Docker for containerization
* GitHub Actions for CI/CD
* Jenkins for build automation
* Kubernetes for deployment

---

## 🟢 Slide 4: Architecture

The workflow starts from the developer pushing code to GitHub.

Then:

* GitHub Actions runs CI/CD pipeline
* Docker builds the container
* Jenkins performs build validation
* Kubernetes deploys the application

---

## 🟢 Slide 5: Application Overview

This is a fitness and gym management system.

It provides:

* REST APIs
* Client data handling
* Fitness and nutrition plans

---

## 🟢 Slide 6: GUI Evolution

Initially, I developed a GUI-based system.

* Version 1.0 was a basic interface
* Version 1.1 added user input and tracking

Later, I converted it into a full backend system with DevOps integration.

---

## 🟢 Slide 7: Testing

Testing is done using Pytest.

* Automated test execution
* Ensures code quality
* All test cases are passing

---

## 🟢 Slide 8: Docker

The application is containerized using Docker.

This ensures:

* Portability
* Consistent environment
* Easy deployment

---

## 🟢 Slide 9: CI/CD Pipeline

GitHub Actions is used for CI/CD.

* Triggered on every push
* Runs tests automatically
* Builds Docker image

---

## 🟢 Slide 10: Jenkins

Jenkins is used as a build server.

* Pulls code from GitHub
* Runs installation and testing
* Acts as a quality gate

---

## 🟢 Slide 11: Kubernetes

The application is deployed using Kubernetes.

* Deployment and service created
* Application exposed using NodePort
* Port-forward used for local access

---

## 🟢 Slide 12: Results

* All tests passed successfully
* CI/CD pipeline working
* Application deployed successfully

---
## 🟢 Slide 13: Execution in OSHA VM

The application was executed inside the official OSHA virtual machine provided for evaluation.
The VM environment runs Rocky Linux with the XFCE desktop interface.

Within the VM, the project repository was cloned from GitHub and all required dependencies were installed.
The Flask application was then started successfully and verified through the local browser.

This confirms that the project can run correctly within the official evaluation environment.

---

## 🟢 Slide 14: Application Testing

Automated testing was implemented using the Pytest framework.

The test cases validate the functionality of the backend application and ensure that the API behaves as expected.
All tests were executed successfully, confirming that the application operates correctly and reliably.

---

## 🟢 Slide 15: DevOps Workflow Verification

The project demonstrates a complete DevOps workflow using multiple industry-standard tools.

Source code is managed using Git and GitHub.
Continuous integration is performed through GitHub Actions.
Jenkins is used for build validation, Docker provides containerization, and Kubernetes enables application deployment and orchestration.

Together, these tools create an automated and reliable development-to-deployment pipeline.


## 🟢 Slide 16: Conclusion

In conclusion:

* A complete DevOps pipeline is implemented
* Automation improves reliability
* The system is scalable and production-ready
* The application was executed in the official Rocky Linux VM   provided in the OSHA portal.


