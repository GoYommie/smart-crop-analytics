# 🌱 Smart Crop Analytics System

A Django web application built for analyzing and visualizing Canadian crop data using a preloaded dataset. The system provides insights through interactive charts and dynamic filtering.

---

# 📌 Features

##  Interactive Charts (Chart.js)

* Production by Crop
* Yield Over Time
* Production by Region

##  Dynamic Filtering

* Filter by year
* Filter by region
* Search crops or regions
* Sort results

##  Database Storage

* Uses SQLite (no external setup required)
* Data is preloaded into the database

##  Data Analysis

* Aggregations using Django ORM (`Sum`, `Avg`)
* Real-time updates based on filters

---
#  Key Questions and How the Charts Answer Them

This application is designed to answer specific analytical questions using visualizations. 
Each chart directly corresponds to a key question.

---

## 📊 Chart 1: Production by Crop (Bar Chart)

### ❓ Question:

* Which crops have the highest production in Canada?
* How does production compare across different crops?

### 📈 How the Chart Answers This:

* The bar chart displays total production for each crop.
* Taller bars represent crops with higher production levels.
* Users can quickly identify dominant crops such as wheat or canola.

---

## 📈 Chart 2: Yield Over Time (Line Chart)

### ❓ Question:

* How has crop yield changed over time?
* Are there trends or improvements in agricultural productivity?

### 📉 How the Chart Answers This:

* The line chart plots average yield for each year.
* The X-axis represents time (years), while the Y-axis shows yield.
* Upward or downward trends reveal changes in productivity over time.

---

## 🗺️ Chart 3: Production by Region (Bar Chart)

### ❓ Question:

* Which regions contribute the most to crop production?
* How does production differ between provinces?

###  How the Chart Answers This:

* The chart compares total production across regions.
* Each bar represents a province or region.
* This helps identify high-producing areas and regional differences.

---

##  Supporting Features (Filters & Table)

### ❓ Questions:

* How does production or yield change when filtering by year?
* What patterns appear when focusing on a specific region?
* How can users explore specific crops?

### How the App Answers This:

* Filters allow users to refine data dynamically.
* Charts update automatically based on selected filters.
* The table provides detailed records for deeper inspection.

---

### Summary

Each visualization in the application is designed to answer a specific analytical question, making the system not just a data display tool, but a decision-support dashboard.


#  Technologies Used

* Python 3
* Django
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
│   ├── db.sqlite3         # Database
│   ├── manage.py
│   ├── import_data.py     # Script to load data
│
├── README.md
```

---

# ⚙️ Installation & Setup Guide

## 1. Install Python

Check if Python is installed:

```bash
python --version
```

If not installed, download from:
https://www.python.org/downloads/

---

## 2. Clone or Download Project

```bash
git clone <your-repo-url>
cd smart-crop-analytics/crop_project
```

Or download the ZIP and extract it.

---

## 3. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

## 4. Install Django

```bash
pip install django
```

---

## 5. Run Migrations

```bash
python manage.py migrate
```

---

## 6. Load Data into Database

```bash
python manage.py shell
```

Then run:

```python
exec(open('import_data.py').read())
```

Exit:

```python
exit()
```

---

## 7. Start the Server

```bash
python manage.py runserver
```

---

## 🌐 8. Open in Browser

Go to:

http://127.0.0.1:8000/

---

#  How to Use the App

##  Filters

* Select Year
* Select Region
* Enter search text
* Click Filter

👉 Charts update automatically based on filters

---

## 📈 Charts

| Chart                | Description                |
| -------------------- | -------------------------- |
| Production by Crop   | Total production per crop  |
| Yield Over Time      | Average yield per year     |
| Production by Region | Total production by region |

---

##  Table

* Displays filtered crop data
* Updates dynamically

---

#  How Data Works

* Data is stored in SQLite (`db.sqlite3`)
* Imported using `import_data.py`
* Uses Django ORM:

  * `Sum()` for production
  * `Avg()` for yield

---

#  Troubleshooting

## Charts not showing

Make sure Chart.js is included:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

---

## Server not starting

Make sure you're inside the project folder:

```bash
python manage.py runserver
```

---

## Data not appearing

Re-run import:

```bash
python manage.py shell
exec(open('import_data.py').read())
```
# 📄 License

Educational use only
