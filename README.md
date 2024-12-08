# Lung Cancer Prediction Application

This repository contains a **Lung Cancer Prediction Application** built using **Machine Learning (ML)** and **Deep Learning (DL)**. The application uses a **Flask** web framework to provide a user interface for predicting lung cancer based on input data. Additionally, the project is containerized using **Docker** for ease of deployment and portability.

---

![lung](https://github.com/user-attachments/assets/1869ca6f-6bae-4cfa-b398-52bf7d00eb30)

---

## Features
- **Machine Learning & Deep Learning Models**: The application utilizes trained neural networks for lung cancer prediction.
- **Flask Web Application**: A simple and user-friendly interface for making predictions.
- **Dockerized Deployment**: The application is packaged as a Docker image for easy setup and execution.

---

## How to Use

### **Clone the Repository**
```bash
git clone https://github.com/yourusername/lung-cancer.git
cd lung-cancer
```

## Run Locally

### 1. Install Dependencies
- Make sure you have Python installed. Then install the required packages:
```bash
pip install -r requirements.txt
```

### 2. Run the Flask Application
```bash
python app.py
```
3. Open your browser and navigate to http://localhost:80.

## Run with Docker

### 1. Pull the Docker Image
The prebuilt Docker image is available on Docker Hub. Pull it using:
```bash
docker pull talha213/lung-cancer
```

### 2. Run the Docker Container
Run the application in a container:
```bash
docker run -d -p 80:80 lung-cancer
```
- The application will be accessible at http://localhost:8080.

# Docker Image Details
- Image Name: talha213/lung-cancer
- Exposed Port: 80

### Build the Image Locally (Optional)
If you prefer to build the image locally:
```bash
docker build -t lung-cancer .
```

### Run the locally built image:
```bash
docker run -d -p 80:80 lung-cancer
```

# Contributing
Feel free to contribute to this project by submitting issues or pull requests.

## **About Me**  

Hi! I'm [Talha](https://github.com/anonymous298), a passionate developer and tech enthusiast focused on building impactful projects. I specialize in **AI/ML**, and crafting efficient solutions for complex problems.  

### **Skills**  
- 🧠 Artificial Intelligence & Machine Learning  
- 💻 Web Development (Frontend & Backend)  
- 📊 Data Analysis & Visualization  

### **Connect with Me**  
- [GitHub](https://github.com/anonymous298)  
- [LinkedIn](https://linkedin.com/in/muhmmad-talha937/)
