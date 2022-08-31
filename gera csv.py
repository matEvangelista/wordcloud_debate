from cgitb import text
import csv
from socket import PACKET_LOOPBACK
from nltk.corpus import PlaintextCorpusReader
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nomes = ['ciro', 'felipe', 'jair', 'lula', 'simone', 'soraya']
partidos = ['pl', 'psl', 'pt', 'pcdob', 'pdt', 'dem', 'psb', 'ptb',
            'mdb', 'pp', 'psc']  # apenas os que tem menos de 4 letras
nomes_proprios = ['brasil', *[nomes]]
textos_lidos = []
texto_final = []
mais_comuns = []

for i in range(len(nomes)):
    textos_lidos.append(PlaintextCorpusReader(
        'textos', nomes[i]+'.txt', encoding='utf-8'))
    texto_final.append([w.lower() for w in textos_lidos[i].words()
                        if (w.lower() not in stopwords.words('portuguese'))
                        and (w not in string.punctuation)
                        and (w.isnumeric() == False)
                        and (w.lower() not in ['boa', 'noite', 'bandeirantes', 'porque'])
                        and (len(w) > 3)
                        or w.lower() in partidos])
    texto_final[i] = [
        w.capitalize() if w in nomes_proprios else w for w in texto_final[i]]
    texto_final[i] = [
        w.upper() if w in partidos else w for w in texto_final[i]]

texto_final = [' '.join(texto) for texto in texto_final]

palavras_candidatos = [word_tokenize(texto) for texto in texto_final]
mais_comuns = [Counter(candidato).most_common()
               for candidato in palavras_candidatos]

for i in range(len(nomes)):
    with open('frequencia/{}.csv'.format(nomes[i]), 'w', encoding='UTF8', newline='') as arq:
        escritor = csv.writer(arq)
        for linha in mais_comuns[i]:
            escritor.writerow(linha)
