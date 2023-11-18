# def measure_time(func):
#     import time
    
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
#         return result
    
#     return wrapper
# @measure_time
# def factorial(n):
#     # x  = [i for i in range(n) if i % 2 == 0 ]
#     if n == 0:
#         return 1
#     else:
#         return n* factorial(n-1)
    
# print(factorial(10))



# def check_types(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if not isinstance(arg, (int, float)):
#                 raise TypeError("Аргумент должен быть числом")
#         return func(*args, **kwargs)
#     return wrapper

# @check_types
# def add_numbers(a, b):
#     return a + b
