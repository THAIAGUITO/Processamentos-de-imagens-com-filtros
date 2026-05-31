import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread('cat.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

k3  = cv2.GaussianBlur(imagem, (3, 3),  0)
k9  = cv2.GaussianBlur(imagem, (9, 9),  0)
k21 = cv2.GaussianBlur(imagem, (21, 21), 0)

# Exibir os resultados da aplicação do filtro
fig, axes = plt.subplots(1, 4, figsize=(20, 5))
titulos = ['Original', 'Gaussiano 3x3', 'Gaussiano 9x9', 'Gaussiano 21x21']
imagens = [imagem, k3, k9, k21]

for ax, img, titulo in zip(axes, imagens, titulos):
    ax.imshow(img)
    ax.set_title(titulo, fontsize=12)
    ax.axis('off')

plt.suptitle('Filtro Gaussiano — Efeito Progressivo', fontsize=14)
plt.tight_layout()
plt.show()