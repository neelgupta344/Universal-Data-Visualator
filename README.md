# 📊 Universal Data Visualizer

A professional and interactive **cloud-hosted data visualization dashboard** built using **Python, Streamlit, Pandas, and Plotly**.

Universal Data Visualizer allows users to upload CSV datasets or load datasets from URLs and automatically generate interactive visualizations and statistical insights without writing any code.

The application is **deployed on Amazon EC2 using Ubuntu Linux** and runs as a Streamlit web application.

---

## 🚀 Live Deployment

The application is deployed on:

**Amazon EC2**

### Deployment Stack

```text
User
  ↓
Internet
  ↓
AWS EC2
  ↓
Ubuntu Linux
  ↓
Python Virtual Environment
  ↓
Streamlit
  ↓
Universal Data Visualizer
```

---

## 🚀 Features

* Upload any CSV file
* Load datasets from URLs
* Automatic data type detection
* Interactive visualizations
* Dataset preview
* Statistical summary
* Correlation heatmap generation
* Dynamic column detection
* Numeric and categorical data identification
* Interactive Plotly charts
* Responsive dashboard layout
* Real-time data exploration

---

## 📈 Supported Visualizations

The application currently supports:

* Line Chart
* Bar Chart
* Scatter Plot
* Histogram
* Box Plot
* Pie Chart
* Correlation Heatmap

---

## 🛠️ Technologies Used

### Programming & Frameworks

* Python
* Streamlit
* Pandas
* Plotly Express

### Cloud & Deployment

* Amazon EC2
* Ubuntu Linux
* AWS VPC
* AWS Security Groups
* Git
* GitHub
* systemd

---

## ☁️ AWS Deployment

The application has been deployed on an **Amazon EC2 Ubuntu Linux instance**.

### AWS Architecture

```text
                    USER
                      │
                      ▼
                  Internet
                      │
                      ▼
                AWS EC2 Instance
                      │
                Ubuntu Linux
                      │
             Python Virtual Env
                      │
                   systemd
                      │
                  Streamlit
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
       Pandas                  Plotly
          │                       │
          └───────────┬───────────┘
                      ▼
           Universal Data Visualizer
```

### EC2 Configuration

* Operating System: Ubuntu Linux
* Application Framework: Streamlit
* Application Port: `8501`
* Process Manager: systemd
* Version Control: Git/GitHub

### Security Group

The EC2 Security Group is configured to allow the required application and administration traffic:

| Protocol | Port | Purpose                      |
| -------- | ---: | ---------------------------- |
| SSH      |   22 | Remote server administration |
| TCP      | 8501 | Streamlit web application    |

SSH access should preferably be restricted to the administrator's IP address.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/neelgupta344/Universal-Data-Visualator.git
```

Navigate to the project directory:

```bash
cd Universal-Data-Visualator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Ubuntu/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

## ☁️ AWS EC2 Deployment Process

The application was deployed on AWS EC2 using the following process:

1. Launch an Ubuntu EC2 instance.
2. Configure the EC2 Security Group.
3. Connect to the server using SSH.
4. Install Python, pip, Git, and virtual environment tools.
5. Clone the GitHub repository.
6. Create a Python virtual environment.
7. Install project dependencies.
8. Configure Streamlit to listen on port `8501`.
9. Run and test the application.
10. Configure a systemd service.
11. Enable automatic application startup.
12. Verify the deployed application through the EC2 public address.

---

## 🔄 Automatic Application Startup

The Streamlit application is configured as a **systemd service** on Ubuntu Linux.

This allows the application to start automatically when the EC2 instance boots.

The deployment workflow is:

```text
EC2 Instance Starts
        ↓
      systemd
        ↓
streamlit.service
        ↓
Python Virtual Environment
        ↓
Streamlit Application
        ↓
Universal Data Visualizer
```

The service can be managed using:

```bash
sudo systemctl start streamlit
```

Check the service status:

```bash
sudo systemctl status streamlit
```

Enable automatic startup:

```bash
sudo systemctl enable streamlit
```

---

## 📂 Project Structure

```text
Universal-Data-Visualizer/
│
├── app.py
├── requirements.txt
├── README.md
├── sample_data.csv
├── .gitignore
│
├── architecture/
│   └── aws-architecture.png
│
├── deployment/
│   └── streamlit.service
│
└── screenshots/
    ├── dashboard.png
    ├── data-upload.png
    ├── visualization.png
    └── aws-ec2.png
```

---

## 📊 How to Use

1. Open the Universal Data Visualizer application.
2. Upload a CSV file or provide a CSV URL.
3. Preview the dataset.
4. Review the statistical summary.
5. Select the required visualization.
6. Select the required columns.
7. Customize the visualization.
8. Analyze the generated charts and insights.

---

## ✨ Key Features

### Dynamic Data Processing

The application automatically detects and processes different types of columns, including numeric and categorical data.

### Interactive Visualizations

Plotly is used to create interactive charts that allow users to explore their data dynamically.

### Dataset Analysis

Users can preview their datasets and examine statistical information before generating visualizations.

### Correlation Analysis

The application can generate a correlation heatmap to help identify relationships between numerical variables.

### Cloud Deployment

The application is hosted on Amazon EC2 and can be accessed remotely through a web browser.

---

## 📸 Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Data Upload

![Data Upload](screenshots/data-upload.png)

### Data Visualization

![Visualization](screenshots/visualization.png)

### AWS EC2 Deployment

![AWS EC2](screenshots/aws-ec2.png)

---

## 🔮 Future Enhancements

* Machine Learning integration
* Dashboard export to PDF
* Advanced filtering options
* Time-series forecasting
* Data cleaning utilities
* AI-generated insights
* AWS S3 integration for dataset storage
* HTTPS configuration
* Custom domain
* AWS CloudWatch monitoring
* CI/CD deployment using GitHub Actions or AWS services
* Docker containerization

---

## 🎯 Project Highlights

* Developed an interactive data visualization dashboard using Python and Streamlit.
* Implemented CSV upload and URL-based dataset loading.
* Used Pandas for data processing and analysis.
* Created interactive visualizations using Plotly.
* Implemented automatic data type detection.
* Deployed the application on Amazon EC2.
* Configured an Ubuntu Linux server for cloud application hosting.
* Configured AWS Security Groups for application access.
* Used systemd for automatic application startup and service management.
* Managed the source code using Git and GitHub.

---

## 👨‍💻 Author

**Neel Gupta**

BCA Student | Python Developer | Cloud & Data Analytics Enthusiast

### GitHub

https://github.com/neelgupta344



---

## 📄 License

This project is licensed under the **MIT License**.
