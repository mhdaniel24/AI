'''
v1 and v2 are a dictionary representation of a mathematical vector.
Returns the dot product of vectors v1 and v2.
'''
def dotProduct(v1, v2):
    result = 0
    
    for dim in v1:
        if dim in v2:
            result = result + v1[dim]*v2[dim]

return result

'''
c is an integer
v is a dictionary representation of a vector
Returns the scalar multiplication of constant c and vector v
'''
def scalarMult(c, v):
    cv = {}
    
    for dim in v:
        cv[dim] = v[dim] * c
    
    return cv

'''
v1 and v2 are dictionary representations of vectors
This function assumes that vectors v1 and v2 have the same exact dimensions
Returns the sum of vectors v1 and v2
'''
def vectorSum(v1, v2):
    sum = {}
    
    for dim in v1:
        sum[dim] = v1[dim] + v2[dim]
    
    return sum