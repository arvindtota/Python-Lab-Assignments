import pandas as pd
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Loading iris data set
data = load_iris()
df = pd.DataFrame(data.data, columns=["sep_len", "sep_wid", "pet_len", "pet_wid"])
df["target"] = pd.Series(data.target)

# Extracting features from panda df
features = df.loc[:, ['sep_len', 'sep_wid', 'pet_len', 'pet_wid']]
labels = df.loc[:, ['target']]

# Inserting features to encoder
one_hot_encoder = OneHotEncoder()
one_hot_encoder.fit(features)
features = one_hot_encoder.transform(features).toarray()
# Inserting labels to encoder
one_hot_encoder.fit(labels)
labels = one_hot_encoder.transform(labels).toarray()

# 80% train and 20% test data splitting
x_tr, x_te, y_tr, y_te = train_test_split(features, labels, test_size=0.2)

# variables
x = tf.placeholder(tf.float32, [None, 15])
y = tf.placeholder(tf.float32, [None, 3])
w = tf.Variable(tf.zeros([15, 3]))
b = tf.Variable(tf.zeros([3]))

# predicted value variable
y_predict = tf.nn.softmax(tf.add(tf.matmul(x, w), b))

# loss function for LR
loss = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predict)

# Gradient descent optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

total_row = df.shape[0]

# Tensor flow graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./arvind/dl/graphs/output', sess.graph)
    # Training Logistic Regression model against training data
    for _ in range(total_row):
        __, current_loss = sess.run([optimizer, loss], feed_dict={x: x_tr, y: y_tr})
        print("(Iteration,Loss):({},{})".format(_ + 1, sum(current_loss) / total_row))
    # Test accuracy against testing data
    prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))

    # Accuracy model percentage
    print("Model accuracy percentage is:", accuracy.eval({x: x_te, y: y_te}))
    writer.close()