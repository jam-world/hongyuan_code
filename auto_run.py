import subprocess

for i in range(0,1):
    for j in range(3):
        for dim_id in range(1,2):
            dim = 100 + 50 * (dim_id - 1)
            file_name = 'sbatch_for_{0}_{1}_{2}.sbatch'.format(i,j,dim)

            args = []
            args.append('sbatch')
            args.append(file_name)

            subprocess.call(args)
