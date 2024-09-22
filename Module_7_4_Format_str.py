team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'

team1_num = 5 #Количество участников первой команды (Мастера кода)
team2_num = 6 #Количество участников второй команды (Волшебники данных)
score_1 = 40 #количество решенных задач первой командой
score_2 = 42 #количество решенных задач второй командой
team1_time = 1552.512
team2_time = 2153.31451

challenge_result = str
if score_1 > score_2:
    challenge_result = f'Победа команды {team1_name}!'
elif score_2 > score_1:
    challenge_result = f'Победа команды {team2_name}!'
else:
    challenge_result = 'Ничья!'

#Использование %:
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

# Использование Format():
print('Команда {name} решила задач: {score}!'.format(name=team2_name, score=score_2))
print('{name} решили задачи за {time} сек.!'.format(name=team2_name, time=team2_time))

#Использование f:
print(f'Команды решили {score_1} и {score_2} задач!')
print(f'Результат битвы: {challenge_result.lower()}')
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {(team1_time + team2_time)//(score_1 + score_2)}'
      f' секунды на задачу!')
