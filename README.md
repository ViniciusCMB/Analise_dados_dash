# Analise_dados_dash

Este é um aplicativo web desenvolvido com [Dash](https://dash.plotly.com/) para visualização e análise de dados do projeto Serra Rocketry.

## Descrição

O Serra Rocketry Dashboard é uma aplicação web que permite a visualização e análise de dados relacionados ao projeto Serra Rocketry. Ele possui uma interface amigável e interativa, com suporte para múltiplas páginas e navegação fácil.

## Tecnologias Utilizadas

- [Dash](https://dash.plotly.com/)
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [FPDF](http://www.fpdf.org/)
- [Plotly](https://plotly.com/python/)
- [SciPy](https://www.scipy.org/)

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e ative-o:

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Dependências

As seguintes dependências são necessárias para executar o projeto:

```plaintext
dash==2.15.0
fpdf==1.7.2
numpy==2.1.1
pandas==2.2.3
plotly==5.19.0
scipy==1.14.1
sympy==1.12
```

## Uso

1. Execute o arquivo:

   ```sh
   python app.py
   ```

2. O navegador web será aberto automaticamente com o aplicativo rodando em http://localhost:8050/.

## Estrutura do Projeto

- `app.py`: Arquivo principal que contém a lógica do aplicativo Dash.
- `navbar.py`: Contém a função `create_navbar` para criar a barra de navegação.
- `analise.py`: Contém a lógica para análise de dados de testes estáticos, incluindo integração numérica, interpolação spline e geração de relatórios em PDF e Excel.
- `assets/`: Diretório para arquivos estáticos como CSS e imagens.
- `pages/`: Diretório para arquivos de páginas adicionais.

```plaintext
├── app.py
├── navbar.py
├── assets/
    ├── LOGO - ALTERNATIVA.png
    ├── logomarca-uerj-300x300.png
    ├── favicon.ico
    └── LOGO - SEM TEXTO.png
├── pages/
    ├── home.py
    ├── not_found_404.py
    ├── analise.py
    └── analise_voo.py
├── requirements.txt
└── README.md
```

## Descrição do analise.py

O arquivo analise.py contém a lógica para análise de dados de testes estáticos. Ele inclui as seguintes funcionalidades:

- Integração Numérica: Calcula a integral dos dados usando a 2ª regra de Simpson.
- Interpolação Spline: Realiza a interpolação spline dos pontos de dados.
- Geração de Relatórios: Gera e salva relatórios em PDF e Excel.
- Callbacks do Dash: Atualiza o gráfico e a seção de análise com base no intervalo de dados selecionado e lida com o salvamento da análise.
