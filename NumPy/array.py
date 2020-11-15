import numpy as np

#declearing arrray
a = np.array([1,3,5,9])
b = np.array([[1,3,4,5,7.5],[3,5,1,6,9]])
c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])


#get dimension
# print(a.ndim)
# print(b.ndim)

#get shape
# print(a.shape)
# print(b.shape)

#get type
# print(a.dtype)
# print(b.dtype)

#get size
# print(a.itemsize)
# print(b.itemsize)

# get total size
# print(a.size * a.itemsize)
     #  or
# print(a.nbytes)    


# get specific element of an 2d array
#print(b[1,3]) #we can use negative index as well


# get a specific row
# print(c[1,:])


#get specific column
# print(c[:,3])


#getting a fancy like [row, startindex:endindex:stepsize]
# print(c[0, 1:6:2])


#assigning values to arrays
# print(c,"\n")

# c[1,5] = 20
# print(c,"\n")

# c[0, 1:6:2] = [0,0,0]
# print(c,"\n")

# a[:2] = [-1,-1]
# print(a,"\n")




#example of 3d array

d = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
    ])
# print(d,"\n")

# #accessign element of 3d array
# print(d[1,1,0])

# print(d[:,1,:])

#assigning values in 3d array
# d[:,1,:] = [[9,9],[9,9]]
# print(d,"\n")



#all 0 matrix np.zeros(shape)
#print(np.zeros((2,3)))

#all 1 matrix np.ones(shape)
#print(np.ones((2,3)))

#any other matrix np.full(shape, value)
# print(np.full((2,3), 99))


#similar as other array but value different
# print(np.full(a.shape,4))
#                 #or
# print(np.full_like(a,4))



#random decimal numbers
# print(np.random.rand(3,4))
#            #or
# print(np.random.random_sample(a.shape))    #have tu use random_sample for getting shape from a sample array       


#random integer value
# print(np.random.randint(2,7, size=(2,3)))




#identity matrix
# print(np.identity(4))


#repeat an existing array
# arr = np.array([[1,2,3]])
# print(np.repeat(arr,3, axis=0))


#challenge output=[[1. 1. 1. 1. 1.]
#                  [1. 0. 0. 0. 1.]
#                  [1. 0. 9. 0. 1.]
#                  [1. 0. 0. 0. 1.]
#                  [1. 1. 1. 1. 1.]]

# x = np.ones((5,5))
# x[1:-1, 1:-1] = 0
# x[2,2] = 9

# print(x)


#copying an array........ if we write y=x that copies the address from x to y and if we change y[0] = 10 it's change the y value also

# x = np.array([1,2,3])
# y = x.copy()
# print(y)



#arithmetic operation in array
# m = np.array([1,2,3])
# n = np.array([4,5,6])
# print(m+2)
# print(m**2)
# print(m+n)
# print(np.sin(a))
# print(np.cos(a))


#linear algebra

# x = np.ones((2,3))
# y = np.full((3,2),2)
# #form matrix multiplication we have to use np.matmul(matrix1, matrix2)
# print(np.matmul(x,y))


#finding the determinant
# x = np.random.randint(1,10, size=(3,3))

# print(np.linalg.det(x))



#statistics
# print(np.min(c))
# print(np.max(c))
# print(np.sum(c, axis=0))



#reorganizing arrays
# before = np.array([[1,2,3,4],[5,6,7,8]])
# after = before.reshape((4,2))
# print(after)



# #vertically stacking arrays
# v1 = np.array([1,2,3,4])
# v2 = np.array([5,6,7,8])
# print(np.vstack([v2,v2, v1, v2, v2]))


#horizontal stacking arrays
# v1 = np.array([1,2,3,4])
# v2 = np.array([5,6,7,8])
# print(np.hstack([v2,v2, v1, v2, v2]))



#miscellaneous

#getting data from a file

# file = np.genfromtxt('data.txt', delimiter=',')
# file = file.astype('int32')
# print(file)


#boolean masling and  advanced indexing
file = np.genfromtxt('data.txt', delimiter=',')
file = file.astype('int32')
print(file > 50)
print(file[file > 50])
print(np.any(file > 50 , axis=0))
print(np.all(file > 50 , axis=0))
print((file > 50) & (file < 100))
print(~(file > 50) & (file < 100)) # ~ similar as !
