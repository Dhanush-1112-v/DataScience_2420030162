from scipy.spatial import distance, minkowski_distance
import numpy as np
pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])
#Euclidean distance
euclidean_distance = distance.euclidean(pointA, pointB)
print("Euclidean:", euclidean_distance)
#inverse of Euclidean distance
similarity = 1 / (1 + euclidean_distance)
print("Similarity:", similarity)

#manhattan distance
pointa = np.array([2, 4, 6, 8])
pointb = np.array([5, 1, 9, 2])
manhattan_distance = distance.cityblock(pointa, pointb)
print("Manhattan:", manhattan_distance)
#inverse of Manhattan distance
similarity_manhattan = 1 / (1 + manhattan_distance)
print("Similarity Manhattan:", similarity_manhattan)

#minkowski distance p=3
point1 = np.array([2, 4, 6,9])
point2 = np.array([5, 1, 9, 2])
minkowski_distance_p3 = distance.minkowski(point1, point2, p=3)
print("Minkowski:", minkowski_distance_p3)
#inverse of Minkowski distance
similarity_minkowski = 1 / (1 + minkowski_distance_p3)
print("Similarity Minkowski:", similarity_minkowski)

#minkowski distance p=2
minkowski_distance_p2 = distance.minkowski(pointA, pointB, p=2)
print("Minkowski p=2:", minkowski_distance_p2)


