# -*- coding=utf-8 -*-

"""TODO: DESCRIPTION."""

from pathlib import Path  # built-in usefull Path class

from pulp import *
import pandas as pd
import numpy as np


from tp2_read_data_files import get_adm_cells_data

# ============================================================================ #
#                                  SET MODEL                                   #
# ============================================================================ #
def set_model_name(adm_cells, row_limits, col_limits):
    """TODO: Description."""
    # ------------------------------------------------------------------------ #
    # Linear problem with maximization
    # ------------------------------------------------------------------------ #
    prob = LpProblem(name='set_model_name', sense=LpMaximize)
    # FIXME: it is not always a maximization problem ...

    # ------------------------------------------------------------------------ #
    # The variables
    # ------------------------------------------------------------------------ #
    # TODO: set variables
    
    variable_names = [str(i)+str(j) for j in range(len(col_limits))
     for i in range( len(row_limits))]
    variable_names.sort()
    print("Variable Indices:", variable_names)

    DV_variables = LpVariable.matrix("X", variable_names, cat = "Integer", lowBound= 0 )
    allocation = np.array(DV_variables).reshape(len(row_limits),len(col_limits))
    print("Decision Variable/Allocation Matrix: ")
    # ------------------------------------------------------------------------ #
    # The objective function
    # ------------------------------------------------------------------------ #
    # TODO: write the objective function
    #obj_func = lpSum(allocation)
    #print(obj_func)
    #prob +=  obj_func
    #print(prob)
    obj_func=0
    for i in range(len(row_limits)):
        for j in range(len(col_limits)):
            if (i, j) in adm_cells:
                obj_func += lpSum(allocation[i][j])
    print(obj_func)
    prob += obj_func
    print(prob)
    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #
    # TODO: write constraints
    for i in range(len(row_limits)):
        print(lpSum(allocation[i][j] 
        for j in range(len(col_limits))if (i,j) in adm_cells) <= row_limits[i])
        prob += lpSum(allocation[i][j] 
        for j in range(len(col_limits))if (i,j) in adm_cells) <= row_limits[i] , "rows Constraints " + str(i)
    
    for j in range(len(col_limits)):
        print(lpSum(allocation[i][j] 
        for i in range(len(row_limits))if (i,j) in adm_cells) >= col_limits[j])
        prob += lpSum(allocation[i][j] 
        for i in range(len(row_limits))if (i,j) in adm_cells) >= col_limits[j] , "Demand Constraints " + str(j)
        
   
    #je veux ecrire sum des j allant jusqu a n des xij <= a li
    #Yt = (1.0/(M*N)) * sum([Y[i][j] for i in range(M) for j in range(N)])
    return prob,allocation


# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #
def solve_admissible_cells(adm_cells, row_limits, col_limits):
    """TODO: Description."""
    # ------------------------------------------------------------------------ #
    # Set data
    # ------------------------------------------------------------------------ #
    # TODO: set data

    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    prob, allocation = set_model_name(adm_cells, row_limits, col_limits)
    # Coin Branch and Cut solver is used to solve the instanced model
    # TODO: change the log path file
    prob.solve(
        PULP_CBC_CMD(
            msg=False, logPath=Path('./CBC_log.log'),
        ),
    )
    # ------------------------------------------------------------------------ #
    # Print the solver output
    # ------------------------------------------------------------------------ #
    print_log_output(prob,allocation)


# ============================================================================ #
#                                   UTILITIES                                  #
# ============================================================================ #
def print_log_output(prob: LpProblem,allocation):
    """Print the log output and problem solutions."""
    print()
    print('-' * 40)
    print('Stats')
    print('-' * 40)
    print()
    print(f'Number variables: {prob.numVariables()}')
    print(f'Number constraints: {prob.numConstraints()}')
    print()
    print('Time:')
    print(f'- (real) {prob.solutionTime}')
    print(f'- (CPU) {prob.solutionCpuTime}')
    print()

    print(f'Solve status: {LpStatus[prob.status]}')
    print(f'Objective value: {prob.objective.value()}')

    print()
    print('-' * 40)
    print("Variables' values")
    print('-' * 40)
    print()
    # TODO: you can print variables value here

    print("Total Cost:", prob.objective.value())

# Decision Variables

    for v in prob.variables():
        try:
            print(v.name,"=", v.value())
        except:
            print("error couldnt find value")

    for i in range(len(row_limits)):
        print("Warehouse ", str(i+1))
        print(lpSum(allocation[i][j].value() for j in range(len(col_limits))))

if __name__ == '__main__':

    for adm_cells, row_limits, col_limits in get_adm_cells_data():
        # adm_cells: list of tuple (row_i, col_j)
        # corresponding to admissible cells
        # row_limits: list of row limits (int)
        # col_limits: list of column limits (int)
        solve_admissible_cells(adm_cells, row_limits, col_limits)
