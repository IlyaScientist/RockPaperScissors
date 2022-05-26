from random import randint

wins = 0
loses = 0 

def exit():
    num = 0
    with open('session.txt', 'r') as g:
        for line in g:
            num = int(line) + 1
                
        print('Сессия игр номер', num, 'была окончена')

    with open('session.txt', 'w') as g:
        g.write(str(num))

def score(wins, loses):

    with open('WL.txt', 'r') as g:
        for line in g:
            if line.startswith('win'):
                win = line
                win = int(win[4:5:]) + wins
                print('Всего побед:', win)

            if line.startswith('los'):
                lose = line
                lose = int(lose[5:6:]) + loses
                print('Всего проигрышей:', lose)

    with open('WL.txt', 'w') as g:
        g.write('win=' + str(win) + '\nlose=' + str(lose))
        
while True:
    try:
        a = int(input('0 - Выход\n1 - Камень\n2 - Ножницы\n3 - Бумага\n> '))
        if a == 0:
            exit(); score(wins, loses)
            break
        else:
            rand_num = randint(1,3)

            if a is rand_num:
                print('Ничья, противник выбрал то же что и вы')

            if a is 1:
                if rand_num == 2:
                    print('Вы победили! У противника были ножницы')
                    wins += 1
                elif rand_num == 3:
                    print('Вы проиграли! У противника была бумага')
                    loses += 1

            elif a is 2:
                if rand_num == 1:
                    print('Вы проиграли! У противника был камень')
                    loses += 1
                elif rand_num == 3:
                    print('Вы победили! У противника была бумага')
                    wins += 1

            elif a is 3:
                if rand_num == 2:
                    print('Вы проиграли! У противника были ножницы')
                    loses += 1
                if rand_num == 1:
                    print('Вы победили! У противника был камень')
                    wins += 1
                    
            else:
                print('Под этим числом ничего нет')
            
    except ValueError:
        print('Напиши число дебил')