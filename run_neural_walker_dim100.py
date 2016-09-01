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

input_trainer = {
    'log_file': './log.dim100.txt',
    'path_rawdata': None,
    #
    'max_epoch': 20,
    'dim_model': 100,
    'path_start_model': None,
    'save_file_path': './dim100.models/',
    'optimizer': 'adam',
    'maps_train': [
        'grid', 'jelly'
    ]
}

#TODO: start training
# run_model.train_model(input_trainer)


'''
my code start
'''
import argparse

map_sequence = ['grid', 'l', 'jelly']

if __name__ == '__main__':
    print('Start Map tester ...')

    # declare the parser
    parser = argparse.ArgumentParser(description = 'run the hong yuan moel')

    # add the argument
    parser.add_argument('-log_file', help='log file content', required = True)
    parser.add_argument('-save_file_path', help='save file path', required = True)
    parser.add_argument('-seed', help='random seed', required = True)
    parser.add_argument('-test_map', help='map_for_test', required = True)
    parser.add_argument('-dim_model', help='depth of the model', default = 100)

    # parse the argument
    args = parser.parse_args()

    input_trainer['log_file'] = args.log_file
    input_trainer['save_file_path'] = args.save_file_path
    input_trainer['seed'] = int(args.seed)
    input_trainer['maps_train'] = [map_sequence[idx] for idx in range(3) if idx != int(args.test_map)]
    input_trainer['dim_model'] = int(args.dim_model)

    print(input_trainer)
    run_model.train_model(input_trainer)

