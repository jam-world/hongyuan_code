#!/bin/sh
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --output={4}.out
source activate theanoPy2
module load cuda
python run_neural_walker_dim100.py -log_file ./{0} -seed {1} -save_file_path ./{2} -test_map {3} -dim_model {5}
