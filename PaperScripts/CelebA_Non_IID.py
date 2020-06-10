import os

os.chdir('../')

params_run = [
    ['celeba', 'LeNet', 'adam', 'None', 5e-4, 1, 'natural', 1000, 1.0, 1],
    ['celeba', 'LeNet', 'adam', 'None', 5e-4, 1, 'natural', 4, 0.1, 32],
]

repeat = 10

num_clients = 100
max_epochs = 2000

upload_sparse = 1.0
upload_strategy = 'no-compress'

order = 'python3 run_base_local.py --dataset {} --model {} --non-iid {} --non-iid-strategy {} ' \
        '--B {} --C {} --E {} --file_name {} --num_clients {} --max_epochs {} --lr {} --optimizer {} ' \
        '--upload_name_filter {} --upload_sparse {} --upload_strategy {} ' \
        '--sudo no'

file_name = os.path.basename(__file__).strip('run_ .py') + '_trials.txt'

for r in repeat:
    for dataset, model, optimizer, upload_name_filter, lr, non_iid, non_iid_strategy, b, c, e in params_run:
        os.system(order.format(dataset, model, non_iid, non_iid_strategy, b, c, e, file_name,
                               num_clients, max_epochs, lr, optimizer, upload_name_filter,
                               upload_sparse, upload_strategy))