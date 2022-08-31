import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

nomes = ['ciro', 'felipe', 'jair', 'lula', 'simone', 'soraya']

frequencia = []
# lista precisa ser criada com 6 elementos
palavras = ['' for i in range(len(nomes))]

for nome in nomes:
    with open('frequencia/{}.csv'.format(nome), 'r', encoding='utf-8') as arq:
        leitor = csv.reader(arq)
        frequencia.append(list(leitor)[1:]) # elimando header

i = 0
for candidato in frequencia:
    for freq in candidato:
        palavras[i] += '{} '.format(freq[0]) * int(freq[1])
    i += 1

i = 0
for candidato in palavras:
    wordcloud = WordCloud(collocations=False, width=1000, height=800, background_color='white').generate(candidato)
    wordcloud.to_file('wordcloud simples/{}.png'.format(nomes[i]))
    i += 1
