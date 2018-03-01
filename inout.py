import pandas as pd
import numpy as np
import re

# Reader
def read_file(file_name):
    df = pd.read_csv(file_name, sep=' ')
    df.columns = ['start_row', 'start_col', 'end_row', 'end_col', 'earliest_start', 'latest_end']

    with open('a_example.in') as f:
        first_line = re.sub(r'\n', '', f.readline())

    variables = dict(zip(['n_rows', 'n_cols', 'n_cars', 'n_rides', 'bonus', 'steps'], [int(st) for st in first_line.split(" ")]))
    return df, variables

#Writer
def write_solution(solutions):
    solution_file = open('solution.out','w') 
    for s in solutions:
        solution_file.write(str(len(s)) + ' ')
        for r in s:
            solution_file.write(str(r) + ' ')
        solution_file.write('\n')

    solution_file.close()