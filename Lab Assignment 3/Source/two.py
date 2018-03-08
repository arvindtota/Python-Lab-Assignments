from sklearn import svm
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Load iris data
iris = datasets.load_wine()
# Load data and target into h and v
h = iris.data
v = iris.target
# Split the data with 20% of testing data and 80% of training data
h_train, h_test, v_train, v_testdata = train_test_split(h, v, test_size=0.2)

print("linear kernel SVM:")
# Create model for SVM with linear kernel
lin_ker = svm.SVC(kernel="linear")
# Fit the data into the model
lin_ker.fit(h_train, v_train)
# Generate v_prediction from trained model with data from h_test
v_prediction = lin_ker.predict(h_test)
# Print data on both v_predicteddata and v_testdata
print("v_predicteddata:")
print(v_prediction)
print("v_testdata:")
print(v_testdata)
# Check accuracv score bv compare v_testdata and v_predicteddata
print("Linear kernel SVM Accuracy: %.4f" % metrics.accuracy_score(v_testdata, v_prediction))

print("\nRBF kernel SVM:")
# Create model for SVM with RBF kernel
rbf_ker = svm.SVC(kernel="rbf")
# Fit the data into the model
rbf_ker.fit(h_train, v_train)
# Generate v_prediction from trained model with data from h_test
v_prediction = rbf_ker.predict(h_test)
# Print data on both v_predicteddata and v_testdata
print("v_predicteddata:")
print(v_prediction)
print("v_testdata:")
print(v_testdata)
# Check accuracv score bv compare v_testdata and v_predicteddata
print("RBF kernel SVM Accuracy: %.4f" % metrics.accuracy_score(v_testdata, v_prediction))