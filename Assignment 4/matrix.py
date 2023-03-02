#--------------------------
# Joseph Myc | 160 740 900
# CP460 (Fall 2019)
# Assignment 4
#--------------------------

import math
import string
import mod

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  checks if the given input is a valid vector
#               A valid vector is a list in which all elements are integers
#               An empty list is a valid vector
# Errors:       None
#-----------------------------------------------------------
def is_vector(A):
    if not isinstance(A, list):
        return False
        
    for val in A:
        if not isinstance(val, int):
            return False
    return True

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  checks if the given input is a valid matrix
#               A matrix is a list in which all elements are valid vectors of equal size
#               Any valid vector is also a valid matrix
# Errors:       None
#-----------------------------------------------------------
def is_matrix(A):
    if not isinstance(A, list):
        return False
    
    if len(A) == 0:
        return True

    #Multiple Vectors
    if isinstance(A[0], list):
        leng = len(A[0])

        for val in A:

            if not isinstance(val, list) or len(val) != leng:
                return False

            for val2 in val:
                if not isinstance(val2, int):
                    return False

    #Single vector
    else:
        for val in A:
            if not isinstance(val, int):
                    return False

    return True

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       None
# Description:  Prints a given matrix, each row on a separate line
# Errors:       If A not a matrix --> print 'Error (print_matrix): Invalid input'
#-----------------------------------------------------------
def print_matrix(A):
    if not isinstance(A, list):
        print("Error (print_matrix): Invalid input")
        return
    
    if len(A) == 0:
        print("[]")
        return

    #Multiple Vectors
    if isinstance(A[0], list):

        for val in A:
            print(val)

    #Single vector
    else:
        print(A)
    return 

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       number of rows (int)
# Description:  Returns number of rows in a given matrix
# Examples:     [5,3,2] --> 1
#               [] --> 0
#               [[1,2],[3,4],[5,6]] --> 3
# Errors:       If A not a matrix -->
#                   return 'Error (get_rowCount): invalid input'
#-----------------------------------------------------------
def get_rowCount(A):
    if not is_matrix(A):
        
        return "Error (get_rowCount): invalid input"
    
    if len(A) == 0:
        return 0

    #Multiple Vectors
    if isinstance(A[0], list):
        return len(A)

    #Single vector
    else:
        return 1

    return 

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       number of columns (int)
# Description:  Returns number of columns in a given matrix
# Examples:     [5,3,2] --> 3
#               [] --> 0
#               [[1,2],[3,4],[5,6]] --> 2
# Errors:       If A not a matrix -->
#                   return 'Error (get_columnCount): invalid input'
#-----------------------------------------------------------
def get_columnCount(A):
    if not is_matrix(A):
        return "Error (get_columnCount): invalid input"
    
    if len(A) == 0:
        return 0

    #Multiple Vectors
    if isinstance(A[0], list):
        return len(A[0])

    #Single vector
    else:
        return len(A)

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       [number of rows (int), number of columns(int)]
# Description:  Returns number size of matrix [rxc]
# Examples:     [5,3,2] --> [1,3]
#               [] --> [0,0]
#               [[1,2],[3,4],[5,6]] --> [3,2]
# Errors:       If A not a matrix -->
#                   return 'Error (get_size): invalid input'
#-----------------------------------------------------------
def get_size(A):
    if is_matrix(A) == False:
        return "Error (get_size): invalid input"
    
    return [get_rowCount(A), get_columnCount(A)]

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  Checks if given input is a valid square matrix
# Examples:     [] --> True
#               [10] --> True
#               [[1,2],[3,4]] --> True
#               [[1,2],[3,4],[5,6]] --> False
# Errors:       None
#-----------------------------------------------------------
def is_square(A):
    
    if len(A) == 0:
        return True

    #Multiple Vectors
    if isinstance(A[0], list):
        if len(A) == len(A[0]) and is_matrix(A):
            return True

    #Single vector
    else:
        if len(A) == 1 and is_matrix(A):
            return True

    return False

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               i (row number)
# Return:       row (list)
# Description:  Returns the ith row of given matrix
# Examples:     ([],0) --> Error
#               ([10],0) --> [10]
#               ([[1,2],[3,4]],0) --> [1,2]
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error (get_row): invalid input matrix'
#               If i is outside the range [0,#rows -1] -->
#                   return 'Error (get_row): invalid row number'
#-----------------------------------------------------------
def get_row(A,i):
    if not is_matrix(A):
        return "Error (get_row): invalid input matrix"
    if i >= len(A):
        return "Error (get_row): invalid row number"

    return A[i]

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               j (column number)
# Return:       column (list)
# Description:  Returns the jth column of given matrix
# Examples:     ([],0) --> Error
#               ([10],0) --> [10]
#               ([[1], [2]],0) --> [[1], [2]]
#               ([[1,2],[3,4]],1) --> [2,4]
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error (get_column): invalid input matrix'
#               If i is outside the range [0,#rows -1] -->
#                   return 'Error (get_column): invalid column number'
#-----------------------------------------------------------
def get_column(A,j):
    if not is_matrix(A):
        return "Error (get_column): invalid input matrix"
    
    if len(A) == 0:
        return "Error"

    #Multiple Vectors
    if isinstance(A[0], list):
        if len(A[0]) <= j:
            return "Error (get_column): invalid column number"

        array = []
        for i in range(len(A)):
            array.append([A[i][j]])

        return array

    #Single vector
    else:
        if 0 < j:
            return "Error (get_column): invalid column number"
        return A[j]
    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               i (row number)
