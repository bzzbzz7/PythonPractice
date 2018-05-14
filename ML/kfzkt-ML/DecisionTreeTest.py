from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO
import csv

allElectronicsData = open(".\electronics.csv",newline='')
reader = csv.reader(allElectronicsData)
headers = next(reader)

print(headers)

featureList=[]
labelList=[]

for row in reader:
    labelList.append(row[len(row)-1])
    rowDic = {}
    for i in range(1, len(row)-1):
        rowDic[headers[i]] = row[i]
    featureList.append(rowDic)
print(featureList)

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()

print("dummyX:" + str(dummyX))

print(vec.get_feature_names())

lb = preprocessing.LabelBinarizer()
dummyY=lb.fit_transform(labelList)
print("dummY:" + str(dummyY))

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(dummyX,dummyY)
print(str(clf))

with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

oneRowX = dummyX[0:5, :]
print("oneRowX:" + str(oneRowX))

newRowX = oneRowX

# newRowX[0] = 1
# newRowX[2] = 0
print("newRowX:" + str(newRowX))

predictedY = clf.predict(newRowX)
print("predictedY:" + str(predictedY))




