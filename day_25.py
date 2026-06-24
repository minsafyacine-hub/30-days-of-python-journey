# Read the hacker_news.csv file from data directory
# Get the first five rows
# Get the last five rows
# Get the title column as pandas series
# Count the number of rows and columns
# Filter the titles which contain python
# Filter the titles which contain JavaScript
# Explore the data and make sense of it

import pandas as pd
import numpy as np
hnf = pd.read_csv('hacker_news (1).csv')
print(hnf.head())
print(hnf.tail())
title_series = hnf['title']
print(title_series)
print(hnf.shape)
titles_python = hnf[hnf['title'].str.contains('python', case=False, na=False)]
print(titles_python)
titles_javascript = hnf[hnf['title'].str.contains('javascript', case=False, na=False)]
print(hnf.describe())