import random, time
import pyinputplus as pyip

numOfQuestions = 10
correctAnswers = 0

for i in range(numOfQuestions):
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)

    prompt = f"{num1} x {num2} = "
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1*num2)],
                      blockRegexes=[('.*', 'Incorrect')],
                      timeout=8,
                      limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)
    print(f'Score {correctAnswers}/{numOfQuestions}')

