import sys
import numpy as np
from gplearn.genetic import SymbolicRegressor
import csv


def read_nth_column(n, filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=",")
        return list(map(lambda x: float(x[n]), reader))


def main():
    if len(sys.argv) < 2:
        print("Provide data file name!")
        exit(1)

    filename = sys.argv[1]

    # Training samples
    x = read_nth_column(0, filename)
    x_train = np.ndarray((len(x),), buffer=np.array(x, dtype=float)).reshape(-1, 1)
    # print(x_train)
    y = read_nth_column(1, filename)
    y_train = np.ndarray((len(y),), buffer=np.array(y, dtype=float))
    # print(y_train)

    # Testing samples
    X_test = read_nth_column(0, filename)
    y_test = read_nth_column(1, filename)

    est_gp = SymbolicRegressor(population_size=5000, generations=100,
                               p_crossover=0.7, p_subtree_mutation=0.1,
                               p_hoist_mutation=0.05, p_point_mutation=0.1, verbose=1,
                               parsimony_coefficient=0.01, random_state=0,
                               function_set=('add', 'sub', 'mul', 'div', 'sin', 'cos', 'sqrt'))
    est_gp.fit(x_train, y_train)

    print(est_gp._program)


if __name__ == "__main__":
    main()








