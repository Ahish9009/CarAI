import tensorflow as tf
import pandas as pd
import numpy as np

modelNo = 1

def multilayerPerceptron(x, weights, biases, keep_prob):
    layer1 = tf.add( tf.matmul(x, weights['h1']), biases['b1'] )
    layer1 = tf.nn.relu(layer1)
    layer1 = tf.nn.dropout(layer1, keep_prob)
    
    outLayer = tf.matmul(layer1, weights['out']) + biases['out']
    
    return outLayer

nH1 = 10
nInput = 11
nOutput = 1

weights = {
    'h1':tf.Variable(tf.random_normal([nInput, nH1])),
    'out':tf.Variable(tf.random_normal([nH1, nOutput]))
}
biases = {
    'b1':tf.Variable(tf.random_normal([nH1])),
    'out':tf.Variable(tf.random_normal([nOutput]))
}

keep_prob = tf.placeholder("float")
x = tf.placeholder("float", [None, nInput])
y = tf.placeholder("float", [None, nOutput])

saver = tf.train.Saver()

def drive(inp):

    inp = np.array([np.array(inp).astype("float32")])
    # saver = tf.train.Saver()
    with tf.Session() as sess:

        saver.restore(sess, 'tensorFlow/aBPedalModel'+str(modelNo)+'/model.ckpt')

        predictions = multilayerPerceptron(x, weights, biases, 1.0)
        yABPedal = sess.run(predictions, feed_dict = {x: inp, keep_prob: 1.0})
        
        saver.restore(sess, 'tensorFlow/stAngleModel'+str(modelNo)+'/model.ckpt')
        
        predictions = multilayerPerceptron(x, weights, biases, 1.0)
        yStAngle = sess.run(predictions, feed_dict = {x: inp, keep_prob: 1.0})
        return float(yABPedal), float(yStAngle)

