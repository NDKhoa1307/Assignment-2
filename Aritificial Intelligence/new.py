import tensorflow as tf

string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.25, tf.float32)

tf.rank(string)