#               j (column number)
# Return:       element
# Description:  Returns element (i,j) of the given matrix
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error (get_element): invalid input matrix'
#               If i or j is outside matrix range -->
#                   return 'Error (get_element): invalid element position'
#-----------------------------------------------------------
def get_element(A,i,j):
    if len(A) == 0 or not is_matrix(A):
        return 'Error (get_element): invalid input matrix'

    if i >= len(A) or j >= len(A[0]):
        return 'Error (get_element): invalid element position'

    return A[i][j]

#-----------------------------------------------------------
# Parameters:   r: #rows (int)
#               c: #columns (int)
#               pad (int)
# Return:       matrix
# Description:  Create an empty matrix of size r x c
#               All elements are initialized to integer pad
# Error:        r and c should be positive integers
#               (except the following which is valid 0x0 --> [])
#                   return 'Error (new_matrix): invalid size'
#               pad should be an integer
#                   return 'Error (new_matrix): invalid pad'
#-----------------------------------------------------------
def new_matrix(r,c,pad):
    if not isinstance(r, int) or r < 0 or not isinstance(c, int) or c < 0 or (r==0 and c>0):
        return 'Error (new_matrix): invalid size'

    if not isinstance(pad, int):
        return 'Error (new_matrix): invalid pad'

    if r == 1:
        return [pad for i in range(c)]
        
    else:
        return [[pad]*c for i in range(r)]
        

#-----------------------------------------------------------
# Parameters:   size (int)
# Return:       square matrix (identity matrix)
# Description:  returns the identity matrix of size: [size x size]
# Examples:     0 --> Error
#               1 --> [1]
#               2 --> [[1,0],[0,1]]
# Errors        size should be a positive integer
#                   return 'Error (get_I): invalid size'
#-----------------------------------------------------------
def get_I(size):
    if size < 1:
        return 'Error (get_I): invalid size'
    if size == 1:
        return [1]

    sqMatrix = new_matrix(size,size,0)
    for i in range(size):
        sqMatrix[i][i] = 1
    return sqMatrix

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  Checks if given input is a valid identity matrix
#-----------------------------------------------------------
def is_identity(A):
    if is_square(A):
        compArray = get_I(len(A))
        if A == compArray:
            return True
            
    return False

