# 🖼️ pipeline-filtros-imagem

Projeto de processamento digital de imagens com aplicação dos filtros clássicos de **Média**, **Mediana** e **Sobel** utilizando Python. Os resultados são exibidos lado a lado e salvos automaticamente na pasta de saída.

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Filtros Implementados](#filtros-implementados)
- [Análise dos Resultados](#análise-dos-resultados)
- [Aplicações em Projetos Reais](#aplicações-em-projetos-reais)

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo aplicar e comparar filtros clássicos de processamento de imagens, permitindo observar como cada filtro transforma a imagem original e em quais situações cada um é mais adequado. O projeto conta com dois scripts principais:

- **`filtros_imagem.py`** — aplica os três filtros (Média, Mediana e Sobel) com kernel fixo 5×5 e exibe os resultados lado a lado
- **`comparacao_kernels.py`** — experimenta diferentes tamanhos de kernel nos filtros de Média e Mediana, permitindo observar como o tamanho influencia a suavização

---

## 🛠️ Tecnologias

- [Python 3.x](https://www.python.org/)
- [OpenCV](https://opencv.org/) — leitura da imagem, aplicação dos filtros e cálculo do gradiente Sobel
- [NumPy](https://numpy.org/) — construção dos kernels e cálculo da magnitude do gradiente
- [Matplotlib](https://matplotlib.org/) — visualização e exportação dos resultados

---

## 📁 Estrutura do Projeto

```
📁 pipeline-filtros-imagem/
├── filtros_imagem.py           # Aplica Média, Mediana e Sobel
├── comparacao_kernels.py       # Compara diferentes tamanhos de kernel
├── README.md
├── 📁 Imagens para teste/
│   └── sua_imagem.jpg
└── 📁 resultados/              # Criada automaticamente ao executar
    ├── resultado_*.png
    ├── kernels_media_*.png
    ├── kernels_mediana_*.png
    └── comparacao_media_vs_mediana_*.png
```

---

## ▶️ Como Executar

**1. Clone o repositório**
```bash
git clone https://github.com/THAIAGUITO/Processamentos-de-imagens-com-filtros
cd pipeline-filtros-imagem
```

**2. Instale as dependências**
```bash
pip install opencv-python numpy matplotlib
```

**3. Adicione sua imagem na pasta `Imagens para teste/`**

**4. Ajuste o caminho da imagem nos scripts e execute**

```bash
# Aplicar os três filtros
python filtros_imagem.py

# Comparar diferentes tamanhos de kernel
python comparacao_kernels.py
```

Os resultados serão salvos automaticamente na pasta `resultados/`.

> ⚠️ Os tamanhos de kernel informados em `comparacao_kernels.py` devem ser sempre **ímpares** (3, 5, 7, 9...). O script valida isso automaticamente.

---

## 🔍 Filtros Implementados

### Filtro de Média
Suaviza a imagem de forma uniforme, sendo eficaz contra ruído Gaussiano, mas pode borrar bordas com kernels maiores.

### Filtro de Mediana
Preserva bordas melhor que a média e é especialmente eficaz para remover ruído sal e pimenta.

### Filtro de Sobel
Destaca regiões de transição de intensidade, ou seja, as bordas da imagem.

---

## 📊 Análise dos Resultados

### a) Como a imagem original mudou após a aplicação de cada filtro?

- **Filtro de Média** — a imagem ficou visivelmente mais suave e com menos detalhes finos. Pequenas variações de cor e textura foram atenuadas, e as bordas perderam um pouco de definição, especialmente com kernels maiores.
- **Filtro de Mediana** — o resultado também foi uma imagem mais suave, porém com as bordas mais preservadas em comparação à média. Ruídos pontuais foram eliminados de forma mais eficiente.
- **Filtro de Sobel** — a imagem foi transformada em escala de cinza, destacando apenas as regiões de transição de intensidade. O resultado evidencia contornos, bordas e detalhes de textura que antes se misturavam ao restante da imagem.

### b) Qual filtro foi mais eficaz para suavizar a imagem?

O **Filtro de Média** foi o mais eficaz para suavização da imagem, pois distribui a influência de todos os pixels vizinhos de forma uniforme. Com kernels maiores (acima de 7×7), o efeito de borramento fica cada vez mais evidente. O **Filtro de Mediana** também suaviza bem, mas tende a preservar bordas, o que o torna menos agressivo na suavização de regiões texturizadas.

### c) Qual filtro foi mais eficaz para destacar as bordas?

O **Filtro de Sobel** foi o mais eficaz para destacar as bordas. Ele transforma a imagem em um mapa de bordas, onde regiões com forte variação de brilho aparecem com alta intensidade e regiões homogêneas ficam escuras. Nenhum dos filtros de suavização é adequado para esse propósito já o filtro de **Sobel** sim.

### d) Quais situações podem exigir o uso de cada tipo de filtro em um projeto real?

| Filtro | Situações de uso |
|---|---|
| **Média** | Pré-processamento de imagens médicas para reduzir ruído antes de segmentação; suavização de imagens capturadas com câmeras de baixa qualidade; preparação de imagens para OCR quando há granulação uniforme |
| **Mediana** | Restauração de fotos antigas digitalizadas com ruído sal e pimenta; limpeza de imagens de câmeras de segurança; pré-processamento em visão computacional onde a preservação de bordas é essencial para detecção de objetos |
| **Sobel** | Detecção de objetos e contornos em sistemas de visão industrial; reconhecimento de placas de trânsito e leitura de texto em imagens; análise de imagens de satélite para identificar limites de regiões; extração de características em redes neurais convolucionais |

---
