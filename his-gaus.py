import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

chave = 'fotodiodo'
# Ler dados do arquivo 'dados.txt'
# Simulando dados como exemplo, substitua pela leitura real
dados = np.loadtxt('dados/'+chave+'.txt')  # Use o arquivo real aqui

# Criar o histograma das medidas usando frequência absoluta
contagens, bins, _ = plt.hist(dados, bins=15, density=False, alpha=0.6, color='w', edgecolor='black', label='frequência exp.')

# Ajustar a curva gaussiana aos dados
media, desvio_padrao = norm.fit(dados)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

# Calcular a curva Gaussiana normalizada pela área total das contagens
p = norm.pdf(x, media, desvio_padrao) * np.diff(bins).mean() * len(dados)

# Plotar a curva gaussiana
plt.plot(x, p, 'k', linewidth=2, label='gaussiana')

# Personalizar o gráfico
plt.title('Histograma - Fotodiodo')
plt.xlabel('$T$ (s)', style='italic')
plt.ylabel('frequência')
plt.legend()

plt.show()
