# 🔥 Algerian Forest Fire FWI Prediction (End-to-End ML Deployment)

An end-to-end Machine Learning project that predicts the **Fire Weather Index (FWI)** using meteorological data from the Algerian Forest Fires dataset.

This project covers:

* Data preprocessing
* Feature scaling
* Model training (Ridge Regression)
* Model serialization
* Flask web application
* Production deployment (AWS Elastic Beanstalk ready)


## 📊 Dataset

**Source:**
Algerian Forest Fires Dataset (Updated CSV)
[https://www.kaggle.com/datasets/mbharti321/algerian-forest-fires-dataset-updatecsv](https://www.kaggle.com/datasets/mbharti321/algerian-forest-fires-dataset-updatecsv)

### Dataset Description

The dataset contains meteorological data from two regions of Algeria:

* Bejaia Region
* Sidi-Bel Abbes Region

### Features Used

* Temperature
* RH (Relative Humidity)
* WS (Wind Speed)
* Rain
* FFMC
* DMC
* ISI
* Classes
* Region

Target Variable:

* FWI (Fire Weather Index)
  

## 🧠 Project Workflow

### 1️⃣ Data Preprocessing

* Cleaning missing values
* Encoding categorical features
* Feature scaling using StandardScaler

### 2️⃣ Model Training

* Algorithm used: **Ridge Regression**
* Model trained on scaled data
* Performance evaluated using regression metrics

### 3️⃣ Model Serialization

* Model saved using `pickle`
* Scaler saved separately
* Loaded inside Flask application

### 4️⃣ Web Application

* Built using Flask
* Accepts user input via HTML form
* Scales input
* Returns predicted FWI value

### 5️⃣ Deployment Ready

* Configured for AWS Elastic Beanstalk
* WSGI path configured
* Gunicorn included for production server


## 🚀 Project Structure

```
algerian-forest-fire-fwi-predictor/
│
├── application.py           # Flask app entry point
├── requirements.txt         # All Python dependencies
├── models/                  # Saved ML models and scaler
│   ├── ridge.pkl
│   └── scaler.pkl
├── templates/               # HTML templates for Flask
│   ├── index.html
│   └── home.html
├── notebooks/               # Jupyter notebooks for EDA & training
│   └── fwi_model_training.ipynb
└── .ebextensions/           # AWS Elastic Beanstalk configs
    └── python.config

```

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd algerian-forest-fire-fwi-predictor
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
python application.py
```

Open in browser:

```
http://127.0.0.1:5000
```

## 🧪 Example Prediction Flow

1. Enter:

   * Temperature
   * RH
   * WS
   * Rain
   * FFMC
   * DMC
   * ISI
   * Classes
   * Region

2. Click **Predict**

3. Application:

   * Scales input
   * Feeds into trained Ridge model
   * Displays predicted FWI

## 📦 requirements.txt

```
Flask
numpy
pandas
scikit-learn
gunicorn
```

## 🌐 Deployment (AWS Elastic Beanstalk)

### WSGI Configuration

`.ebextensions/python.config`

```yaml
option_settings:
  "aws:elasticbeanstalk:container:python":
    WSGIPath: application:application
```

### Notes

* Ensure `application.py` contains:

  ```python
  application = Flask(__name__)
  app = application
  ```
* Do not include `venv/` in deployment zip
* Include `models/` folder


## 🏗 Technologies Used

* Python
* Flask
* NumPy
* Pandas
* Scikit-Learn
* Ridge Regression
* AWS Elastic Beanstalk
* Gunicorn

## 🎯 Key Learning Outcomes

* End-to-end ML pipeline
* Model serialization using pickle
* Flask web integration
* Handling form inputs safely
* Debugging template and server errors
* Production deployment setup
* WSGI configuration for AWS


## 🔮 Future Improvements

* Convert model + scaler into a single Pipeline object
* Add input validation
* Add logging
* Improve UI with Bootstrap
* Add Docker support
* Add CI/CD pipeline


## 👨‍💻 Author

**Jules Kitenge Kiayima**



## ⭐ If You Like This Project

Give it a ⭐ on GitHub and connect with me on LinkedIn!

