print ('кол-во сотрудников (до 1000)')
N=int(input())

print ('расстояние до дома')
rasstoyanie_dom = [{"сотрудник": i+1, "расстояние до дома": int(input())} for i in range(N)]

print ('тариф такси за 1 км')
tarif=[int(input()) for i in range(N)]

tarif.sort()
rasstoyanie_dom.sort(key=lambda x: x["расстояние до дома"], reverse=True)
print('')
for i in range(N):
    print('Сотрудник номер', rasstoyanie_dom[i]['сотрудник'], 'сядет в машину с тарифом', tarif[i])
    print('Стоимость поездки составит', rasstoyanie_dom[i]['расстояние до дома']*tarif[i])
    print('')