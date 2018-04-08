# Author: bulletcross@gmail.com (Vishal Keshav)
# Module to transfer the weights to model tensors
import tensorflow as tf
import numpy as np

"""
Original AlexNet weights are stored in:
http://www.cs.toronto.edu/~guerzhoy/tf_alexnet/
"""

def transfer_weight(sess, weight_file, transfer_list, init_list):
    weight_dict = np.load(weight_file, encoding = 'bytes').item()
    #First transfer the weights to model
    for op in transfer_list:
        with tf.variable_scope(op, reuse = True):
            for data in weight_dict[op]:
                if len(data.shape) == 1:
                    v = tf.get_variable('biases', trainable = True)
                    sess.run(v.assign(data))
                else:
                    v = tf.get_variable('weights', trainable = True)
                    sess.run(v.assign(data))
    # Initialize init_list ops
    init_op = tf.variable_initializer(var_list = init_list)
    sess.run(init_op)
    return
