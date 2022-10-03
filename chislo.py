def ch(tarif):
    A=['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    B=['одна', 'две', 'три', 'четыре', 'пять','шесть', 'семь', 'восемь', 'девять']
    O=['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    C=['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят','восемьдесят', 'девяносто']
    D=['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот','девятьсот']
    E=['тысяча', 'тысячи', 'тысяч']
    R=['рубль', 'рубля', 'рублей']

    stots=D[(tarif//100000)-1]
    if ((tarif//100000)==0):
        stots=''
        
    dts=C[(tarif%100000//10000)-1]
    if ((tarif%100000//10000)==0):
        dts=''
        
    ts=B[(tarif%10000//1000)-1]
    if ((tarif%10000//1000)==0):
        ts=''
        
    sto=D[(tarif%1000//100)-1]
    if ((tarif%1000//100)==0):
        sto=''
        
    ds=C[(tarif%100//10)-1]
    if ((tarif%100//10)==0):
        ds=''
        
    odin=A[(tarif%10)-1]
    if ((tarif%10)==0):
        odin=''

    if ((tarif%10000//1000)==0): 
        tsa=E[2]
    if ((tarif%10000//1000)==1): 
        tsa=E[0]
    if (1<(tarif%10000//1000)<5): 
        tsa=E[1]
    if (4<(tarif%10000//1000)<10): 
        tsa=E[2]
    if (10<(tarif//1000)<20):
        tsa=E[2]
    if (10<(tarif//1000)<20):
        tsa=E[0]
    if (10<(tarif//1000%100)<20):
        tsaa=E[2]
        
    if ((tarif%10)==0): 
        rub=R[2]  
    if ((tarif%10)==1): 
        rub=R[0]
    if (1<(tarif%10)<5): 
        rub=R[1]
    if (4<(tarif%10)<10):                
        rub=R[2]

    if (tarif==1):
        result = A[0]+' '+R[0]
    if (tarif==10):
        result = C[0]+' '+R[2]
    if (1<tarif<5):
        result = A[tarif-1]+' '+R[1]
    if (4<tarif<10):
        result = A[tarif-1]+' '+R[2]
    if (10<tarif<20):
        result = O[(tarif%10)-1]+' '+R[2]
    if (10<(tarif%100)<20):
        rub=R[2]

    if (99999<tarif<1000000): #100 000 -> 999 999
        if ((10<(tarif%100)<20) and (10<(tarif//1000%100)<20)):
            result = stots+' '+O[(tarif//1000%100%10)-1]+' '+tsaa+' '+sto+' '+O[(tarif%10)-1]+' '+rub
        else:
            if (10<(tarif%100)<20):
                result = stots+' '+dts+' '+ts+' '+tsa+' '+sto+' '+O[(tarif%10)-1]+' '+rub
            else:
                if (10<(tarif//1000%100)<20): 
                    result = stots+' '+O[(tarif//1000%100%10)-1]+' '+tsaa+' '+sto+' '+ds+' '+odin+' '+rub
                
                else:
                    if ((tarif//100000)==0 or (tarif%100000//10000)==0 or(tarif%10000//1000)==0 or (tarif%1000//100)==0 or (tarif%100//10)==0 or (tarif%10)==0):
                        result = stots+' '+dts+' '+ts+' '+tsa+' '+sto+' '+ds+' '+odin+' '+rub
                    else:
                        result = stots+' '+dts+' '+ts+' '+tsa+' '+sto+' '+ds+' '+odin+' '+rub
                
    if (9999<tarif<100000): #10 000 -> 99 999
        if ((10<(tarif//1000)<20) and (10<(tarif%100)<20)):
            result = O[(tarif//1000%10)-1]+' '+tsaa+' '+sto+' '+O[(tarif%100%10)-1]+' '+rub
        else:
            if (10<(tarif//1000)<20):
                result = O[(tarif//1000%10)-1]+' '+tsaa+' '+sto+' '+ds+' '+odin+' '+rub
            else:
                if (10<(tarif%100)<20):
                    result = dts+' '+ts+' '+tsa+' '+sto+' '+O[(tarif%100%10)-1]+' '+rub
                else:
                    if ((tarif%100000//10000)==0 or(tarif%10000//1000)==0 or (tarif%1000//100)==0 or (tarif%100//10)==0 or (tarif%10)==0):
                        result = dts+' '+ts+' '+tsa+' '+sto+' '+ds+' '+odin+' '+rub
                    else:
                        result = dts+' '+ts+' '+tsa+' '+sto+' '+ds+' '+odin+' '+rub

    if (999<tarif<10000): #1000 -> 9999
        if (10<(tarif%100)<20):
            result = ts+' '+tsa+' '+sto+' '+O[(tarif%10)-1]+' '+rub
        else:
            if ((tarif%10000//1000)==0 or (tarif%1000//100)==0 or (tarif%100//10)==0 or (tarif%10)==0):
                result = ts+' '+tsa+' '+sto+' '+ds+' '+odin+' '+rub
            else:
                result = ts+' '+tsa+' '+sto+' '+ds+' '+odin+' '+rub

    if (99<tarif<1000): #100 -> 999
        if (10<(tarif%100)<20):
            result = sto+' '+O[(tarif%10)-1]+' '+rub
        else:
            if ((tarif%1000//100)==0 or (tarif%100//10)==0 or (tarif%10)==0):
                result = sto+' '+ds+' '+odin+' '+rub
            else:
                result = sto+' '+ds+' '+odin+' '+rub

    if (19<tarif<100): #20 -> 99
        result = ds+' '+odin+' '+rub
    return tarif


