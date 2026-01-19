# Portfolio Website with CI/CD Automation

This project is a personal portfolio web application built using **Flask**, integrated with **Selenium automation** and a **Jenkins CI/CD pipeline**. The goal of this project is to demonstrate real-world automation testing and continuous integration practices by ensuring that deployments happen only when automated tests pass successfully.

---

## 🚀 Project Overview

The application serves a portfolio website showcasing profile details, skills, and projects. Automated UI tests are written using Selenium and PyTest to validate that the application loads correctly and displays expected content. A Jenkins pipeline is configured to automatically trigger on code changes, execute the test suite, and block deployment if any test fails.

This setup mimics production-level CI/CD workflows used in real software teams.

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Selenium WebDriver**
- **PyTest**
- **Jenkins**
- **HTML / CSS**
- **Git & GitHub**

---

## 📂 Project Structure

Portfolio/
│
├── app/
│ ├── app.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ ├── css/
│ ├── js/
│ └── img/
│
├── tests/
│ ├── pages/
│ ├── test_home.py
│ └── conftest.py
│
├── requirements.txt
├── Jenkinsfile
└── README.md


---

## ⚙️ CI/CD Pipeline Flow

1. Code is pushed to the GitHub repository  
2. Jenkins automatically triggers the pipeline  
3. Dependencies are installed  
4. Flask application is started  
5. Selenium automation tests are executed  
6. **If tests pass** → Deployment is approved  
7. **If tests fail** → Pipeline stops and deployment is blocked  

---

## 🧪 Automated Testing

- UI tests are written using Selenium and PyTest
- Tests validate page loading and key content visibility
- Test failures immediately stop the pipeline

---

## 🏁 How to Run Locally

```bash
pip install -r requirements.txt
python app/app.py
