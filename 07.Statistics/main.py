import numpy as np

film_1 = np.array([0,0,0,0,1,0])
film_2 = np.array([0,1,0,1,0,0])
film_3 = np.array([0,0,1,1,1,0])
film_4 = np.array([1,0,0,1,0,1])

def angle_bw_vectors(vec1, vec2):
    dot_films_2_3 = film_2.dot(film_3)
    norm_films_2_3 = np.linalg.norm(vec1) * np.linalg.norm(vec2)

    return np.rad2deg(np.arccos(dot_films_2_3 / norm_films_2_3))

angle_2_3 = angle_bw_vectors(film_2, film_3)

print(angle_2_3)

film_matrix = np.array([film_1, film_2, film_3, film_4])



print(film_matrix.T.dot([1,2,3,4]))

print(film_matrix.T * [1,2,3,4])

print(np.linalg.norm(film_matrix) * np.linalg.norm([1,2,3,4]))