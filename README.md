# Chemical Equipment Parameter Visualizer  
*A Hybrid Web and Desktop Application for Data Visualization and Analytics*

---

## 📌 Project Overview

Chemical industries generate large volumes of operational data related to equipment such as pumps, reactors, heat exchangers, and compressors. Analyzing this data manually is inefficient and error-prone.

This project presents a **hybrid Web and Desktop application** that allows users to upload chemical equipment data in CSV format, analyze key parameters, visualize insights, and generate PDF reports using a **common Django REST backend**.

---

## 🧱 System Architecture

- **Backend**: Django + Django REST Framework  
- **Web Frontend**: React.js (Vite)  
- **Desktop Frontend**: PyQt5  
- **Data Processing**: Pandas  
- **Visualization**:
  - Web: Summary cards (textual distribution)
  - Desktop: Matplotlib charts
- **Database**: SQLite  
- **Reporting**: PDF generation using ReportLab  
- **Authentication**: Basic Authentication  

Both frontends consume the **same backend APIs**, ensuring consistency and reusability.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend | Django, Django REST Framework |
| Web Frontend | React.js (Vite) |
| Desktop Frontend | PyQt5 |
| Data Handling | Pandas |
| Visualization | Matplotlib |
| Database | SQLite |
| Reporting | ReportLab |
| Version Control | Git & GitHub |

---

## 📂 Project Structure