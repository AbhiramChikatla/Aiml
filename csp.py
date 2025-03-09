def is_consistent(assignment, variable, value, constraints):
    # Check if the value assignment is consistent with the constraints
    for constraint in constraints:
        if not constraint(assignment, variable, value):
            return False
    return True

def backtrack(assignment, variables, domains, constraints):
    if len(assignment) == len(variables):
        return assignment  # All variables are assigned
    
    # Select an unassigned variable
    variable = select_unassigned_variable(variables, assignment)
    
    for value in domains[variable]:
        if is_consistent(assignment, variable, value, constraints):
            # Assign the value to the variable
            assignment[variable] = value
            
            # Recursively try to complete the assignment
            result = backtrack(assignment, variables, domains, constraints)
            if result:
                return result
            
            # If not successful, remove the assignment
            assignment.pop(variable)
    
    return None  # Trigger backtracking

def select_unassigned_variable(variables, assignment):
    for variable in variables:
        if variable not in assignment:
            return variable

def example_constraint(assignment, variable, value):
    # Example: All variables must have different values
    for var, val in assignment.items():
        if val == value:
            return False
    return True

if __name__ == "__main__":
    # Define variables
    variables = ['X1', 'X2', 'X3']
    
    # Define domains
    domains = {
        'X1': [1, 2, 3],
        'X2': [1, 2, 3],
        'X3': [1, 2, 3]
    }
    
    # Define constraints
    constraints = [example_constraint]
    
    # Solve CSP
    assignment = {}
    solution = backtrack(assignment, variables, domains, constraints)
    
    if solution:
        print("Solution found:", solution)
    else:
        print("No solution exists")




# # AIM:
# Implement the Constraint Satisfaction problem using backtracking
# DESCRIPTION:
# A Constraint Satisfaction Problem (CSP) consists of a set of variables, each with a domain of values, and a set of
# constraints that specify which combinations of values are acceptable. The goal of CSP is to find an assignment of
# values to variables that satisfies all the constraints.
# Backtracking is a common algorithmic technique used to solve CSPs. It incrementally builds candidates for the
# solution and abandons a candidate as soon as it determines that the candidate cannot possibly lead to a valid
# solution.
# ALGORITHM:
# 1. Input:
#  A set of variables X={X1,X2,...,Xn}X = \{X_1, X_2, \ldots, X_n\}X={X1,X2,...,Xn}.
#  A set of domains D={D1,D2,...,Dn}D = \{D_1, D_2, \ldots, D_n\}D={D1,D2,...,Dn} where each
# DiD_iDi is the set of possible values for XiX_iXi.
#  A set of constraints C={C1,C2,...,Cm}C = \{C_1, C_2, \ldots, C_m\}C={C1,C2,...,Cm} where each
# constraint specifies allowable combinations of values for a subset of variables.
# 2. Initialization:
#  Start with an empty assignment.
# 3. Backtracking Procedure:
#  Select an unassigned variable: Choose a variable XiX_iXi that is not yet assigned a value.
#  Order domain values: Select an ordering of the values in the domain DiD_iDi to assign to XiX_iXi.
#  Assign value: Assign a value vvv from the domain DiD_iDi to the variable XiX_iXi.
#  Check constraints: If the assignment is consistent with the constraints (i.e., no constraint is violated),
# proceed.
#  If the assignment is not consistent, backtrack by unassigning XiX_iXi and try the next value in DiD_iDi.
#  Recursive call: Recursively assign values to the remaining variables.
#  Return: If all variables are assigned and all constraints are satisfied, return the solution. If no valid
# assignment is found, backtrack.
# 4. Output:
#  A complete assignment of values to variables that satisfies all constraints or a failure indication if no
# such assignment exists.