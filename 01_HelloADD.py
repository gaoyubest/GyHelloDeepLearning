# noinspection PyInterpreter
import tensorflow as tf

# # Tensor
# a = tf.constant(1)
# b = tf.constant(2)
# result = tf.add(a, b)
# print(result)
# #
tensor_constant_demo = tf.constant([
    [1.1, 2.2, 3.3],
    [4.4, 5.5, 6.6]
], name='tensor_constant_demo', dtype=tf.float32)

# 修改形状
# value, dtype=None, shape=None
# tensor_constant_demo2 = tf.constant(value=list(range(8)), dtype=tf.float32, shape=[4, 2])
# print(tensor_constant_demo2)
# result_reshape = tf.reshape(tensor_constant_demo2, [2, 2, 2], name='result_reshape')
# print(result_reshape)
# exit()

# plt = tf.placeholder(tf.float32, [None, 2])
# print(plt)
# plt.set_shape([3, 2])
# print(plt)
# plt_reshape = tf.reshape(plt, [2, 3])
# print(plt_reshape)

# tensor_demo = tf.zeros([2, 3], name=None)
# print(tensor_demo)
# tensor_demo1 = tf.ones([2, 3], name=None)
# print(tensor_demo1)
# tensor_demo2 = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3], name=None)
# print(tensor_demo2)
# tensor_fill = tf.fill([2, 3], 99, name=None)

# 类型转换
result_cast = tf.cast(tensor_constant_demo, tf.int32, name='result_cast')
print(tensor_constant_demo.dtype, '=>', result_cast.dtype)

# 结构调整
result_reshape = tf.reshape(tensor_constant_demo, [3, 2], name='result_reshape')
print(tensor_constant_demo.shape, '=>', result_reshape.shape)

# Session
with tf.Session() as sess:
    print(sess.run(tensor_demo))
    print(sess.run(tensor_demo1))
    print(sess.run(tensor_demo2))
    print(sess.run(tensor_fill))
    # print(sess.run(result))
    # print(sess.run([a, b, result]))
    # print(tensor_constant_demo.shape)
    # print(tensor_constant_demo.graph)
    #
    # print("-"*80)
    # print(tensor_constant_demo)
    # print("-"*80)
    # print(tensor_constant_demo.op)
