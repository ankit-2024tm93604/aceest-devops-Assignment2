# 🏋️ ACEest Functional Fitness System (v3.2.4)

## 📌 Overview

ACEest is a fitness and gym management system developed using Flask and enhanced through a complete DevOps pipeline. The project demonstrates real-world software development practices including version control, testing, containerization, CI/CD, and deployment.

---

## 🚀 Version

**Current Version:** v3.2.4 (Final DevOps Integrated System)

---

## 🧬 Version History

* v1.0 – Initial GUI prototype (Tkinter)
* v1.1 – Enhanced GUI with user input
* v2.2.4 – Stable backend with Flask and testing
* v3.2.4 – Full DevOps pipeline (Final)

---

## 🛠️ Tech Stack

* Python (Flask)
* Git & GitHub
* Docker
* GitHub Actions
* Jenkins
* Kubernetes
* Postman
* Pytest

---

## 🟢 Features

* Client management via REST API
* Dynamic fitness plans
* Automated testing using Pytest
* Docker-based containerization
* CI/CD pipeline automation
* Jenkins build validation
* Kubernetes deployment support

---

## ⚙️ Local Setup

```bash
git clone https://github.com/ankit-2024tm93604/aceest-devops.git
cd aceest-devops
pip install -r requirements.txt
python app.py
```

Access:
http://localhost:5000

---

## 🧪 Testing

```bash
pytest
```

---

## 🐳 Docker

```bash
docker build -t aceest-app .
docker run -p 5000:5000 aceest-app
```

---

## 🔄 CI/CD (GitHub Actions)

* Triggered on push
* Runs tests
* Builds Docker image

---

## 🏗️ Jenkins

* Pulls code from GitHub
* Executes:

  * pip install
  * pytest

---

## ☸️ Kubernetes

```bash
kubectl apply -f k8s/
kubectl port-forward service/aceest-service 5000:80
```

---

## 📸 Screenshots

Available in `/screenshots` folder.

---

## 🗄️ Database Note

The database (`aceest.db`) is created dynamically at runtime and may initially be empty.

---
## Execution in Official VM

The project was successfully executed inside the OSHA evaluation VM 
running Rocky Linux XFCE.

Steps performed:
- Cloned project from GitHub
- Installed dependencies
- Ran Flask application
- Executed automated tests using Pytest

## 🎯 Conclusion

This project demonstrates a complete DevOps lifecycle from development to deployment using industry-standard tools.
The application was executed in the official Rocky Linux VM provided in the OSHA portal.

---

## 👨‍💻 Author

Ankit Adarsha Behera
