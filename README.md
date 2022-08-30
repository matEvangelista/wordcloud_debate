# Tag cloud (ou word cloud) das palavras mais ditas pelos candidatos à presidência no primeiro debate na Band

<figure align="center">
<figcaption align="center"><b>Ciro Gomes</b>
</figcaption>
<img src="wordcloud simples/ciro.png" width=300>
</figure>

<figure align="center">
<figcaption align="center"><b>Felipe d'Ávila</b>
</figcaption>
<img src="wordcloud simples/felipe.png" width=300>
</figure>

<figure align="center">
<figcaption align="center"><b>Jair Bolsonaro</b>
</figcaption>
<img src="wordcloud simples/jair.png" width=300>
</figure>

<figure align="center">
<figcaption align="center"><b>Lula</b>
</figcaption>
<img src="wordcloud simples/lula.png" width=300>
</figure>

<figure align="center">
<figcaption align="center"><b>Simone Tebet</b>
</figcaption>
<img src="wordcloud simples/simone.png" width=300>
</figure>

<figure align="center">
<figcaption align="center"><b>Soraya</b>
</figcaption>
<img src="wordcloud simples/soraya.png" width=300>
</figure>


# Primeira etapa - web scraping de uma página com a transcrição
Como, <a href="https://www.poder360.com.br/eleicoes/leia-a-transcricao-do-debate-presidencial-da-band/">neste site</a>, toda a fala registrada por cada candidato começa com seu nome em negrito, selecionaram-se apenas os parágrafos que começavam com seus nomes, com o apoio do módulo Beautiful Soup 4. Depois, os parágrafos lidos foram salvos em arquivos .txt.

Esta etapa pertence ao arquivo `scraper.txt`

# Segunda etapa - frequência absoluta de cada palavra por candidato
O programa `gera csv.py` lê os arquivos .txt, conta a frequência das palavras utilizadas em cada arquivo e salva-as em um arquivo csv, na forma `palavra, quantidade`.

# Terceira etapa - leitura dos arquivos .csv e WordCloud
Esta estapa é feita por `gerador de imagens.py`. São lidas as palavras e quantidades dos arquivos .csv e, a partir deles, através do módulo wordcloud, obtiveram-se as imagens.