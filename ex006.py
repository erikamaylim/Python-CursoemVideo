"""Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""
n = int(input('Digite um número inteiro: '))
print(f'Seu dobro é {n * 2} \nSeu triplo é {n * 3} \nSua raiz quadrada é {n ** 0.5:.2f}')
#print('Seu dobro é {} \nSeu triplo é {} \nSua raiz quadrada é {:.2f}'.format(n * 2, n * 3, n ** 0.5))
print(f'Seu dobro é {n * 2} \nSeu triplo é {n * 3} \nSua raiz quadrada é {pow(n, 0.5):.2f}')