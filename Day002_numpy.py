#Day002: numpy (numerical python)
"""
numpy - python library used to work with numerical data.
It includes functions and data structures that can perform a wide variety 
of mathematical operations.
mport numpy as np
"""
import numpy as np
dir(np)
help(np.product)

"""
python - list
numpy array:
    are fatser and more compact than python lists.
    np.array - function to convert list to numpy array
"""
list1 = [1,6,4,3,2]
np.array(list1)
list1
list1[1]

"""
Numpy arrays are homogeneous - means they can contain single data types
while list can store multiple datatypes.
"""
list2 = [3,5,7,'first','jhik',8]
list2
np.array(list2)

"""
numpy arrays - ndarrays means n-dimensinal arrays
.ndim - returns dimension of the array
.size - returns total number of elements
.shape - returns a tuple of integers that indicates the number of elemets 
stored along each dimension of the array.
"""
x = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10,11,12]]])
print(x[1][1][2])
x.ndim
x.size
x.shape

#Adding, sorting and removing in an ndarray:
"""
append() - adds an element to an ndarray at last
delete() - deletes an element from any index(posiion)
sort() - arranges an ndarray in ascending order
arange() - allows to create an array that contains a range of evenly spaced 
intervals, similar to range in python.
reshape() - allows to change the shapoe of our ndarray, while reshaping an 
array the number of elements should be same in both.
"""
x = np.array([2, 3, 1])

x = np.append(x, 4)
print(x)

x = np.delete(x, 1)
print(x)

x = np.sort(x)
print(x)

y = np.arange(6)
print(y)

z = np.arange(3,16,4)
print(z)

y = y.reshape(3,2)
print(y)

a = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
a = a.reshape(4,3)
print(a)

b = np.array([1,2,3,4,5,6,7,8,9])
b = b.reshape(9)
print(b)
b = b.flatten() #flatten converts an ndarray into 1D array
print(b)

#Indexing and slicing:
num = np.arange(2,15)
print(num)
print(num[:9:2])
print(num[3:])
print(num[0:5])
print(num[-4:]) #only left to right so backward slicing not possible.
print(len(num)) #.size will give the same result
num.size
print(num[-1:]) #will give last element in a list
print(num[-1]) #will give last element as a sepertae numeric value

#Conditions:
"""
For variables we used to use &, | to establish conditions which will be an 
array of boolean values showing whether or not the values in the array 
fulfill the condition
y = (x>5) & (x%2==0)
In numpy, we can provide these conditions inside index to select the 
elements which fullfills the given condiion.
"""
num1 = np.arange(3,18)
print(num1)
print(num1[num1<8]) #numbers lesser than 8
print(num1[(num1>4) & (num1%2 != 0)]) #odds greater than 4

#Array operations:
num2 = np.arange(4,28,3)
print(num2)
print(num2.sum()) #sum() function to find sum of all elements
print(num2.min()) #min() function to find minimum value from the entire array
print(num2.max()) #max() function to find maximum value from the entire array
num2 = num2+2
"""performing mathematical operations will effect each element of the array, 
this is called as broadcasting because numpy understands that given operation
should be performed with each element
"""
print(num2)

#Statistics:
series = np.array([170,182,192,168,171,172,192,166,193])
print(np.mean(series)) #mean
print(np.median(series)) #median
print(np.var(series)) #variance
print(np.std(series)) #standard deviation
print('range is: '+'('+str(np.mean(series)-np.std(series))+', '+str(np.mean(series)+np.std(series))+')')

#code challenge:
#House Prices: one std from the mean
import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
dev = np.std(data)
mean = np.mean(data)
list1 = []
for num in data1:
    if mean - dev < num < mean + dev:
        list1.append(num)
print(list1)
print((len(list1)/len(data))*100)
