# noinspection PyInterpreter
import tensorflow as tf

# # Tensor
# a = tf.constant(1)
# b = tf.constant(2)
# result = tf.add(a, b)
# print(result)
# #
# tensor_constant_demo = tf.constant([
#     [1.1, 2.2, 3.3],
#     [4.4, 5.5, 6.6]
# ], name='tensor_constant_demo', dtype=tf.float32)

# 修改形状
# value, dtype=None, shape=None
# tensor_constant_demo2 = tf.constant(value=list(range(8)), dtype=tf.float32, shape=[4, 2])
# print(tensor_constant_demo2)
# result_reshape = tf.reshape(tensor_constant_demo2, [2, 2, 2], name='result_reshape')
# print(result_reshape)
# exit()

plt = tf.placeholder(tf.float32, [None, 2])
print(plt)
plt.set_shape([3, 2])
print(plt)

# Session
with tf.Session() as sess:
    # print(sess.run(result))
    # print(sess.run([a, b, result]))
    # print(tensor_constant_demo.shape)
    # print(tensor_constant_demo.graph)
    #
    # print("-"*80)
    # print(tensor_constant_demo)
    # print("-"*80)
    # print(tensor_constant_demo.op)
    pass
