# -*- coding: utf-8 -*-
"""graphs1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AIcizkXxRszc7j4KWTfR39H3qJYKNv-J
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/content/drive/MyDrive/EDA_DPA/Features/final_df.csv")

df.head()

feature_names = ['mfcc', 'zero_features', 'rms_features', 'sc_features', 'sb_features', 'sco_features', 'poly_features']

for feature_name in feature_names:
    plt.figure(figsize=(8, 4))
    plt.plot(df[feature_name])
    plt.xlabel('Sample Index')
    plt.ylabel(f'{feature_name} Value')
    plt.title(f'Line Plot of {feature_name}')
    plt.grid(True)
    plt.show()

import plotly.express as px

# Sample data (replace with your actual data)
state_counts = df['state'].value_counts().reset_index()
state_counts.columns = ['State', 'Count']

# Create a pie chart using Plotly with hoverinfo
fig = px.pie(state_counts, names='State', values='Count', title='Distribution of Calls by State')
fig.update_traces(textposition='inside', textinfo='percent+label')

# Show the pie chart
fig.show()

import re

def label_title(row):
    # Define a list of keywords and their variations
    keywords = ['accident', 'prank', 'fake', 'date', 'Non-emerg']

    # Create a regex pattern to match any form of the keywords
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in keywords) + r')\b'

    # Check if the title contains the pattern or if false_alarm is 1
    if re.search(pattern, row.title, flags=re.IGNORECASE) or row.false_alarm == 1:
        return 'prank'
    return 'genuine'

# Apply the label_title function to create a new 'label' column
df['label'] = df.apply(label_title, axis=1)

df.isna().sum() #state, false_alarm and potential_death columns had NaN values
majority_state = df['state'].mode()[0]
df['state'].fillna(majority_state, inplace=True)
df['false_alarm'] = df.apply(lambda row: 1 if row['label'] == 'prank' else 0 if row['label'] == 'genuine' else row['false_alarm'], axis=1)

from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=1)
# Define the column to be imputed
impute_column = ["potential_death"]

# Fit and transform the imputer on the specified column
df[impute_column] = imputer.fit_transform(df[impute_column])

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame

# Find the top 10 states based on the frequency of potential_death
top_states = df['state'].value_counts().head(10).index.tolist()

# Filter the DataFrame to include only the top 10 states
filtered_df = df[df['state'].isin(top_states)]

# Create a bar plot
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
sns.countplot(data=filtered_df, x='state', hue='potential_death', order=top_states)

# Add labels and title
plt.xlabel('State')
plt.ylabel('Count of Potential Death')
plt.title('Count of Potential Death by State (Top 10)')

# Rotate x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Display the plot
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame

# Find the top 5 states based on the frequency of potential_death
top_states = df['state'].value_counts().head(5).index.tolist()

# Filter the DataFrame to include only the top 5 states
filtered_df = df[df['state'].isin(top_states)]

# Create a bar plot
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
sns.countplot(data=filtered_df, x='state', hue='potential_death')

# Add labels and title
plt.xlabel('State')
plt.ylabel('Count of Potential Death')
plt.title('Count of Potential Death by State')

# Display the plot
plt.show()

from wordcloud import WordCloud

# Assuming your text data is in a column named 'text' in the DataFrame
text_data = " ".join(df['title'])

wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis', max_words=100).generate(text_data)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Sentiment Analyzed Text')
plt.show()

