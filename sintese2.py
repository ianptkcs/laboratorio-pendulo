import numpy as np

chave = 'mao'

# Ler dados do arquivo 'dados.txt'    
dados = np.loadtxt(f'dados/{chave}.txt')
media_total = np.mean(dados)
desvio_padrao_m_total = np.std(dados)/np.sqrt(100)

alunos = [dados[i:i+10] for i in range(0, len(dados), 20)]
media_alunos = [np.mean(aluno) for aluno in alunos]
desvio_padrao_m_alunos = [np.std(aluno)/np.sqrt(20) for aluno in alunos]


# Salvar os resultados em um arquivo txt
with open(f'tabelas/tabelas_{chave}.txt', 'w') as f:
    for i in range(len(media_alunos)):
        f.write(f'{media_alunos[i]:.3f} {desvio_padrao_m_alunos[i]:.3f}\n')
    f.write(f'{media_total:.3f} {desvio_padrao_m_total:.3f}')