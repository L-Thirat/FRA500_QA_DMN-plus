from __future__ import print_function
from __future__ import division
import os
import tensorflow as tf
import numpy as np

import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--babi_task_id", help="specify babi task 1-20 (default=1)")
parser.add_argument("-t", "--dmn_type", help="specify type of dmn (default=original)")
args = parser.parse_args()

dmn_type = args.dmn_type if args.dmn_type is not None else "plus"
if dmn_type == "original":
    from dmn_original import Config
    config = Config()
elif dmn_type == "plus":
    from dmn_self_plus import Config
    config = Config()
else:
    raise NotImplementedError(dmn_type + ' DMN type is not currently implemented')

if args.babi_task_id is not None:
    config.babi_id = args.babi_task_id

config.strong_supervision = False

config.train_mode = False

print( 'Testing DMN ' + dmn_type + ' on babi task', config.babi_id)

import codecs
#todo writing & run
path_out = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/en-10k/%s_self_test.txt' % config.babi_id)
# f = codecs.open(path_out, 'w',encoding='utf8')
# for i in range(0,2):
#     inp = input("Input :")
#     inp = u"%s"%inp
#     f.write(inp)
#     f.write("\n")
# inp = input("Q :")
# f.write(inp)
# f.write("\n")
# f.close()
# asd

# create model
with tf.variable_scope('DMN') as scope:
    if dmn_type == "original":
        from dmn_original import DMN
        model = DMN(config)
    elif dmn_type == "plus":
        from dmn_self_plus import DMN_PLUS
        model = DMN_PLUS(config)

print('==> initializing variables')
init = tf.global_variables_initializer()
saver = tf.train.Saver()

with tf.Session() as session:
    session.run(init)
    print('==> restoring weights')
    saver.restore(session, 'weights/task' + str(model.config.babi_id) + '.weights')

    print('==> running DMN')
    # test_loss, test_accuracy = model.run_epoch(session, model.test)
    # print(model.test)
    # qp, ip, ql, il, im, a = data
    # questions, inputs, q_lens, input_lens, input_masks, answers

    asd
    answer = model.run_epoch(session, model.test)
    print(answer)
    # print('Test accuracy:', test_accuracy)
