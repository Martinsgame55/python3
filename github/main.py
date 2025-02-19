pocetVstupenek = int(input("zadejte počet vstupenek"))
cena = 0

for i in range(pocetVstupenek):
    vek = int(input("Zadejte váš věk: "))
    if vek <= 6:
        print("-1x dítě do 6 let(0 eur)")   
    elif vek > 6 and vek <= 17:
        print("-1x student(10 eur)")
        cena += 10
    elif vek > 17 and vek <= 64:
        print("-1x dospělí(20 eur)")
        cena += 20
    elif vek > 65:
        print("-1x senior(25 eur)")
        cena += 25

    print("celková cena je:" ,cena)

        
