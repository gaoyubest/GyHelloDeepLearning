import tensorflow as tf

a = tf.constant([1, 2, 3, 4, 5, 6])
# 平均值0.0，方差1.0
var2 = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0), name='var2')

print(a, var2)

# 错误：Attempting to use uninitialized value var2
# 必须做一步显示的初始化
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    # 必须运行初始化op
    sess.run(init_op)
    print(sess.run([a, var2]))