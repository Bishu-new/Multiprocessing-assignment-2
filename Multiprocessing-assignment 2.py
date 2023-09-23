#!/usr/bin/env python
# coding: utf-8

# Ans 1 :  **Multiprocessing** in Python is a package that supports spawning processes using an API similar to the threading module. It refers to the ability of a system to support more than one processor at the same time. Applications in a multiprocessing system are broken into smaller routines that run independently. The operating system allocates these threads to the processors, improving the performance of the system.
# 
# Here's why multiprocessing is useful:
# 
# 1. **Better Usage of CPU**: When dealing with high CPU-intensive tasks, multiprocessing allows for better usage of the CPU.
# 2. **More Control Over Child Processes**: Compared with threads, multiprocessing provides more control over child processes.
# 3. **Avoids Global Interpreter Lock (GIL) Limitations**: For CPython, multiprocessing allows you to sidestep limitations imposed by the Global Interpreter Lock (GIL), which restricts execution to one thread at a time.
# 4. **Takes Advantage of Multiple CPUs & Cores**: Multiprocessing enables you to leverage multiple CPUs and cores, which can lead to significant performance improvements for certain types of programs.
# 5. **Ease of Coding**: The multiprocessing module in Python includes a simple and intuitive API for dividing work between multiple processes, making it easier to code concurrent applications.
# 

# Ans 2 : The difference between Multiprocessing and multithreading:
#     Basic Concept: Multiprocessing involves multiple processors or CPUs, each with its own set of registers, cache, and control units. This allows for true parallel execution of different processes1. On the other hand, multithreading occurs within a single process and shares the same set of resources, including memory and CPU.
# 
# Computing Power: In multiprocessing, CPUs are added to increase computing power. In contrast, multithreading creates multiple threads of a single process to increase computing power.
# 
# Execution: In multiprocessing, many processes are executed simultaneously. While in multithreading, many threads of a process are executed simultaneously.
# 
# Process Creation: In multiprocessing, process creation is a time-consuming process. While in multithreading, process creation is economical in terms of time and resources.
# 
# Memory Space: In multiprocessing, every process owns a separate address space. While in multithreading, a common address space is shared by all the threads.
# 
# Classification: Multiprocessing can be classified into symmetric and asymmetric. Multithreading is not classified into any categories.

# Ans 3 :  here's a Python program that uses the multiprocessing module to create a process:
# 

# In[2]:


import multiprocessing

def worker():
    """worker function"""
    print('Worker')

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()


# In[3]:


jobs


# Ans 4 : The multiprocessing Pool class in Python is a means of parallelizing the execution of a function across multiple input values, distributing the input data across processes. It provides a convenient way to create and manage a pool of worker processes.
# 
# Here's why it is used:
# 
# 1. **Ease of Use**: The Pool class is easier to use than the Process class because you do not have to manage the processes by yourself. It creates the processes, splits the input data, and returns the result in a list.
# 
# 2. **Efficient Memory Use**: While the Process keeps all the processes in memory, the Pool keeps only those that are under execution⁵.
# 
# 3. **Automatic Management**: It also waits for the workers to finish their tasks, i.e., you do not have to call the join() method explicitly.
# 
# 4. **Better Resource Utilization**: The multiprocessing package allows the programmer to fully leverage multiple processors on a given machine. It effectively side-steps the Global Interpreter Lock by using subprocesses instead of threads, which makes it particularly useful for tasks that are CPU intensive and can be broken down into smaller, independent tasks.
# 
# 5. **Convenient Parallelization**: The pool.map() function allows you to parallelize the execution of a function across multiple input values. It takes care of dividing the data into chunks and scheduling the execution of these chunks on available processors.
# 

# Ans 5 :  here's how we can create a pool of worker processes in Python using the multiprocessing module:
# 
# In this code, we first import the `Pool` class from the `multiprocessing` module. We then define a function `f` that takes an argument `x` and returns the square of `x`.
# 
# In the main part of the code, we create a pool of 5 worker processes using `with Pool(5) as p:`. The `with` statement is used for cleanup tasks and ensures that processes are cleaned up promptly when we're done with the pool.
# 
# We then use the `map` method of the pool to apply function `f` to multiple arguments `[1, 2, 3]`. The `map` method distributes the input arguments across processes and collects the results. The results are returned in a list that preserves the order of the input arguments.
# 
# This program will output `[1, 4, 9]`, which are the squares of 1, 2, and 3 respectively.

# In[ ]:


from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))


# Ans 6 : Write a python program to create 4 processes, each process should print a different number using the
# multiprocessing module in python.

# In[1]:


from multiprocessing import Process

def print_number(number):
    print(number)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    processes = []

    # create processes
    for number in numbers:
        process = Process(target=print_number, args=(number,))
        processes.append(process)

    # start processes
    for process in processes:
        process.start()

    # ensure all processes have finished execution
    for process in processes:
        process.join()

    print("All processes finished execution!")


# In[2]:


processes.append


# In[3]:


processes


# In[ ]:





# In[ ]:




