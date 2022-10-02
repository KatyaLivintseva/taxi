R=['рубль', 'рубля', 'рублей']

print ('Количество сотрудников (до 1000)')
N=int(input())

print ('Расстояние до дома')
rasstoyanie_dom = [{"сотрудник": i+1, "расстояние до дома": int(input())} for i in range(N)]

print ('Тариф такси за 1 км')
tarif=[int(input()) for i in range(N)]

if ((tarif%10)==0): 
    rub=R[2]  
if ((tarif%10)==1): 
    rub=R[0]
if (1<(tarif%10)<5): 
    rub=R[1]
if (4<(tarif%10)<10):                
    rub=R[2]

tarif.sort()
rasstoyanie_dom.sort(key=lambda x: x["расстояние до дома"], reverse=True)
print('')
for i in range(N):
    print('Сотрудник номер', rasstoyanie_dom[i]['сотрудник'], 'сядет в машину с тарифом', tarif[i], rub)
    print('Стоимость поездки составит', rasstoyanie_dom[i]['расстояние до дома']*tarif[i], rub)
    print('')
