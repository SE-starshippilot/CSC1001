#  Assignment 3 report

## Question 1

1. Code saved in [q3-1.py](q3-1.py)
2. The program constructs a class flower. User can acquire/ modify its name, petal number and price by calling correspondent methods
3. Input: 
   - Flower name:	A string
     - The input is realized via `set_name()` method
     - If the input is not a string, the program will prompt' This is not a valid name.'
   - Number of petals:	A positive integer
     - The input is realized via `set_num_of_petals()` method
     - If the input is not a positive integer, the program will prompt' This is not a valid petal number.'
   - Price:	A positive float
     - The input is realized via `set_price()` method
     - If the input is not a positive float, the program will prompt' This is not a valid price.'
4. Execute as following:

![image-20210420220643161](C:\Users\ObserveX\AppData\Roaming\Typora\typora-user-images\image-20210420220643161.png)

## Question 2

1. Code saved in [q3-2.py](q3-2.py)
2. The program acquires the first derivative of a single-variable polynomial in its standard form
3. Input: A single-variable polynomial in its standard form(as a string)
4. Execute as followings:

![image-20210420221646755](C:\Users\ObserveX\AppData\Roaming\Typora\typora-user-images\image-20210420221646755.png)

## Question 3

1. Code saved in [q3-3.py](q3-3.py)
2. The program simulates an ecosystem consisting of two creatures: fish and bear. Each animal has a tendency to move or stay. Bear eats fish if they are in the same location. Two creatures colliding will produce a new animal of its kind. The program quits if the ecosystem is full.
3. Inputs:
   - The length of river:	Integer
   - The number of bears:    Integer
   - The number of fish:    Integer
   - Steps to simulate:    Integer
     - If any datatype is wrong, the program will print 'Check your input'
     - If the number of animals is larger than the length of river, the program will print 'Animal number exceeds length of river!'
4. Special cases:
   1. During a step of simulation, the new animals are recorded in a list. After a simulation, the new animals are placed into the river in succession.
   2. If there is no space to place new animal, the program will quit, printing the final status of river.
   3. If there is only one animal in the river, the program will also quit, printing the final status of river. 
5. Execute as following:

![image-20210423125055345](C:\Users\ObserveX\AppData\Roaming\Typora\typora-user-images\image-20210423125055345.png)
