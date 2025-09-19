#PART 1 
# analysis.py
import pandas as pd

# Load metadata.csv into pandas
df = pd.read_csv("metadata.csv", low_memory=False)

# Inspect structure
print("Shape (rows, columns):", df.shape)
print("\nDataFrame info:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum().head(10))   # show top 10

# Basic stats for numerical columns
print("\nStatistics for numerical columns:")
print(df.describe())

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors="coerce")
df['year'] = df['publish_time'].dt.year

print("\nEarliest publication:", df['publish_time'].min())
print("Latest publication:", df['publish_time'].max())

#PART 2
# Handle missing values
df_clean = df.dropna(subset=['title', 'publish_time']).copy()

# Create derived columns
df_clean['abstract_word_count'] = df_clean['abstract'].fillna("").apply(lambda x: len(x.split()))

print("\nCleaned dataset shape:", df_clean.shape)
print("Abstract word count summary:")
print(df_clean['abstract_word_count'].describe())

# Save a cleaned version for later use in Streamlit
df_clean.to_csv("metadata_clean.csv", index=False)

#PART 3
import os
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Create folder for plots
os.makedirs("plots", exist_ok=True)

# Count papers per year
year_counts = df_clean['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.savefig("plots/publications_by_year.png")
plt.close()

# Top journals
top_journals = df_clean['journal'].value_counts().head(10)
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.savefig("plots/top_journals.png")
plt.close()

# Word cloud for paper titles
titles = " ".join(df_clean['title'].dropna().tolist())
wc = WordCloud(width=800, height=400, background_color="white").generate(titles)

plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Frequent Words in Titles")
plt.savefig("plots/wordcloud.png")
plt.close()

