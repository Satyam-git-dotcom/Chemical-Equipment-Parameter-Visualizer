# 🧪Chemical Equipment Parameter Visualizer  
Hybrid Web and Desktop Application for Data Visualization and Analytics

---

## 📌Project Overview

The Chemical Equipment Parameter Visualizer is a hybrid application designed to analyze and visualize operational data of chemical equipment such as pumps, reactors, valves, and heat exchangers. Users can upload a CSV file containing equipment parameters, and the system processes the data to generate analytical insights. The application is accessible through both a Web Dashboard and a Desktop Application, powered by a common Django REST backend.

---

## 🏗️System Architecture

React Web Application and PyQt5 Desktop Application both communicate with a centralized Django REST API. The backend performs data parsing, analytics, history management, and PDF report generation, ensuring consistent results across platforms.
React Web Application ───┐
├── Django REST API ─── SQLite Database
PyQt5 Desktop Application ─┘

---

## 🛠️Technology Stack

Backend: Django, Django REST Framework  
Web Frontend: React.js (Vite), Chart.js  
Desktop Frontend: PyQt5, Matplotlib  
Data Processing: Pandas  
Database: SQLite  
Reporting: ReportLab (PDF Generation)  
Authentication: Basic Authentication  
Version Control: Git and GitHub  

---

## 📁Project Structure

Chemical-Equipment-Parameter-Visualizer  
--backend  
--frontend-web  
--frontend-desktop  
--sample_equipment_data.csv  
--README.md  

---

## ⚙️Backend Setup Instructions

Navigate to the backend directory and execute the following commands:

cd backend  
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
python3 manage.py migrate  
python3 manage.py createsuperuser  
python3 manage.py runserver  

The backend server runs at:  
http://127.0.0.1:8000/

---

## 🌐Web Frontend Setup Instructions

Navigate to the web frontend directory and run:

cd frontend-web/chemical-equipment-frontend  
npm install  
npm run dev  

The web application runs at:  
http://localhost:5173/

---

## 🖥️Desktop Application Setup Instructions

Navigate to the desktop application directory and run:

cd frontend-desktop  
python3 main.py  

The desktop application connects to the same Django REST API.

---

## ✨Features Implemented

CSV Upload:  
Users can upload CSV files from both the Web and Desktop applications. The backend processes the file using Pandas.

Data Summary API:  
The backend returns total equipment count, average flowrate, average pressure, average temperature, and equipment type distribution.

Web Dashboard:  
The web application provides a modern analytics dashboard with tab-based navigation for Analytics and History. It includes dark and light mode, interactive charts using Chart.js (bar chart, pie chart, and line chart), and chart export functionality.

Desktop Visualization:  
The desktop application uses Matplotlib to visualize equipment distribution and analytics.

History Management:  
The system stores the last five uploaded datasets along with their summaries. Users can view upload history, reload analytics by selecting a previous dataset, and download PDF reports for each dataset.

PDF Report Generation:  
The backend generates PDF reports containing summary statistics and equipment distribution using ReportLab.

Authentication:  
Basic authentication is implemented to secure API endpoints.

---

## 📄Sample CSV Format

Equipment Name,Type,Flowrate,Pressure,Temperature  
Pump A,Pump,120,5,80  
Reactor B,Reactor,200,10,150  
Valve C,Valve,90,4,60  
Heat Exchanger D,Exchanger,180,8,120  

A sample file named sample_equipment_data.csv is included for testing and demonstration.

---

## 🌐Deployment (Optional)

The web frontend can be deployed using Netlify (free tier). The backend and desktop application are intended to run locally during demonstrations. This approach is suitable for academic and FOSSEE project submissions.

---

## 🎥Demo Video

A short demo video (2–3 minutes) demonstrates CSV upload, analytics dashboard, interactive charts, history management, PDF report generation, and the desktop application workflow.

---

## 🎓Academic Note

This project demonstrates hybrid application development, REST API integration, data analytics using Pandas, interactive data visualization, UI/UX enhancement, and proper version control practices.

---

## ✅Conclusion

The Chemical Equipment Parameter Visualizer is a complete hybrid solution for analyzing chemical equipment data through both web and desktop platforms. The project fulfills all specified requirements and is ready for academic and FOSSEE submission.
