with open('./template.sbatch','r') as f:
    sbatch_template = f.read()
def sbatch_generator(arg_map):
    new_sbatch = sbatch_template.format(arg_map['log_file'], arg_map['seed'], arg_map['save_file_path'], arg_map['test_map'], arg_map['out_file'], arg_map['dim_model'])
    with open(arg_map['file_name'], 'w') as f:
        f.write(new_sbatch)

arg_map = {}
for i in range(0,1):
    for j in range(3):
        for dim_id in range(1,2):
            dim = 100 + 50 * (dim_id - 1)
            arg_map['log_file'] = 'base_line_log_{0}_{1}_{2}.txt'.format(i,j,dim)
            arg_map['seed'] = 12345 + i * 1000
            arg_map['save_file_path'] = 'base_line{0}.{1}.{2}/'.format(j,i,dim)
            arg_map['test_map'] = j
            arg_map['file_name'] = 'sbatch_for_{0}_{1}_{2}.sbatch'.format(i,j,dim)
            arg_map['out_file'] = 'sbatch_for_{0}_{1}_{2}'.format(i,j,dim)
            arg_map['dim_model'] = dim
            sbatch_generator(arg_map)
