"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

p = float(input('Digite seu peso em quilos: '))
h = float(input('Digite sua altura em metros: '))
imc = p / (h * h) # Ou imc = p / (h ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f} e você está ABAIXO do peso ideal.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f} e você está no seu PESO IDEAL.')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f} e você está com SOBREPESO.')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f} e você está com OBESIDADE.')
else:
    print(f'Seu IMC é {imc:.1f} e você está com OBESIDADE MÓRBIDA.')
