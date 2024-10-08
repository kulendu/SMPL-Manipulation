## Installing packages
You can install [Gpytoolbox](https://gpytoolbox.org/), [Polyscope](https://polyscope.run/py), [Numpy](https://numpy.org/), and [Scipy](https://scipy.org/) into your venv/conda using the console command:

```sh
python -m pip install numpy==1.26.4 scipy==1.13.1 gpytoolbox==0.2.0 polyscope==2.2.1
```

# NumPy for geometry processing
## Defining vectors and matrices
The basic data type in numpy is an array with `k` axes. If `k==1`, then we have a vector.
```py
import numpy as np
u = np.array([1., 2.])
print(u)
```
This prints:
```
[1. 2.]
```

If `k==2`, we have a matrix, which we specify in row major order (i.e., the matrix is an array of rows),
```py
import numpy as np
A = np.array([[1., 2.], [3., 4.], [5., 6.]])
print(A)
```
This prints:
```
[[1. 2.]
 [3. 4.]
 [5. 6.]]
 ```

### Elementwise arithmetic
Using the arithmetic operators `+`, `-`, `*`, `/` and `**` on numpy arrays (i.e., vectors and matrices), results in elementwise operations. This is different from MATLAB, where, for example, * will perform a matrix multiplication. In order to perform an elementwise operation, your operands must be two array of compatible sizes, or an array and a scalar. So, the following elementwise operations are legal:
```py
import numpy as np
A = np.array([[1., 2.], [3., 4.], [5., 6.]])
B = np.array([[13., 14.], [15., 16.], [17., 18.]])
print(f"A+B: {A+B}")
print(f"B*A: {B*A}")
print(f"A-3: {A-3}")
print(f"1./A: {1./A}")
```
This prints:
```
A+B: [[14. 16.]
 [18. 20.]
 [22. 24.]]
B*A: [[ 13.  28.]
 [ 45.  64.]
 [ 85. 108.]]
A-3: [[-2. -1.]
 [ 0.  1.]
 [ 2.  3.]]
1./A: [[1.         0.5       ]
 [0.33333333 0.25      ]
 [0.2        0.16666667]]
 ```

 ### Matrix arithmetic
 There are a variety of mathematic operations in NumPy that are specific to matrices. **Matrix multiplication** is performed via the `@` operator or the `dot()` function:
```py
import numpy as np
A = np.array([[1., 2.], [3., 4.], [5., 6.]])
u = np.array([7., 8.])
print(f"A@u matrix multiplication: {A@u}")
```
This prints: 
```
A@u matrix multiplication: [23. 53. 83.]
```
The **transpose** of a matrix can be taken with the simple `.T` operator:
```py
import numpy as np
A = np.array([[1., 2.], [3., 4.], [5., 6.]])
print(f"Transpose A.T: {A.T}")
```
This prints:
```
Transpose A.T: [[1. 3. 5.]
 [2. 4. 6.]]
```

Finally, the Frobenius norm of a matrix (and the Euclidean norm of a vector) can be computed with the `np.linalg.norm` function:

```python
import numpy as np
A = np.array([[1., 2.], [3., 4.], [5., 6.]])
u = np.array([7., 8.])
print(f"||A||_F = {np.linalg.norm(A)}")
print(f"||u|| = {np.linalg.norm(u)}")
```

This prints:
```
||A||_F = 9.539392014169456
||u|| = 10.63014581273465
```

### Sparse matrices
When dealing with very large matrices where most entries are zero, it is usually advisable to not use a `np.array`. A normal `np.array` stores every single entry of the matrix, wasting a lot of memory for just zeros. In the case where we know that a matrix consists mostly of zeros, we want to use a sparse matrix instead.

SciPy has many sparse matrix formats and many ways to define them. The simplest, in my opinion, is to use triplets: With triplets, we specify all entries of a matrix that are nonzero in three lists: the row, the column, and the value. Given three arrays `i`, `j`, `k` of equal length $n$

$ A(i[a], j[a]) = k[a],  \forall a = 0,1,...n $

We construct a matrix from these triplet lists like this:

```py
import numpy as np, scipy as sp
i = np.array([0,1,1,2])
j = np.array([0,1,2,2])
k = np.array([1., -1., -2., 1.])
A = sp.sparse.csr_matrix((k, (i,j)), shape=(3,3)) #the shape tuple is the dimension of A
print(f"A = {A.todense()}")
```

This prints:
```
A = [[ 1.  0.  0.]
 [ 0. -1. -2.]
 [ 0.  0.  1.]]
 ```