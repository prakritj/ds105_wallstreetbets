import pickle
import pandas as pd
import textstat
import statistics as st
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
import numpy as np
import matplotlib.pyplot as plt

comments = pickle.load(open('WSB_Comments.pickle', 'rb'))
comments

pd.set_option("display.max_columns", None)
print(comments.body)
print(comments.body[0])
print("\n")
print(comments.body[0][:])

reading_grades = []

for i in range(0,len(comments)):
    comment_body = comments.body[i][:]


    comment_reading_grade = textstat.flesch_kincaid_grade(comment_body)
    reading_grades.append(comment_reading_grade)
    if i % 1000 == 0:
        print(i)

comments.insert(4,"Reading Level",reading_grades)
pd.set_option('display.max_rows', 50)
print(comments)
# comments.to_pickle('comments_reading_level.pickle')
# comments.to_csv(r'comments_reading_level.csv', mode = 'w')
reading_level_average = st.mean(reading_grades)


print("Average Flesch-Kincaid Reading Level of WSB comments: Grade ", round(reading_level_average,2))


max = 0
min = 0
for i in range (0,len(reading_grades)):
    if reading_grades[i] > max:
        max = reading_grades[i]
    if reading_grades[i] < min:
        min = reading_grades[i]



read_level_array = np.array(reading_grades)
print('Mean: ' + str(np.mean(read_level_array)))
print('Median: ' + str(np.median(read_level_array)))
print('Max: ' + str(max))
print('Min: ' + str(min))
plt.hist(read_level_array, bins=np.arange(-5, 25, 1), log=False, histtype='bar')
plt.title('Distribution of Reading Level')
plt.xlabel('Reading Level')
plt.ylabel('Number of comments')
plt.show()

