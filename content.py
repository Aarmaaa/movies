import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("final.csv")
df = df[df["soup"].notna()]

count = CountVectorizer(stop_words="english")
count_matrix = count.fit_transform(df["soup"])

cosin = cosine_similarity(count_matrix, count_matrix)

df = df.reset_index()
indices = pd.Series(df.index, index = df["title"])

def get_recommendations(title, consin):
  idx = indices[title]
  sim_scores = list(enumerate(consin[idx]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse = True)
  sim_scores = sim_scores[1:11]
  movies_indices = [i[0] for i in sim_scores]
  return df[["title", "vote_count", "vote_average", "posterlink"]].iloc[movies_indices].values().tolist()