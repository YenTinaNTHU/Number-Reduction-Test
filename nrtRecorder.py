import csv
import os
from time import perf_counter
from pathlib import Path

class TimeRecorder:
    def __init__(self):
        self.t0 = 0.0
        self.t1 = 0.0

    def start_timer(self):
        self.t0 = perf_counter()
        return
    
    def stop_timer(self):
        self.t1 = perf_counter()
        return self.t1 - self.t0
    

class NrtRecorder:
    def __init__(self, name, age, gender):
        id = 0
        with open('subjects.csv', 'r', newline='') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                id = id + 1
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.test_type = ''
        self.block = -1
        self.question_num = -1
        self.question_id = -1
        self.time = 0.0
        self.isCorrect = False
        self.ans = ''
    
    def get_from_id(self, id):
        name = ''
        age = 0
        gender = ''
        with open(f'subjects.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                if(row[0] and row[0] == id):
                    name = row[1]
                    age = row[2]
                    gender = row[3]
                    break
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender


    def set_on_question(self, test_type, block, question_num, question_id,):
        self.test_type = test_type
        self.block = block
        self.question_num = question_num
        self.question_id = question_id

    def set_on_answer(self, ans, isCorrect, time):
        self.time = time
        self.isCorrect = isCorrect
        self.ans = ans
    
    def get_subject_id(self):
        return self.id
    
    def write_subject_data(self):
        with open('subjects.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.id, self.name, self.age, self.gender])
    
    def create_file(self):
        curpath = Path().absolute()
        newpath = os.path.join(curpath, 'data')
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        filename = f'/subject{self.id}.csv'
        file = open(f'{newpath}{filename}', 'w')
        file.write('test_type, block, question_num, question_id, ans, isCorrect, time\n')
        file.close()

    def write_file(self):
        filename = f'./data/subject{self.id}.csv'
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.test_type, self.block, self.question_num, self.question_id, self.ans, self.isCorrect, self.time])