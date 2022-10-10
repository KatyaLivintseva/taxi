from chislo import *  #импортируем данные из кода для перевода цифр в словесную форму
try:
    A=0
    N = int(input('Количество сотрудников (до 1000) '))

    rasstoyanie_dom = []
    for i in range(N):
        rasstoyanie_dom.append(int(input('Введите количество км до дома сотрудника ' + str(i + 1) + ': '))) #вводим км столько раз, сколько указано сотрудников
    tarif = []
    for i in range(N):
        tarif.append(int(input(str(i + 1)+" такси с тарифом за 1 км" + ': '))) #вводим стоимость такси за 1 км столько раз, сколько указано сотрудников

    taxis = []
    sum = 0
    for i in range(N):
        taxis.append(0)
    for i in range(N): #минимальному расстоянию до дома соответствует максимальный тариф
        minR = rasstoyanie_dom.index(min(rasstoyanie_dom))
        maxT = tarif.index(max(tarif))
        taxis[minR] = maxT + 1
        sum += min(rasstoyanie_dom) * max(tarif)
        rasstoyanie_dom[minR] = max(rasstoyanie_dom) + 1
        tarif[maxT] = 0
    try:
        sum<1000000
        for i in range(N):
            print('Сотрудник',str(i + 1),'сядет в такси под номером', str(taxis[i]))
        print('\nСтоимость такси составит:',(sum),'(', ch(sum), ')') #вывод полной стоимости поездки в цифровой и словесной формах
    except IndexError:
        A=1
        print('\nПолучилась большая сумма, денег не хватит. \nЧтобы заплатить за такси, сумма не должна превышать 999 999 руб.')
except ValueError:
    A=1
    print('Нужно ввести целое число')

while A==1: #появилась ошибка, то программа запрашивает данные до тех пор, пок не будет работать правильно
    try:
        A=0
        N = int(input('\nКоличество сотрудников (до 1000) '))
        rasstoyanie_dom = []
        for i in range(N):
            rasstoyanie_dom.append(int(input('Расстояние до дома сотрудника ' + str(i + 1) + ': ')))

        tarif = []
        for i in range(N):
            tarif.append(int(input(str(i + 1)+" такси с тарифом за 1 км" + ': '))) 

        taxis = []
        sum = 0
        for i in range(N):
            taxis.append(0)
        for i in range(N): 
            minR = rasstoyanie_dom.index(min(rasstoyanie_dom)) 
            maxT = tarif.index(max(tarif))
            taxis[minR] = maxT + 1
            sum += min(rasstoyanie_dom) * max(tarif)
            rasstoyanie_dom[minR] = max(rasstoyanie_dom) + 1
            tarif[maxT] = 0
        try:
            sum<1000000
            for i in range(N):
                print('Сотрудник',str(i + 1),'сядет в такси под номером', str(taxis[i]))
            print('\nСтоимость такси составит:',(sum),'(', ch(sum), ')')
        except IndexError:
            A=1
            print('\nПолучилась большая сумма, денег не хватит. \nЧтобы заплатить за такси, сумма не должна превышать 999 999 руб.')
    except ValueError:
        A=1
        print('Нужно ввести целое число')
