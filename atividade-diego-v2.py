kmPorLitroAlcohol = float(input('quantos km o seu automovel faz por litro de alcoll: '))
kmPorLitroGasoline = float(input('quantos km o seu automovel faz por litro de gasolina: '))
PricePerAlcoholLiter = float(input('quanto custa o litro de alcol: '))
PricePerGasolineLiter = float(input('quanto custa o litro de gasosa: '))
if kmPorLitroAlcohol and kmPorLitroGasoline and PricePerAlcoholLiter and PricePerGasolineLiter > 0:
    if kmPorLitroAlcohol/kmPorLitroGasoline >= PricePerAlcoholLiter/PricePerGasolineLiter:
        print(f'O Alcool está tendo um melhor custo benefício em relação a gasolina')
    else:
        print(f'A gasolina está tendo um melhor custo beneficio em relação ao Alcool')
else: 
    while kmPorLitroAlcohol or kmPorLitroGasoline or PricePerAlcoholLiter or PricePerGasolineLiter <= 0:
        print('insira valores validos2')
        kmPorLitroAlcohol = float(input('quantos km o seu automovel faz por litro de alcoll: '))
        kmPorLitroGasoline = float(input('quantos km o seu automovel faz por litro de gasolina: '))
        PricePerAlcoholLiter = float(input('quanto custa o litro de alcol: '))
        PricePerGasolineLiter = float(input('quanto custa o litro de gasosa: '))
        if kmPorLitroAlcohol and kmPorLitroGasoline and PricePerAlcoholLiter and PricePerGasolineLiter > 0:
            if kmPorLitroAlcohol/kmPorLitroGasoline >= PricePerAlcoholLiter/PricePerGasolineLiter:
                print(f'A gasolina está tendo um melhor custo beneficio em relação ao Alcool')
                break
            else:
                print(f'O Alcool está tendo um melhor custo benefício em relação a gasolina')
                break
        else:
            print("erro1")
            break
    else: print("erro2")



