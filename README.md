# 🌱 Smart Crop Analytics System

A Django web application built for analyzing and visualizing Canadian crop data using a preloaded dataset.
The system provides insights through **interactive charts** and **dynamic filtering**.

---

# 📌 Features

## 📊 Interactive Charts (Chart.js)

* Production by Crop
* Yield Over Time
* Production by Region

## 🔍 Dynamic Filtering

* Filter by year
* Filter by region
* Search crops or regions
* Sort results

## 🗄️ Database Storage

* Uses SQLite (no external setup required)
* Data is preloaded into the database

## 📈 Data Analysis

* Aggregations using Django ORM (`Sum`, `Avg`)
* Real-time updates based on filters

---

# ❓ Key Questions and How the Charts Answer Them

This application is designed to answer specific analytical questions using visualizations.

---

## 📊 Chart 1: Production by Crop (Bar Chart)

### Questions:

* Which crops have the highest production in Canada?
* How does production compare across different crops?

### Explanation:

* Displays total production for each crop
* Taller bars represent higher production
* Helps identify dominant crops

---

## 📈 Chart 2: Yield Over Time (Line Chart)

### Questions:

* How has crop yield changed over time?
* Are there trends in agricultural productivity?

### Explanation:

* Shows average yield for each year
* X-axis = Year
* Y-axis = Yield
* Reveals trends over time

---

## 📊 Chart 3: Production by Region (Bar Chart)

### Questions:

* Which regions contribute the most to crop production?
* How does production differ between provinces?

### Explanation:

* Compares production across regions
* Helps identify high-producing areas

---

## 📋 Supporting Features (Filters & Table)

### Questions:

* What happens when filtering by year or region?
* How can users explore specific crops?

### Explanation:

* Filters refine data dynamically
* Charts update automatically
* Table displays detailed records

---

# 🛠️ Technologies Used

* Python 3.13
* Django 5.x
* SQLite
* HTML / CSS
* JavaScript
* Chart.js

---

# 📁 Project Structure

```
smart-crop-analytics/
│
├── crop_project/
│   ├── crop_project/      # Project settings
│   ├── crops/             # App (models, views, templates)
│   ├── db.sqlite3         # Database (preloaded)
│   ├── manage.py
│   ├── import_data.py     # Data import script
│
├── README.md
```

---

# ⚙️ Installation & Setup Guide

## 1. Install Python

Check version:

```bash
python --version
```

Download if needed:
https://www.python.org/downloads/

---

## 2. Clone the Repository

```bash
git clone <your-repo-url>
cd smart-crop-analytics/crop_project
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

---

## 4. Install Django

```bash
pip install django
```

---

## 5. Apply Migrations

```bash
python manage.py migrate
```

---

## 6. Run the Server

```bash
python manage.py runserver
```

---

## 🌐 Open in Browser

http://127.0.0.1:8000/

---

# 🧠 How Data Works

* Data is stored in SQLite (`db.sqlite3`)
* Originally imported from CSV using `import_data.py`
* Uses Django ORM:

  * `Sum()` for production
  * `Avg()` for yield

---

# ⚠️ Troubleshooting

## Charts not showing

Make sure Chart.js is included:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

---

## Server not starting

Make sure you are in the correct folder:

```bash
cd crop_project
python manage.py runserver
```

---

## Data not appearing

Re-run import (optional):

```bash
python manage.py shell
exec(open('import_data.py').read())
```

---

# 📄 License

Educational use only
