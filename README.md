# 📊 CORD-19 Data Explorer  

A simple data analysis and visualization project using the **CORD-19 dataset** (COVID-19 research papers).  
This project demonstrates the **end-to-end data science workflow**: data loading, cleaning, analysis, visualization, and building a basic **Streamlit web app**.

---

## 🚀 Project Overview
This project explores the `metadata.csv` file from the [CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).  

## DOWNLOADING METADATA.CSV
Follow the link to download
(https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge?resource=download&select=metadata.csv)

##
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

-- From the analysis.py 
----------------------------------------------------------------------------------------
PART 1

Shape (rows, columns): (1056660, 19)

DataFrame info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1056660 entries, 0 to 1056659
Data columns (total 19 columns):
 #   Column            Non-Null Count    Dtype  
---  ------            --------------    -----  
 0   cord_uid          1056660 non-null  object 
 1   sha               373766 non-null   object 
 2   source_x          1056660 non-null  object 
 3   title             1056157 non-null  object 
 4   doi               656780 non-null   object 
 5   pmcid             389571 non-null   object 
 6   pubmed_id         498932 non-null   object 
 7   license           1056660 non-null  object 
 8   abstract          821116 non-null   object 
 9   publish_time      1054846 non-null  object 
 10  authors           1032791 non-null  object 
 11  journal           969338 non-null   object 
 12  mag_id            0 non-null        float64
 13  who_covidence_id  482935 non-null   object
 14  arxiv_id          14249 non-null    object
 15  pdf_json_files    373766 non-null   object
 16  pmc_json_files    315742 non-null   object
 17  url               686934 non-null   object
 18  s2_id             976468 non-null   float64
dtypes: float64(2), object(17)
memory usage: 153.2+ MB
None

First 5 rows:
   cord_uid  ... s2_id
0  ug7v899j  ...   NaN
1  02tnwd4m  ...   NaN
2  ejv2xln0  ...   NaN
3  2b73a28n  ...   NaN
4  9785vg6d  ...   NaN

[5 rows x 19 columns]

Missing values per column:
cord_uid             0
sha             682894
source_x             0
title              503
doi             399880
pmcid           667089
pubmed_id       557728
license              0
abstract        235544
publish_time      1814
dtype: int64

Statistics for numerical columns:
       mag_id         s2_id
count     0.0  9.764680e+05
mean      NaN  2.175871e+08
std       NaN  5.312281e+07
min       NaN  9.600000e+01
25%       NaN  2.211411e+08
50%       NaN  2.320829e+08
75%       NaN  2.373948e+08
max       NaN  2.491936e+08

Earliest publication: 1856-04-01 00:00:00
Latest publication: 2024-04-20 00:00:00

🔹 Part 2: Data Cleaning & Preparation
Handled missing values (drop/fill strategy)
Converted publication date to datetime & extracted year
Created new columns (e.g., abstract word count)

----------------------------------------------------------------------------------------------
PART 2
Cleaned dataset shape: (518429, 21)
Abstract word count summary:
count    518429.000000
mean        170.892655
std         123.346234
min           0.000000
25%          86.000000
50%         188.000000
75%         249.000000
max       18000.000000
Name: abstract_word_count, dtype: float64


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
