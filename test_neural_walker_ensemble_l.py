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
    'map_test': 'l',
    'file_save': './test.l.dim100.results.pkl',
    'seed': 12345
}

input_tester['path_model'] = []
input_tester['path_model'].append('./dim100.test1.0.100/model48.pkl')
input_tester['path_model'].append('./dim100.test1.1.100/model69.pkl')
input_tester['path_model'].append('./dim100.test1.2.100/model45.pkl')
input_tester['path_model'].append('./dim100.test1.3.100/model75.pkl')
input_tester['path_model'].append('./dim100.test1.4.100/model62.pkl')
input_tester['path_model'].append('./dim100.test1.5.100/model66.pkl')
input_tester['path_model'].append('./dim100.test1.6.100/model44.pkl')
input_tester['path_model'].append('./dim100.test1.7.100/model83.pkl')
input_tester['path_model'].append('./dim100.test1.8.100/model42.pkl')
input_tester['path_model'].append('./dim100.test1.9.100/model79.pkl')

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


