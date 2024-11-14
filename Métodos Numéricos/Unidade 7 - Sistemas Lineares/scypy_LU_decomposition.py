import scipy
import scipy.linalg

A = scipy.array([[2, 0, 1],
                 [0, 2, 1],
	         [1, 1, 3]])

P, L, U = scipy.linalg.lu(A)
print (P)
print (L)
print (U)


