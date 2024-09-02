# Animações Didáticas com Manim uma lib do Python
<details><summary> tl;dr:</summary>  To organizando as animações q to fazendo no manim em um lugar só, podem alterar, usar, vender, fazer o que quisere. Só mantenham a lib viva</details>

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
          ├── exemplo_pasta #<strong>ONDE ESTÃO AS ANIMAÇÕES</strong> Cada animaçao terá uma pasta exclusiva e contará com subpastas separadas pela qualidade do vídeo renderizado (-ql, -qm, -qh)
     ├── Tex/ #Dentro dessa pasta se encontram os códigos LaTeX usado nas animações. !!!!Não alterar!!!!        
├── README.md                # Este arquivo
└── ...                      # As demais pastas nesse repositório são necessárias para carregar as libs
```
🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
