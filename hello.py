
import tensorflow as tf

a = tf.constant(1, dtype=tf.float32)
b = tf.constant(1, dtype=tf.float32)
c = tf.add(a, b)

with tf.Session() as sess:
    val = sess.run(c)
    print(val)
