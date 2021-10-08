from pulp import lpSum, LpMaximize, LpVariable, LpProblem
a=[(i,j) for i in range(6) for j in range(6) if i<2]
print(a)
variable = [LpVariable(f'x_{i}{j}', lowBound=0) 
     for i in range(6) 
     for j in range(6) 
     
     if((i,j) in a)
]
c=[i for i in range(6)]
r=[i for i in range(2)]
print(c)
print(variable)
prob = LpProblem(name='name', sense=LpMaximize)
prob += lpSum(
         element for element in enumerate(variable)
), 'Objective'
print(prob)

for i in range(len(a)):
    if(a[i] (i,1)) :
        print(a[i])

#print(prob)

  
for i in range(r):
    print(lpSum(allocation[i][j] for j in range(n_customers)) 
    <= warehouse_supply[i])
    model += lpSum(allocation[i][j] for j in range(n_customers))
     <= warehouse_supply[i] , "Supply Constraints " + str(i))