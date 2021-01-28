import tensorflow as tf
from zhmh.TensorBoard import TensorBoard

# 在此处编写图像
a = tf.constant(5.0, name="a")
b = tf.constant(6.0, name="b")
c = tf.add(a, b, name='c')


# 设置graph存放目录
tb = TensorBoard("./summary")
with tf.Session() as sess:
    # 初始化全局变量（没有定义变量，这2句话其实不用写）
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    # 计算图
    print(sess.run(c))

    # 保存graph到
    tb.save(sess.graph)
# 启动网页查看
tb.board()
