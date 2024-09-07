# ManimEdu: Animações Didáticas para Matemática com Manim uma lib Python

---
Este repositório contém uma coleção de animações criadas usando a biblioteca [Manim](https://github.com/3b1b/manim), com o objetivo de produzir materiais didáticos digitais para serem utilizados em sala de aula e compartilhados online de forma a auxiliar o trabalho dos professores inserindo novas tecnologias no ensino de matemática.  

## 📚 Propósito do Projeto

O objetivo deste projeto é criar recursos visuais que auxiliem no ensino de conceitos complexos de forma clara e atraente para os alunos do ensino médio. Através dessas animações, pretendemos tornar o aprendizado mais dinâmico e acessível.

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para criar as animações.
- **Manim**: Biblioteca Python para animações matemáticas.
- **GitHub**: Plataforma para hospedagem e compartilhamento de código.

## 🎯 Como Usar

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd nome-do-repositorio
    ```

3. Instale as dependências necessárias:
   Linux:
    ```bash
    pip install manim
    ```
    Windows/MacOS:
    Consulte na documentação oficial do [Manim Community v0.18.1](https://docs.manim.community/en/stable/installation.html)
    
5. Execute as animações:
    ```bash
    manim -pql nome_da_animacao.py (o comando -p tem a função de abrir o seu player de mídia. Caso queira rodar em alta 1080p e 60fps troque -pql para -pqh)
    ```

## 📂 Estrutura do Repositório

```plaintext
/
├── AnimationsManim/              # Pasta Principal
│   ├── nome_da_animacao.py  # Código fonte das animações
│   └── ...
├── media/
     ├── videos/  # Aqui será armazenado todos os vídeos que foram renderizados no diretório principal
          ├── exemplo_pasta # ONDE ESTÃO AS ANIMAÇÕES Cada animaçao terá uma pasta exclusiva e contará com subpastas separadas pela qualidade do vídeo renderizado 
     ├── Tex/ #Dentro dessa pasta se encontram os códigos LaTeX usado nas animações. !!!!Não alterar!!!!        
├── README.md                # Este arquivo
└── ...                      # As demais pastas nesse repositório são necessárias para carregar as libs
```

## 📚 CATÁLOGO 

```plaintext
IdentidadeTrigonometricaFundamental.py - Animação que demonstra a identidade trigonométrica fundamental utilizando teorema de pitágoras.
TVM_mobile.py - Teorema do Valor Médio configurado para ser renderizado no formato mobile para rells,tiktok e etc.


SenoDomimg.py - Domínio e Imagem 
SenoInversa.py - Função Inversa 
SenoSimetria.py - A simetria da função 
SenoReciproca.py - A função reciproca 
SenoConcavidade.py - A concavidade da função 
SenoCortesEixos.py - Em quais pontos a função corta nos eixos
SenoPeriodicidade.py - Periodicidade da função


CosDomimg.py - Domínio e Imagem 
CosInversa.py - Função Inversa 
CosSimetria.py - A simetria da função 
CosReciproca.py - A função reciproca 
CosConcavidade.py - A concavidade da função 
CosCortesEixos.py - Em quais pontos a função corta nos eixos
CosPeriodicidade.py - Periodicidade da função

TgDomimg.py - Domínio e Imagem 
TgInversa.py - Função Inversa 
TgSimetria.py - A simetria da função 
TgReciproca.py - A função reciproca 
TgConcavidade.py - A concavidade da função 
TgCortesEixos.py - Em quais pontos a função corta nos eixos
TgPeriodicidade.py - Periodicidade da função
```



## 🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
