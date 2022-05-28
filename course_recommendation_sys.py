# -*- coding: utf-8 -*-
"""course recommendation sys.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QeRLbFHTyqv06YtOHNqN_VLTCIR2g9bX
"""

import pandas as pd
!pip install neattext
import neattext.functions as nfx

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel

df = pd.read_csv("udemy_courses.csv")
df.head()

df['course_title']

dir(nfx)

df['clean_course_title'] = df['course_title'].apply(nfx.remove_stopwords)
df['clean_course_title'] = df['clean_course_title'].apply(nfx.remove_special_characters)

df[['course_title', 'clean_course_title']]

count_vec = CountVectorizer()
cv_mat = count_vec.fit_transform(df['clean_course_title'])

cv_mat

cv_mat.todense()

df_cv_words = pd.DataFrame(cv_mat.todense(), columns = count_vec.get_feature_names())

df_cv_words.head()

cosine_sim_mat = cosine_similarity(cv_mat)

cosine_sim_mat

import seaborn as sns
sns.heatmap(cosine_sim_mat[0:10], annot = True)

df.head()

course_indices = pd.Series(df.index, index = df['course_title']).drop_duplicates()

course_indices

course_indices['How To Maximize Your Profits Trading Options']

idx = course_indices['How To Maximize Your Profits Trading Options']

idx

scores = list(enumerate(cosine_sim_mat[idx]))

scores

sorted_score = sorted(scores, key = lambda x:x[1], reverse=True)

sorted_score[1:]

selected_course_indices = [i[0] for i in sorted_score[1:]]

selected_course_indices

selected_course_scores = [i[1] for i in sorted_score[1:]]

selected_course_scores

recommended_result = df['course_title'].iloc[selected_course_indices]

rec_df = pd.DataFrame(recommended_result)

rec_df.head()

rec_df['similarity_scores'] = selected_course_scores

rec_df

def recommend_course(title,num_of_rec=10):
    # ID for title
    idx = course_indices[title]
    # Course Indice
    # Search inside cosine_sim_mat
    scores = list(enumerate(cosine_sim_mat[idx]))
    # Scores
    # Sort Scores
    sorted_scores = sorted(scores,key=lambda x:x[1],reverse=True)
    # Recomm
    selected_course_indices = [i[0] for i in sorted_scores[1:]]
    selected_course_scores = [i[1] for i in sorted_scores[1:]]
    result = df['course_title'].iloc[selected_course_indices]
    rec_df = pd.DataFrame(result)
    rec_df['similarity_scores'] = selected_course_scores
    return rec_df.head(num_of_rec)

recommend_course('Trading Stock Chart Patterns For Immediate, Explosive Gains') #the qoutes can be changed into any course in the udemy databse
