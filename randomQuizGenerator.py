#! python3
""" Creates quizzes with questions and answers in random order, along with an answer key"""

import random

capitals = {'Andhra Pradesh':'Amravati',
            'Arunachal Pradesh':'Itanagar',
            'Assam':'Dispur',
            'Bihar':'Patna',
            'Chhatisgarh':'Naya Raipur',
            'Goa':'Panaji',
            'Gujarat':'Gandhinagar',
            'Haryana':'Chandigarh',
            'Himachal Pradesh':'Shimla',
            'Jharkhand':'Ranchi',
            'Karnataka':'Bengaluru',
            'Kerala':'Thiruvanathapuram',
            'Madhya Pradesh':'Bhopal',
            'Maharashtra':'Mumbai',
            'Manipur':'Imphal',
            'Meghalaya':'Shillong',
            'Mizoram':'Aizwal',
            'Nagaland':'Kohima',
            'Odisha':'Bhubaneswar',
            'Punjab':'Chandigarh',
            'Rajasthan':'Jaipur',
            'Sikkim':'Gangtok',
            'Tamil Nadu':'Chennai',
            'Telangana':'Hyderabad',
            'Tripura':'Agartala',
            'Uttar Pradesh':'Lucknow',
            'Uttarakhand':'Dehradun',
            'West Bengal': 'Kolkata'}

for quizNum in range(35):
    quizFile = open(f'capitalsQuiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsQuiz_answers{quizNum + 1}.txt', 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(len(states)):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}. {answerOptions[i]}\n")
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}")
    quizFile.close()
    answerKeyFile.close()
