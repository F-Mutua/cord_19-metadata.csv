# 📊 CORD-19 Data Explorer  

A simple data analysis and visualization project using the **CORD-19 dataset** (COVID-19 research papers).  
This project demonstrates the **end-to-end data science workflow**: data loading, cleaning, analysis, visualization, and building a basic **Streamlit web app**.

---

## 🚀 Project Overview
This project explores the `metadata.csv` file from the [CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).  

We perform:  
- Data loading and exploration  
- Data cleaning and preparation  
- Analysis and visualization  
- A simple **Streamlit app** for interactive exploration  

---

## 🛠️ Tools & Libraries
- **Python 3.7+**
- [Pandas](https://pandas.pydata.org/) → Data manipulation  
- [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/) → Visualization  
- [WordCloud](https://amueller.github.io/word_cloud/) → Word cloud generation  
- [Streamlit](https://streamlit.io/) → Interactive web application  

---

## 📂 Project Structure
python_assignment/
│
├── analysis.py 
├── app.py 
├── metadata.csv
├── requirements.txt
└── README.md 



## ⚡ Setup Instructions

### 1️⃣ Clone Repository
git clone https://github.com/<your-username>/Frameworks_Assignment.git
cd Frameworks_Assignment

2️⃣ Create Virtual Environment
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Analysis
python analysis.py
This will generate plots and statistics for Parts 1–3

5️⃣ Run the Streamlit App
streamlit run app.py
Open your browser at http://localhost:8501 to interact with the app.

📊 Workflow & Results
🔹 Part 1: Data Loading & Exploration
Loaded metadata.csv into Pandas

Checked dimensions, data types, missing values

Generated summary statistics



🔹 Part 2: Data Cleaning & Preparation
Handled missing values (drop/fill strategy)
Converted publication date to datetime & extracted year
Created new columns (e.g., abstract word count)


🔹 Part 3: Analysis & Visualization
Publications by year
Top publishing journals
Word frequency in titles (WordCloud)
Source distribution
 *PHOTOS ARE UPLOADED*

🔹 Part 4: Streamlit Application
Built an interactive app with filters (year range, dropdowns)
Displayed visualizations and sample data
Enabled simple exploration of COVID-19 research papers

<img width="1207" height="676" alt="image" src="https://github.com/user-attachments/assets/c28724a2-ed81-4427-92a5-b16967df894f" />
<img width="1252" height="730" alt="image" src="https://github.com/user-attachments/assets/867de86d-81d4-4181-b7c1-2b713cf5ed7b" />
<img width="1287" height="693" alt="image" src="https://github.com/user-attachments/assets/c0a7f774-3be6-42ab-99dd-4b5d4976ef59" />
<img width="1251" height="675" alt="image" src="https://github.com/user-attachments/assets/5234ed8b-2251-4cee-870c-f00750640365" />




📝 Reflection
🔹 Challenges Faced
Large dataset size: The CORD-19 dataset is huge, so working with just the metadata.csv was necessary to keep things manageable.
Missing and inconsistent data: Many rows had missing publication dates, journals, or titles, which required careful cleaning before analysis.
Tooling setup: Getting Streamlit and WordCloud running in VS Code required troubleshooting, especially with dependencies and correct execution commands.
Visualization clarity: Choosing the right type of charts and making them readable took some iteration.

🔹What I Learned
How to load and explore real-world datasets using pandas.
Practical experience with data cleaning (handling missing values, converting dates, creating new features).
Confidence in creating visualizations with Matplotlib, Seaborn, and WordCloud.
How to build and run a Streamlit web app for sharing insights interactively.
The importance of incremental debugging — testing small parts of the code before moving to the next step saved time.



👩🏽‍💻 Author
Faith mUTUA
