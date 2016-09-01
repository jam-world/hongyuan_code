import re
import subprocess
def read_model_list():
    with open('latest_model_list.txt') as f:
        return f.readlines()

records = read_model_list()
for record in records:
    temp = re.search('line[0-9]+', record)
    temp = temp.group(0)
    temp = re.search('[0-9]+', temp)
    test_map = temp.group(0)
    
    args = []
    model_info = record.replace('\n','').split(' ')
    model_path = model_info[0] + '/' + model_info[1]

    record = record.replace('\n', '')
    record = record.replace(' ', '')

    args.append('python')
    args.append('test_neural_walker.py')
    args.append('-seed')
    args.append(str(12345 + int(test_map)))
    args.append('-model_path')
    args.append(model_path)
    args.append('-test_map')
    args.append(test_map)
    args.append('-file_save')
    args.append(record + '.txt')

    subprocess.call(args)
