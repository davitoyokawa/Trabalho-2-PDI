# High-Boost Filtering e Unsharp Masking em Python

Este repositório contém um exemplo de implementação de filtros de High-Boost e Unsharp Masking utilizando Python e OpenCV. O código aplica uma convolução Gaussiana para desfocar uma imagem e, em seguida, utiliza a diferença entre a imagem original e a imagem borrada (máscara de nitidez) para realçar detalhes na imagem.

## Funcionalidades

- **Kernel Gaussiano Personalizado**: Geração de um kernel Gaussiano 2D com tamanho e desvio padrão (`sigma`) definidos pelo usuário.
- **Desfoque Gaussiano**: Aplicação de convolução utilizando o kernel Gaussiano para desfocar a imagem.
- **Unsharp Masking**: Realce de detalhes ao somar a máscara de nitidez à imagem original.
- **High-Boost Filtering**: Extensão do Unsharp Masking, permitindo a amplificação adicional dos detalhes com um fator de amplificação (`k`) maior que 1.

## Pré-requisitos

- Python 3.x
- OpenCV
- NumPy

Como usar
1 - Carregar uma imagem: O código carrega uma imagem em escala de cinza da pasta images. Certifique-se de que a imagem esteja presente no diretório correto ou ajuste o caminho da imagem no código.

2 - Rodar o código: Execute o script para ver os resultados das operações de filtragem na imagem carregada.

3 - Interação com o código: O código exibirá a imagem original, a imagem borrada, a máscara de nitidez, o resultado de Unsharp Masking, e o resultado do High-Boost Filtering. As imagens serão exibidas em janelas separadas.

Explicação do Código
Geração do Kernel Gaussiano: O kernel é criado com base no tamanho e no desvio padrão (sigma) fornecidos, e é normalizado para que a soma dos seus elementos seja 1.

Convolução e Desfoque: A convolução é realizada utilizando cv2.filter2D, aplicando o kernel Gaussiano na imagem para gerar a versão borrada.

Máscara de Nitidez: A máscara de nitidez é calculada subtraindo a imagem borrada da imagem original.

Unsharp Masking: Este filtro é aplicado somando a máscara de nitidez à imagem original, com o objetivo de realçar os detalhes.

High-Boost Filtering: O filtro High-Boost é uma generalização do Unsharp Masking, onde a máscara de nitidez é amplificada por um fator k > 1 para aumentar a nitidez da imagem.

Resultados
As imagens resultantes das operações de Unsharp Masking e High-Boost Filtering são exibidas em janelas do OpenCV. O resultado final é salvo no formato correto para exibição, com valores de pixels convertidos para o intervalo de [0, 255].

Você pode instalar as dependências com:

```bash
pip install opencv-python numpy
