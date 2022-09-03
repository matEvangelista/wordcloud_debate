from cmath import exp
import csv
from tkinter.tix import Tree
from wordcloud import WordCloud

nomes = ['ciro', 'felipe', 'jair', 'lula', 'simone', 'soraya']

frequencia = []
# lista precisa ser criada com 6 elementos
palavras = ['' for i in range(len(nomes))]

lemma = False

while True:
    try:
        s_n = input(
            'Quer o gráfico lemmatizado? S para sim qualquer outra letra para não: ')
        if s_n.strip().lower() == 's':
            lemma = True
        break
    except:
        print("Digite corretamente.\n")

local = 'frequencia lematizada/' if lemma else 'frequencia/'

for nome in nomes:
    with open(local+'{}.csv'.format(nome), 'r', encoding='utf-8') as arq:
        leitor = csv.reader(arq)
        frequencia.append(dict(list(leitor)[1:]))  # eliminando header

frequencia = [{chave: int(candidato[chave])
               for chave in candidato} for candidato in frequencia]

local = 'wordcloud simples lemmatizado' if lemma else 'wordcloud simples'
for i in range(len(nomes)):
    wordcloud = WordCloud(collocations=False, width=1200, height=800,
                          background_color='white').generate_from_frequencies(frequencia[i])
    wordcloud.to_file('{}/{}.png'.format(local, nomes[i]))
    i += 1
