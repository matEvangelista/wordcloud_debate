# Tag cloud (ou word cloud) das palavras mais ditas pelos candidatos à presidência no primeiro debate na Band

Foram feitos dois conjuntos de imagens: uma com o texto sem alterações e outra com <i>lemmatization</i>, que coloca verbos no infinitivo e substantivos no plural

## Texto sem alterações

<figure align="center">
<figcaption align="center"><b>Ciro Gomes</b>
</figcaption>
<img src="wordcloud simples/ciro.png" width=600>
</figure>

<figure align="center">
<figcaption align="center"><b>Felipe d'Ávila</b>
</figcaption>
<img src="wordcloud simples/felipe.png" width=600>
</figure>

<figure align="center">
<figcaption align="center"><b>Jair Bolsonaro</b>
</figcaption>
<img src="wordcloud simples/jair.png" width=600>
</figure>

<figure align="center">
<figcaption align="center"><b>Lula</b>
</figcaption>
<img src="wordcloud simples/lula.png" width=600>
</figure>

<figure align="center">
<figcaption align="center"><b>Simone Tebet</b>
</figcaption>
<img src="wordcloud simples/simone.png" width=600>
</figure>

<figure align="center">
<figcaption align="center"><b>Soraya</b>
</figcaption>
<img src="wordcloud simples/soraya.png" width=600>
</figure>

## Texto <i>lemmatizado</i>
<figure align="center">
<figcaption align="center"><b>Ciro Gomes</b>
</figcaption>
<img src="wordcloud simples lemmatizado/ciro.png" width=600>
</figure>

<figure align="center">
<figcaption align="center"><b>Felipe d'Ávila</b>
</figcaption>
<img src="wordcloud simples lemmatizado/felipe.png" width=600>
</figure>

<figure align="center">
<figcaption align="center"><b>Jair Bolsonaro</b>
</figcaption>
<img src="wordcloud simples lemmatizado/jair.png" width=600>
</figure>

<figure align="center">
<figcaption align="center"><b>Lula</b>
</figcaption>
<img src="wordcloud simples lemmatizado/lula.png" width=600>
</figure>

<figure align="center">
<figcaption align="center"><b>Simone Tebet</b>
</figcaption>
<img src="wordcloud simples lemmatizado/simone.png" width=600>
</figure>

<figure align="center">
<figcaption align="center"><b>Soraya</b>
</figcaption>
<img src="wordcloud simples lemmatizado/soraya.png" width=600>
</figure>

Com a <i>lemmatização</i>, a palavra mais dita por alguns candidatos mudou. A de Bolsonaro passou a ser "mulher"; a de Soraya, "todo"


## Primeira etapa - web scraping de uma página com a transcrição
Como, <a href="https://www.poder360.com.br/eleicoes/leia-a-transcricao-do-debate-presidencial-da-band/">neste site</a>, toda a fala registrada por cada candidato começa com seu nome em negrito, selecionaram-se apenas os parágrafos que começavam com seus nomes, com o apoio do módulo Beautiful Soup 4. Depois, os parágrafos lidos foram salvos em arquivos .txt.

Esta etapa pertence ao arquivo `scraper.py`

## Segunda etapa - frequência absoluta de cada palavra por candidato
O programa `gera csv.py` e `gera csv lemmatizado.py` lêem os arquivos .txt, contam a frequência das palavras utilizadas em cada arquivo e salva-as em arquivos csv, na forma `palavra, quantidade`. Há pastas indicando quais foram <i>lematizados</i> ou não.

## Terceira etapa - leitura dos arquivos .csv e WordCloud
Esta estapa é feita por `gerador de imagens.py`. São lidas as palavras e quantidades dos arquivos .csv e, a partir deles, através do módulo wordcloud, obtiveram-se as imagens.