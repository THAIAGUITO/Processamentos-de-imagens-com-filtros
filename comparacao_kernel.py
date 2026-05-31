import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def comparar_kernels(caminho_imagem, tamanhos_kernel=(3, 5, 7, 11, 15)):
    """
    Aplica filtros de Média e Mediana com diferentes tamanhos de kernel
    e exibe os resultados lado a lado para comparação.

    Parâmetros:
        caminho_imagem  : caminho para a imagem de entrada
        tamanhos_kernel : tupla com os tamanhos de kernel a testar (devem ser ímpares)
    """

    imagem_bgr = cv2.imread(caminho_imagem)
    if imagem_bgr is None:
        raise FileNotFoundError(f"Imagem não encontrada: {caminho_imagem}")

    imagem_rgb = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2RGB)
    nome_arquivo = os.path.splitext(os.path.basename(caminho_imagem))[0]
    os.makedirs("resultados", exist_ok=True)

    for k in tamanhos_kernel:
        if k % 2 == 0:
            raise ValueError(f"O tamanho do kernel deve ser ímpar. Valor inválido: {k}")

    n_kernels = len(tamanhos_kernel)

    fig1, eixos1 = plt.subplots(1, n_kernels + 1, figsize=(5 * (n_kernels + 1), 5))
    fig1.suptitle("Comparação de Kernels — Filtro de Média", fontsize=15, fontweight="bold")

    eixos1[0].imshow(imagem_rgb)
    eixos1[0].set_title("Original", fontsize=12)
    eixos1[0].axis("off")

    for i, k in enumerate(tamanhos_kernel):
        kernel_media = np.ones((k, k), dtype=np.float32) / (k * k)
        resultado = cv2.filter2D(imagem_rgb, -1, kernel_media)
        eixos1[i + 1].imshow(resultado)
        eixos1[i + 1].set_title(f"Kernel {k}×{k}", fontsize=12)
        eixos1[i + 1].axis("off")

    plt.tight_layout()
    caminho_media = f"resultados/kernels_media_{nome_arquivo}.png"
    plt.savefig(caminho_media, dpi=150, bbox_inches="tight")
    print(f"[Média]      Salvo em: {caminho_media}")

    fig2, eixos2 = plt.subplots(1, n_kernels + 1, figsize=(5 * (n_kernels + 1), 5))
    fig2.suptitle("Comparação de Kernels — Filtro de Mediana", fontsize=15, fontweight="bold")

    eixos2[0].imshow(imagem_rgb)
    eixos2[0].set_title("Original", fontsize=12)
    eixos2[0].axis("off")

    for i, k in enumerate(tamanhos_kernel):
        resultado = cv2.medianBlur(imagem_rgb, k)
        eixos2[i + 1].imshow(resultado)
        eixos2[i + 1].set_title(f"Kernel {k}×{k}", fontsize=12)
        eixos2[i + 1].axis("off")

    plt.tight_layout()
    caminho_mediana = f"resultados/kernels_mediana_{nome_arquivo}.png"
    plt.savefig(caminho_mediana, dpi=150, bbox_inches="tight")
    print(f"[Mediana]    Salvo em: {caminho_mediana}")

    fig3, eixos3 = plt.subplots(2, n_kernels + 1, figsize=(5 * (n_kernels + 1), 10))
    fig3.suptitle("Média vs Mediana por Tamanho de Kernel", fontsize=15, fontweight="bold")

    for linha, rotulo in enumerate(["Filtro de Média", "Filtro de Mediana"]):
        eixos3[linha][0].imshow(imagem_rgb)
        eixos3[linha][0].set_title(f"Original\n({rotulo})", fontsize=11)
        eixos3[linha][0].axis("off")

    for i, k in enumerate(tamanhos_kernel):
        kernel_media = np.ones((k, k), dtype=np.float32) / (k * k)
        eixos3[0][i + 1].imshow(cv2.filter2D(imagem_rgb, -1, kernel_media))
        eixos3[0][i + 1].set_title(f"Média {k}×{k}", fontsize=11)
        eixos3[0][i + 1].axis("off")

        eixos3[1][i + 1].imshow(cv2.medianBlur(imagem_rgb, k))
        eixos3[1][i + 1].set_title(f"Mediana {k}×{k}", fontsize=11)
        eixos3[1][i + 1].axis("off")

    plt.tight_layout()
    caminho_comparacao = f"resultados/comparacao_media_vs_mediana_{nome_arquivo}.png"
    plt.savefig(caminho_comparacao, dpi=150, bbox_inches="tight")
    print(f"[Comparação] Salvo em: {caminho_comparacao}")

    plt.show()

if __name__ == "__main__":
    comparar_kernels(
        caminho_imagem="Imagens para teste/teste_filtro_sobel.jpg",  
        tamanhos_kernel=(3, 5, 7, 11, 15)                  
    )