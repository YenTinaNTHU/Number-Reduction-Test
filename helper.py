import csv
import random

def get_problem_set(max, size):
    l = list(range(0, max))
    random.shuffle(l)
    return(l[0:size])

## open csv file
topics = []
answers = []
with open('./nrtProblems.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        topics.append(row[0])
        answers.append(row[2])
topics.remove('topic')
answers.remove('answer')

## constants
TOTAL_PROBLEM_NUM = len(topics)
TRAIN_PROBLEM_NUM = 10
BLOCK_SIZE = 30
PRE_BLOCK_NUM = 2
POST_BLOCK_NUM = 6