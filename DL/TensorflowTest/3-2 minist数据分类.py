import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

with tf.name_scope("input"):
    x = tf.placeholder(tf.float32, [None, 784],name="x_input")
    y = tf.placeholder(tf.float32, [None, 10],name="y_input")

with tf.name_scope("layer"):
    with tf.name_scope("weights"):
        w1 = tf.Variable(tf.truncated_normal([784, 100], stddev=0.1), name="w1")
    with tf.name_scope("biases"):
        b1 = tf.Variable(tf.zeros([100]) + 0.1, name="b1")
    with tf.name_scope("layer1"):
        a1 = tf.nn.relu(tf.matmul(x, w1) + b1, name="a1")

# w1 = tf.Variable(tf.truncated_normal([784, 100], stddev=0.1))
# b1 = tf.Variable(tf.zeros([100]) + 0.1)
# a1 = tf.nn.relu(tf.matmul(x, w1) + b1)

w2 = tf.Variable(tf.truncated_normal([100, 100], stddev=0.1))
b2 = tf.Variable(tf.zeros([100]) + 0.1)
a2 = tf.nn.relu(tf.matmul(a1, w2) + b2)

w3 = tf.Variable(tf.truncated_normal([100, 10], stddev=0.1))
b3 = tf.Variable(tf.zeros([10]) + 0.1)
prediction = tf.nn.softmax(tf.matmul(a2, w3) + b3)

# loss = tf.reduce_mean(tf.square(y - prediction))
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=prediction))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter("logs/",sess.graph)
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
        acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
        print("Iter " + str(epoch) + "   " + str(acc))
