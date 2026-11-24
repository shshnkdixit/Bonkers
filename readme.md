# BONKERS – Python Web App on Azure

A Python-based web application deployed on **Microsoft Azure App Service**. BONKERS is a modern footwear storefront demo featuring a clean interface, product listings, and a shopping-cart interaction.

## 🚀 Live Demo

**Website:** https://bonkers-cxdjh3gkb3ekhghs.centralindia-01.azurewebsites.net

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Flask
- **Web Server:** Gunicorn
- **Cloud Platform:** Microsoft Azure
- **Hosting Service:** Azure App Service (Linux)

## ✨ Features

- Modern footwear storefront interface
- Product listings with images
- Product search and filtering
- Add-to-cart interaction
- Responsive web interface

## 📁 Project Structure

```text
BONKERS/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Run Locally

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd BONKERS
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

4. Open in your browser:

```text
http://127.0.0.1:5000
```

## ☁️ Azure Deployment

The application is hosted using Microsoft Azure App Service.

Deployment configuration:

- **Publish:** Code
- **Operating System:** Linux
- **Runtime:** Python
- **Region:** Central India
- **Web App:** bonkers

**Startup Command:**

```bash
gunicorn --bind=0.0.0.0 --timeout 600 app:app
```

## 🎯 Objective

To understand Python web application hosting, runtime configuration, cloud deployment, and public accessibility using Azure App Service.

## 👨‍💻 Author

**Shashank Dixit**

B.Tech – Computer Science Engineering (AI & ML)

GitHub: [shshnkdixit](https://github.com/shshnkdixit)

---

⭐ If you find this project useful, consider giving the repository a star!