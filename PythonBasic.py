1. List vs Tuple
    List is mutable
    Tuple is immutable

2. Memory for objects
    int takes 24 bytes
    float takes 24 bytes
    empty str takes 37 bytes, additional characters add one bytes

3. limitation of Python 
    Design restriction 
    slow when compared with C/C++/JAVA
    weak in mobile computing
    underdeveloped database access layers
    dont compile, so more runtime errors

4. break and continue
    break stops the loop
    continue jumps to the next iteration
    pass just pass the statement, and continue the rest of the part in one loop

5. eval
    eval() Parses a string as an expression.

6. set & dictionary
    dictionary key-value pairs and mutable
    set is mutable

7. math operators
    // floor division
    ** performs exponentiation
    % is for modulus
    2^3 = 1 ^ is XOR
    1<<1 = 2 This shifts the bits to the left by the specified amount
    5>>1 = 2 binary right shifts

8. zip, enumerate, 
    zip returns an iterator of tuples: list(zip(['a','b','c'],[1,2,3])) -> [(‘a’, 1), (‘b’, 2), (‘c’, 3)]
    enumerate returns an iterator of index and values

8. with statement
    It may be used to open a file, do something, and then automatically close the file at the end.

9. map, reduce, and filter
    Map applies a function to every element in an iterable.
    list(map(lambda x:x**2,range(8))) -> [0, 1, 4, 9, 16, 25, 36, 49]

    Reduce repeatedly reduces a sequence pair-wise until we reach a single value.
    reduce(lambda x,y:x-y,[1,2,3,4,5]) -> -13

    Filter lets us filter in some values based on conditional logic.
    list(filter(lambda x:x>5,range(8))) -> [6, 7]

10. try, except, else, finally
    try: try the block
    except: if it has error
    else: when try doesnt raise any error
    finally: execute this part anyway

11. shallow copy and deep copy
    shallow copy: only copy the reference, if we make a change in the copy, it will affect the original object. 
    deep copy: copy the object. if you make a change to a copy of an object, it won’t affect the original object.

12. generator and iterator
    generator: we create a function and use yield to return result. 
    a generator will save the stats of local variables when yield pause the loop, 
    fast, compact, and simpler

    iterator: we use iter() or next(), memory efficient

13. decorator
    A decorator is a function that adds functionality to another 
    function without modifying it. It wraps another function to add functionality to it.

14. instance, staticmethod & classmethod
    instance: it takes self as input, it can freely access attributes and methods on the same object
            can modify object state and class state
    classmethod: it takes cls as input that point to the class not the object instance, 
            if you need to create a class instance or use a static method within the function
            can only modify class state
    staticmethod: you can consider it as a normal function that exists in a class
            cannot modify state

15. *args and **kwargs:
    *args means arguments, this will pass the values to variables in the order
    **kwargs means keyword arguments, this will pass the values to variables according to its key

16. garbage collection (gc):
    Reference counting works by counting the number of times an object is referenced by other objects
    in the system. When the reference count becomes zero the object is deallocated.
    Python maintains a count of how many references there are to each object in memory
    When a reference count drops to zero, 
    it means the object is dead and Python can free the memory it allocated to that object
    The garbage collector looks for reference cycles and cleans them up

17. monte carlo simulation
    randomly select (unbiased) for a large number of samples
    a. randomness
    b. large sample size

    according to the law of large number, 
    we believe the estimation from these samples is getting closer to the true value
    the average result of samples will getting closer to the expected value

18. JSON
    JSON stands for JavaScript Object Notation
    A collection of <name,value> pairs
    An ordered list of values
    it is a dictionary in Python 

19. Pickle
    serialize a python object structure

20. Python is call-by-object reference
    '''
    >>> item='milk'
    >>> groceries=[]
    >>> groceries.append(item)
    >>> items=groceries
    >>> item='cheese'
    >>> items.append(item)
    >>> groceries, item
    >>> ([‘milk’, ‘cheese’], [‘milk’, ‘cheese’])
    '''

21. Abstract Class
    An abstract method is a method that is declared, 
    but contains no implementation. 
    Abstract classes may not be instantiated, 
    and its abstract methods must be implemented by its subclasses.

22. correlation
    it refers to the degree which the pair of variables are linearly related

23. PCA
    dimension reduction method
    eigendecomposition on covariance matrix
    it preserves as much variance as possible
    uncorrelated principal components
    it is a way to reduce the effect of collinearity

24. eigenvalue and eigenvector
    matrix diagonalization
    an eigenvector, corresponding to a real nonzero eigenvalue, 
    points in a direction in which it is stretched by the transformation 
    and the eigenvalue is the factor by which it is stretched. 
    If the eigenvalue is negative, the direction is reversed.

25. logistic regression vs SVM
    SVM: Try to maximize the margin between the closest support vectors
    LR: Maximize the posterior class probability

    SVM is deterministic while LR is probabilistic.
    For the kernel space, SVM is faster

26. 由均匀分布的变量生成几何分布的变量并验证正确性
    用inverse transfom method, 先算出geometric distri. 的inverse cdf
    在帶入uniform distribution

    用rejection sampling:
    持續 random.uniform() / p 如果小於 1，
    則繼續迭帶，且每次加上 1 次的失敗
    最後成功的時候，輸出失敗+1 (成功) 的次數
    