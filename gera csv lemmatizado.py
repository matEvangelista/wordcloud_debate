import spacy
import csv
from nltk.tokenize import word_tokenize
from collections import Counter


nlp = spacy.load('pt_core_news_sm')

nomes = ['ciro', 'felipe', 'jair', 'lula', 'simone', 'soraya']
palavras = ['' for i in range(len(nomes))]
frequencia = []

for nome in nomes:
    with open('frequencia/{}.csv'.format(nome), 'r', encoding='utf-8') as arq:
        leitor = csv.reader(arq)
        frequencia.append(list(leitor)[1:])  # elimando header

i = 0
for candidato in frequencia:
    for freq in candidato:
        palavras[i] += '{} '.format(freq[0]) * int(freq[1])
    i += 1

doc_candidatos = [nlp(palavras[i]) for i in range(len(nomes))]
fala_candidatos_lemmatizado = []
for doc in doc_candidatos:
    fala_candidatos_lemmatizado.append(
        ' '.join([token.lemma_ for token in doc]))

# por algum motivo, tranformou-se "família" em "famílio". Apesar de não recomendado, aqui está uma substituição específica para o caso
# mesma coisa com "pessoa", que virou "pessoo"

for i in range(len(nomes)):
    fala_candidatos_lemmatizado[i] = fala_candidatos_lemmatizado[i].replace('famílio', 'família')
    fala_candidatos_lemmatizado[i] = fala_candidatos_lemmatizado[i].replace('pessoo', 'pessoa')

palavras_candidatos = [word_tokenize(candidato)
                       for candidato in fala_candidatos_lemmatizado]
mais_comuns = [Counter(candidato).most_common()
               for candidato in palavras_candidatos]

for i in range(len(nomes)):
    with open('frequencia lematizada/{}.csv'.format(nomes[i]), 'w', encoding='UTF8', newline='') as arq:
        escritor = csv.writer(arq)
        escritor.writerow(['palavra', 'quantidade'])
        for linha in mais_comuns[i]:
            escritor.writerow(linha)
