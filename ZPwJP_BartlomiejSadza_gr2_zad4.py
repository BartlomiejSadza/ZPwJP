import numpy as np 
import pandas as pd
import random 
from PIL import Image
import numpy as np
from scipy.ndimage import convolve

def zadanie1(n, m):
    board = np.random.normal(3, 2, (n, m))
    print("Wygenerowana macierz (board):\n", board)
    
    board_det = np.linalg.det(board)
    print("Wyznacznik macierzy (board_det):\n", board_det)
    
    inverse_board = np.linalg.inv(board)
    print("Odwrotność macierzy (inverse_board):\n", inverse_board)
    
    transposed_board = np.transpose(board)
    print("Macierz transponowana (transposed_board):\n", transposed_board)

    eigenvalues, eigenvectors = np.linalg.eig(board)
    print("Wartości własne (eigenvalues):\n", eigenvalues)
    print("Wektory własne (eigenvectors):\n", eigenvectors)


# zadanie1(3, 3)

def zadanie2(matrix):
    df = pd.DataFrame(matrix)
    print("DataFrame:\n", df)
    value_counts = df.apply(pd.Series.value_counts).fillna(0)
    print("Częstotliwość występowania poszczególnych wartości:\n", value_counts)

# print(zadanie2(np.random.normal(3, 2, (3, 3))))

def zadanie3(matrix):
    matrix[matrix < 0] = 0
    
    col_means = np.nanmean(matrix, axis=0)
    inds = np.where(np.isnan(matrix))
    matrix[inds] = np.take(col_means, inds[1])
    
    return matrix


# matrix = np.array([[1, -2, np.nan], [4, np.nan, 6], [-7, 8, 9]])
# print(zadanie3(matrix))

matrix = np.random.rand(100, 5) * 10 
def zadanie4(matrix):
    
    min_vals = matrix.min(axis=0)
    max_vals = matrix.max(axis=0)
    normalized_matrix = (matrix - min_vals) / (max_vals - min_vals)
    
    col_means = normalized_matrix.mean(axis=0)
    
    return normalized_matrix, col_means


# normalized_matrix, col_means = zadanie4(matrix)
# print("Znormalizowana tablica:\n", normalized_matrix)
# print("Średnia wartość każdej kolumny po normalizacji:\n", col_means)

def zadanie5(array1, array2):

    iloczyn = np.dot(array1, array2)
    print(f"Iloczyn: {iloczyn}")

    kronecker_product = np.kron(array1, array2)
    print(f"Iloczyn Kroneckera: {kronecker_product}")


# matrix1 = np.random.rand(100, 100) * 10
# matrix2 = np.random.rand(100, 100) * 10
# print(zadanie5(matrix1, matrix2))

def zadanie6(data):

    correlation_matrix = np.corrcoef(data, rowvar=False)
    print("Correlation Matrix:")
    print(correlation_matrix)
    
    highest_positive_corr = -1
    highest_negative_corr = 1
    pos_pair = (0, 0)
    neg_pair = (0, 0)
    
    for i in range(correlation_matrix.shape[0]):
        for j in range(i + 1, correlation_matrix.shape[1]):
            if correlation_matrix[i, j] > highest_positive_corr:
                highest_positive_corr = correlation_matrix[i, j]
                pos_pair = (i, j)
            if correlation_matrix[i, j] < highest_negative_corr:
                highest_negative_corr = correlation_matrix[i, j]
                neg_pair = (i, j)
    
    print(f"Najwyższa dodatnia korelacja: {highest_positive_corr} między kolumnami {pos_pair}")
    print(f"Najwyższa ujemna korelacja: {highest_negative_corr} między kolumnami {neg_pair}")


# zadanie6(data)

def zadanie7(image_path):
    image = Image.open(image_path)
    image_np = np.array(image)
    
    def rgb2gray(rgb):
        return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    
    gray_image = rgb2gray(image_np)
    
    def gaussian_blur(image, kernel_size=9, sigma=2.0):
        ax = np.linspace(-(kernel_size - 1) / 2., (kernel_size - 1) / 2., kernel_size)
        gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
        kernel = np.outer(gauss, gauss)
        kernel /= np.sum(kernel)
        return convolve(image, kernel)

    blurred_image = gaussian_blur(gray_image)
    def sobel_edge_detection(image):
        Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        Ix = convolve(image, Kx)
        Iy = convolve(image, Ky)
        G = np.hypot(Ix, Iy)
        G = G / G.max() * 255
        return G
    
    edges = sobel_edge_detection(blurred_image)
    

    gray_image_pil = Image.fromarray(gray_image.astype(np.uint8))
    blurred_image_pil = Image.fromarray(blurred_image.astype(np.uint8))
    edges_pil = Image.fromarray(edges.astype(np.uint8))
    
    gray_image_pil.save("gray_image.png")
    blurred_image_pil.save("blurred_image.png")
    edges_pil.save("edges.png")


zadanie7('/Users/bartlomiejsadza/Downloads/mati.png')

