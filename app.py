# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load cleaned data
@st.cache_data
def load_data():
    df = pd.read_csv("metadata_clean.csv")
    return df

df = load_data()

# App title
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Year range filter
years = st.slider("Select year range",
                  int(df['year'].min()),
                  int(df['year'].max()),
                  (2020, 2021))

df_filtered = df[(df['year'] >= years[0]) & (df['year'] <= years[1])]

# Show sample data
st.subheader("Sample Data")
st.write(df_filtered[['title','authors','journal','publish_time']].head())

# Publications per year
st.subheader("Publications by Year")
year_counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = df_filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax)
st.pyplot(fig)

# Word cloud
st.subheader("Word Cloud of Titles")
titles = " ".join(df_filtered['title'].dropna().tolist())
wc = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
