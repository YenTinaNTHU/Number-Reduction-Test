from helper import *
from nrtRecorder import *

recorder = NrtRecorder('',-1,'')
recorder.get_from_id(input('id? '))
print(type(recorder))
timer = TimeRecorder()

time = 0.0
isCorrect = False
userAns = 0
print('---------- post-measurement start ----------')
## after test (9 blocks)
for i in range(POST_BLOCK_NUM):
    print(f'---------- start block{i+1} ----------')
    counter = 23
    problemSet = get_problem_set(max=TOTAL_PROBLEM_NUM, size=TRAIN_PROBLEM_NUM)
    for j in range(TRAIN_PROBLEM_NUM):
        input('<press enter key to continue>')
        print(f'Q{j+1}:{topics[problemSet[j]]}')
        recorder.set_on_question('posts', i+1, j+1, problemSet[j])
        timer.start_timer()
        userAns = input(f'A{j+1}:')
        time = timer.stop_timer()
        if(userAns == answers[problemSet[j]]):
            isCorrect = True
            if(time < 10):
                counter = counter - 1
            print('correct!')
        else:
            isCorrect = False
            print('incorrect!')
        recorder.set_on_answer(userAns, isCorrect, time)
        recorder.write_file()
    print(f'---------- finish block{i+1} ----------')
    if(counter < 0):
        break

input('<press enter key to continue>')
print('---------- post-measurement end ----------')