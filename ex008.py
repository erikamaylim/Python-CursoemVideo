"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""
d = float(input('Digite uma distância em metros: '))
#print('A distância {}m corresponde a: \n{}cm. \n{}mm. \n{}dm. \n{}km. \n{}hm. \n{}dam.'.format(d, d*100, d*1000, d*10, d*0.001, d*0.01, d*0.1))
print(f'A distância {d}m corresponde a: \n{d*0.001:}km. \n{d*0.01}hm. \n{d*0.1:.1f}dam. \n{d*10:.0f}dm. \n{d*100:.0f}cm. \n{d*1000:.0f}mm.')
