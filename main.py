import cv2
import numpy as np

def gaussian_kernel(size, sigma):
    # Gera um kernel Gaussiano 2D
    ax = np.linspace(-(size - 1) / 2., (size - 1) / 2., size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-0.5 * (np.square(xx) + np.square(yy)) / np.square(sigma))
    return kernel / np.sum(kernel)

# Carregar a imagem em escala de cinza
imagem_original = cv2.imread('images/fig3.4.tif', 0)
imagem_normalizada = imagem_original / 255.0  # Normalizar a imagem para o intervalo [0, 1]

cv2.imshow('Imagem Original', imagem_normalizada)

# Criar um kernel Gaussiano 31x31 com sigma=5
kernel_gaussiano = gaussian_kernel(size=31, sigma=5)

# Aplicar a convolução 
imagem_borrada = cv2.filter2D(imagem_normalizada, -1, kernel_gaussiano)

# Exibir a imagem borrada
cv2.imshow('Imagem Borrada', imagem_borrada)

# Calcular a máscara de nitidez 
mascara_nitidez = imagem_normalizada - imagem_borrada

# Exibir a máscara de nitidez
cv2.imshow('Máscara de Nitidez', mascara_nitidez)

# Aplicar unsharp masking com k = 1 (padrão)
imagem_unsharp = imagem_normalizada + mascara_nitidez
cv2.imshow('Resultado Unsharp Masking', np.clip(imagem_unsharp, 0, 1))

# Aplicar high-boost filtering com k > 1 (ex: k = 4.5)
fator_amplificacao = 4.5
imagem_highboost = imagem_normalizada + fator_amplificacao * mascara_nitidez

# Clipping para garantir que os valores estejam no intervalo [0, 1]
imagem_highboost_clipped = np.clip(imagem_highboost, 0, 1)

# Exibir o resultado de high-boost filtering
cv2.imshow('Resultado High-Boost Filtering', imagem_highboost_clipped)

# Converter para o intervalo [0, 255] para salvar como imagem e para exibição correta
imagem_final_exibicao = (imagem_highboost_clipped * 255).astype(np.uint8)

# Exibir o resultado final (após clipping e conversão para 8 bits)
cv2.imshow('Resultado Final', imagem_final_exibicao)

cv2.waitKey(0)
cv2.destroyAllWindows()
