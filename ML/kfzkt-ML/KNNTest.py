from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()

# print(iris)

print(iris.data)
print(iris.target)
print(iris.target_names)
print(iris.DESCR)

knn.fit(iris.data, iris.target)

print(knn.predict([[5.1, 3.5, 1.4, 0.2]]))