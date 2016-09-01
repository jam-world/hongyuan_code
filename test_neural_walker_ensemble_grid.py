# -*- coding: utf-8 -*-
"""
run file for neural walker

@author: hongyuan
"""

import pickle
import time
import numpy
import theano
from theano import sandbox
import theano.tensor as tensor
import os
import scipy.io
from collections import defaultdict
from theano.tensor.shared_randomstreams import RandomStreams
import modules.utils as utils
import modules.models as models
import modules.optimizers as optimizers
import modules.trainers as trainers
import modules.data_processers as data_processers

import run_model

dtype=theano.config.floatX

#
input_tester = {
    #'log_file': './log.dim100.txt',
    'path_rawdata': None,
    #
    #'max_epoch': 50,
    #'dim_model': 100,
    'path_model': './test.l.dim100.models/model43.pkl',
    'map_test': 'grid',
    'file_save': './test.l.dim100.results.pkl',
    'seed': 12345
}

input_tester['path_model'] = []
input_tester['path_model'].append('./dim100.test0.0.100/model100.pkl')
input_tester['path_model'].append('./dim100.test0.1.100/model19.pkl')
input_tester['path_model'].append('./dim100.test0.2.100/model64.pkl')
input_tester['path_model'].append('./dim100.test0.3.100/model98.pkl')
input_tester['path_model'].append('./dim100.test0.4.100/model70.pkl')
input_tester['path_model'].append('./dim100.test0.5.100/model29.pkl')
input_tester['path_model'].append('./dim100.test0.6.100/model25.pkl')
input_tester['path_model'].append('./dim100.test0.7.100/model73.pkl')
input_tester['path_model'].append('./dim100.test0.8.100/model36.pkl')
input_tester['path_model'].append('./dim100.test0.9.100/model75.pkl')


#TODO: start training
run_model.test_model(input_tester)



'''
my code start
'''
# import argparse

# map_sequence = ['grid', 'l', 'jelly']

# if __name__ == '__main__':
#     print('Start Map tester ...')

#     # declare the parser
#     parser = argparse.ArgumentParser(description = 'test the hong yuan moel')

#     # add the argument
#     # parser.add_argument('-log_file', help='log file content', required = True)
#     # parser.add_argument('-save_file_path', help='save file path', required = True)
#     parser.add_argument('-model_path', help='model path', required = True)
#     parser.add_argument('-seed', help='random seed', required = True)
#     parser.add_argument('-test_map', help='map_for_test', required = True)
#     parser.add_argument('-file_save', help='file save path', required=True)

#     # parse the argument
#     args = parser.parse_args()

#     # input_trainer['log_file'] = args.log_file
#     # input_trainer['save_file_path'] = args.save_file_path
#     input_tester['seed'] = int(args.seed)
#     input_tester['map_test'] = map_sequence[int(args.test_map)]
#     input_tester['path_model'] = args.model_path
#     input_tester['file_save'] = args.file_save
#     # input_trainer['map_train'] = [map_sequence[idx] for idx in range(3) if idx != int(args.test_map)]

#     print(input_tester)
#     run_model.test_model(input_tester)


