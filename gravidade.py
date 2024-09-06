import numpy as np
import math

chave = 'mao'
match(chave):
    case 'mao':
        flag = True
        sigma_x = 0.01
        n = 10  
    case 'bancada':
        flag = True
        sigma_x = 0.001
        n = 10
    case 'tracker':
        flag = False
        n = 1
    case 'fotodiodo':
        flag = True
        sigma_x = 0.00005
        n = 1


T, sigma_m = np.loadtxt(f'resultados/resultados_{chave}.txt')
T = T/n
if(flag):
    incerteza_x = np.sqrt(sigma_x**2 + (sigma_m)**2)
else:
    incerteza_x = sigma_m
L = 0.333
sigma_l = 0.001


g =L*(2*math.pi/T)**2
incerteza_g = np.sqrt(((2*math.pi/T)**2)*incerteza_x**2+((64*L**2*math.pi**4)/(T**6))*sigma_l**2)

print(f'{T} {incerteza_x:.6f}')
print(f'{g:.3f} {incerteza_g:.3f}')
# Save results to file
with open(f'gravidades/gravidades_{chave}.txt', 'w') as f:
    f.write(f"g: {g}\n")
    f.write(f"incerteza_g: {incerteza_g}\n")

# Optionally, you can still print the values