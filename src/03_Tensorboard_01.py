import tensorflow as tf
import os

# 设置graph存放目录,定义目录，如果不存在就建立，如果不是目录就报错
summary_dir = "./summary"
if os.path.exists(summary_dir):
    assert os.path.isdir(summary_dir) is True  # 指定目录不是文件
else:
    os.makedirs(summary_dir)
# end if

# 在此处编写图像
a = tf.constant(5.0, name="a")
b = tf.constant(6.0, name="b")
c = tf.add(a, b, name='c')


with tf.Session() as sess:
    # 初始化全局变量（没有定义变量，这2句话其实不用写）
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    # 计算图
    print(sess.run(c))

    # 保存graph到
    tf.summary.FileWriter(summary_dir, graph=sess.graph)

# 启动网页查看
os.system('tensorboard --logdir="' + summary_dir + '"')
