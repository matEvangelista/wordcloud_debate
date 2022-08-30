from bs4 import BeautifulSoup
import requests as re

url = 'https://www.poder360.com.br/eleicoes/leia-a-transcricao-do-debate-presidencial-da-band/'
print("Lendo a página, isto pode demorar um pouco...")
page = re.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
paragrafos = soup.find_all('p')

jair = []
for p in paragrafos:
    if p.find('b'):
        if('Jair' in p.find('b').text):
            jair.append(' '.join(p.text.split()[2:]))

simone = []
for p in paragrafos:
    if p.find('b'):
        if('Simone' in p.find('b').text):
            simone.append(' '.join(p.text.split()[2:]))

soraya = []
for p in paragrafos:
    if p.find('b'):
        if('Soraya' in p.find('b').text):
            soraya.append(' '.join(p.text.split()[2:]))

ciro = []
for p in paragrafos:
    if p.find('b'):
        if('Ciro' in p.find('b').text):
            ciro.append(' '.join(p.text.split()[2:]))

lula = []
for p in paragrafos:
    if p.find('b'):
        if('Lula' in p.find('b').text):
            lula.append(' '.join(p.text.split()[1:]))

felipe = []
for p in paragrafos:
    if p.find('b'):
        if('Felipe' in p.find('b').text):
            felipe.append(' '.join(p.text.split()[2:]))

discursos = [jair, simone, soraya, lula, ciro, felipe]
nomes = ['jair', 'simone', 'soraya', 'lula', 'ciro', 'felipe']

for i in range(len(nomes)):
    print("Salvando o texto do candidato {}".format(nomes[i]))
    with open('textos/'+nomes[i]+'.txt', 'w', encoding='utf-8') as arq:
        for linha in discursos[i]:
            arq.write(linha)
