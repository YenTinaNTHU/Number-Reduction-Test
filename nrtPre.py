from helper import *
from nrtRecorder import *

name = str(input('name? '))
age = int(input('age? '))
gender = str(input('gender?(male/female) '))

recorder = NrtRecorder(name, age, gender)
timer = TimeRecorder()
id = recorder.get_subject_id()
print(f'Hi, {name}! Your ID is {id}, please fill it in the form')
recorder.create_file()
recorder.write_subject_data()

time = 0.0
isCorrect = False
userAns = 0
## TODO: Record the correct rate


## training
print('---------- start training ----------')
problemSet = get_problem_set(max=TOTAL_PROBLEM_NUM, size=TRAIN_PROBLEM_NUM)
for i in range(TRAIN_PROBLEM_NUM):
    input('<press enter key to continue>')
    print(f'Q{i+1}:{topics[problemSet[i]]}')
    recorder.set_on_question('train', 1, i+1, problemSet[i])
    timer.start_timer()
    userAns = input(f'A{i+1}:')
    time = timer.stop_timer()
    print(time)
    if(userAns == answers[problemSet[i]]):
        isCorrect = True
        print('correct!')
    else:
        isCorrect = False
        print('incorrect!')
    recorder.set_on_answer(userAns, isCorrect, time)
    recorder.write_file()
print('---------- finish training ----------')
input('<press enter key to continue>')
print('>>>>>>>>>> pre-measurement start')
## before test (2 blocks)
for i in range(PRE_BLOCK_NUM):
    print(f'---------- start block{i+1} ----------')
    problemSet = get_problem_set(max=TOTAL_PROBLEM_NUM, size=BLOCK_SIZE)
    for j in range(BLOCK_SIZE):
        input('<press enter key to continue>')
        print(f'Q{j+1}:{topics[problemSet[j]]}')
        recorder.set_on_question('pre', i+1, j+1, problemSet[j])
        timer.start_timer()
        userAns = input(f'A{j+1}:')
        time = timer.stop_timer()
        if(userAns == answers[problemSet[j]]):
            isCorrect = True
            print('correct!')
        else:
            isCorrect = False
            print('incorrect!')
        recorder.set_on_answer(userAns, isCorrect, time)
        recorder.write_file()
    print(f'---------- finish block{i+1} ----------')

input('<press enter key to continue>')
print('>>>>>>>>>> pre-measurement end')