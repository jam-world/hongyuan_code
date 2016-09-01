import subprocess

for i in range(10):
    for j in range(3):
        file_name = 'sbatch_for_{0}_{1}.sbatch'.format(i,j)

        args = []
        args.append('sbatch')
        args.append(file_name)

        subprocess.call(args)
