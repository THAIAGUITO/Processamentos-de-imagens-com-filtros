import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("resultados", exist_ok=True)

def aplicar_filtros(caminho_imagem):
    imagem_bgr = cv2.imread(caminho_imagem)
    if imagem_bgr is None:
        raise FileNotFoundError(f"Imagem não encontrada: {caminho_imagem}")
    
    imagem_rgb = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2RGB)

    imagem_cinza = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2GRAY)

    kernel_media = np.ones((5, 5), dtype=np.float32) / 25
    filtro_media = cv2.filter2D(imagem_rgb, -1, kernel_media)

    filtro_mediana = cv2.medianBlur(imagem_rgb, 5)

    sobel_x = cv2.Sobel(imagem_cinza, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagem_cinza, cv2.CV_64F, 0, 1, ksize=3)

    magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

    filtro_sobel = np.uint8(255 * magnitude / magnitude.max())

    fig, eixos = plt.subplots(1, 4, figsize=(22, 6))
    fig.suptitle(f"Filtros Aplicados — {os.path.basename(caminho_imagem)}", fontsize=16, fontweight="bold")

    configuracoes = [
        (imagem_rgb,     "Original",                        None),
        (filtro_media,   "Filtro de Média\n(kernel 5×5)",   None),
        (filtro_mediana, "Filtro de Mediana\n(janela 5×5)", None),
        (filtro_sobel,   "Filtro de Sobel\n(bordas)",       "gray"),
    ]

    for ax, (img, titulo, cmap) in zip(eixos, configuracoes):
        ax.imshow(img, cmap=cmap)
        ax.set_title(titulo, fontsize=13)
        ax.axis("off")

    plt.tight_layout()
    nome_arquivo = os.path.splitext(os.path.basename(caminho_imagem))[0]
    plt.savefig(f"resultados/resultado_{nome_arquivo}.png", dpi=150, bbox_inches="tight")
    plt.show()
    print(f"Resultado salvo em: resultados/resultado_{nome_arquivo}.png")

    # Adiciona ruído na imagem de teste para demonstrar a eficácia dos filtros
    ruido = np.random.choice([0, 255], size=imagem_cinza.shape, p=[0.95, 0.05]).astype(np.uint8)
    imagem_com_ruido = np.clip(imagem_cinza.astype(np.int16) + ruido, 0, 255).astype(np.uint8)

if __name__ == "__main__":
    aplicar_filtros("Imagens para teste/teste_media_mediana.jfif")