#-----------------------------------------------------------
# Parameters:   c (int)
#               A (matrix)
# Return:       a new matrix which is the result of cA
# Description:  Performs scalar multiplication of constant c with matrix A
# Errors:       if A is empty or not a valid matrix or c is not an integer:
#                   return 'Error(scalar_mul): invalid input'
#-----------------------------------------------------------
def scalar_mul(c, A):
    if not isinstance(c, int) or not is_matrix(A) or len(A) == 0:
        return 'Error(scalar_mul): invalid input'

    
    if isinstance(A[0], list):
        B = new_matrix(len(A), len(A[0]), 0)
        for i in range(len(A)):
            for j in range(len(A[0])):
                B[i][j] = A[i][j] * c

    else:
        B = new_matrix(len(A), 1, 0)
        for i in range(len(A)):
            B[i] = A[i]*c
    return B

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               B (matrix)
# Return:       a new matrix which is the result of AxB
# Description:  Performs cross multiplication of matrix A and matrix B
# Errors:       if eithr A or B or both is empty matrix nor not a valid matrix
#                   return 'Error(mul): invalid input'
#               if size mismatch:
#                   return 'Error(mul): size mismatch'
#-----------------------------------------------------------
def mul(A,B):
    if len(A) == 0 or len(B) == 0 or not is_matrix(A) or not is_matrix(B):
        return 'Error(mul): invalid input'
    if get_columnCount(A) != get_rowCount(B):
        return 'Error(mul): size mismatch'

    mulArray = new_matrix(get_rowCount(A), get_columnCount(B), 0)

    if (is_vector(A) and is_vector(B)):
        for i in range(get_rowCount(A)):
            for j in range(get_columnCount(B)):        
                mulArray[i] += A[i]*B[j]

    elif (is_vector(A)):
        for i in range(get_rowCount(A)):
            for j in range(get_rowCount(B)):
                    mulArray[i] += A[j] * B[j][i]

    elif (is_vector(B)):
        for i in range(get_rowCount(B)):
            for j in range(get_rowCount(A)):
                mulArray[i] += A[j][i] * B[j]

    else:
        for i in range(get_rowCount(A)):
            for j in range(get_columnCount(B)):
                for k in range(get_rowCount(B)):                
                    mulArray[i][j] += A[i][k]*B[k][j]

    return mulArray

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               m (int)
# Return:       A` (matrix)
# Description:  Returns matrix A such that each element is the 
#               residue value in mod m
# Errors:       if A is empty matrix or not a valid matrix
#                   return 'Error(matrix_mod): invalid input'
#               if m is not a positive integer:
#                   return 'Error(matrix_mod): invalid mod'
#-----------------------------------------------------------
def matrix_mod(A,m):
    if not is_matrix(A) or len(A) == 0:
        return 'Error(matrix_mod): invalid input'

    if m < 1:
        return 'Error(matrix_mod): invalid mod'

    if isinstance(A[0], list):
        B = new_matrix(len(A), len(A[0]), 0)
        for i in range(len(A)):
            for j in range(len(A[0])):
                B[i][j] = mod.residue(A[i][j], m)
            
    else:
        B = new_matrix(len(A), 1, 0)
        for i in range(len(A)):
            B[i] = mod.residue(A[i], m)

    return B

#-----------------------------------------------------------
# Parameters:   A (matrix)
# Return:       determinant of matrix A (int)
# Description:  Returns the determinant of a 2x2 matrix
# Errors:       if A is empty matrix nor not a valid square matrix
#                   return 'Error(det): invalid input'
#               if A is square matrix of size other than 2x2
#                   return 'Error(det): Unsupported matrix size'
#-----------------------------------------------------------
def det(A):
    if not is_square(A) or len(A) == 0:
        return 'Error(det): invalid input'
    if get_rowCount(A) != 2 or get_columnCount(A) != 2:
        return 'Error(det): Unsupported matrix size'

    return (A[0][0]*A[1][1]) - (A[1][0]*A[0][1])

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               m (int)
# Return:       a new matrix which is the inverse of A mode m
# Description:  Returns the inverse of a 2x2 matrix in mode m
# Errors:       if A is empty matrix or not a valid matrix
#                   return 'Error(inverse): invalid input'
#               if A is not a square matrix or a matrix of 2x2 with no inverse:
#                   return 'Error(inverse): matrix is not invertible'
#               if A is a square matrix of size other than 2x2
#                   return 'Error(inverse): Unsupported matrix size'
#               if m is not a positive integer:
#                   return 'Error(inverse): invalid mod'
#-----------------------------------------------------------
def inverse(A,m):
    if not is_matrix(A) or len(A) == 0:
        return 'Error(inverse): invalid input'
    if not is_square(A):
        return 'Error(inverse): matrix is not invertible'
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    if mod.mul_inv(det, m) == "NA":
        return 'Error(inverse): matrix is not invertible'
    if get_rowCount(A) != 2 or get_columnCount(A) != 2:
        return 'Error(inverse): Unsupported matrix size'
    if m < 1:
        return 'Error(inverse): invalid mod'
    
    

    detInv = mod.mul_inv(det, m)
    B = new_matrix(2, 2, 0)

    B[0][0] = (A[1][1] * detInv) % m
    B[0][1] = (A[0][1]*-1*detInv) % m
    B[1][0] = (A[1][0]*-1*detInv) % m
    B[1][1] = (A[0][0] * detInv) % m
    
    return B
