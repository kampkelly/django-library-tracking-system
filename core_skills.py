import random
rand_list = [random.randint(1, 20) for _ in range(10)]
# Create a list of 10 random numbers between 1 and 20.

list_comprehension_below_10 = [num for num in rand_list if num >= 10]
# Filter Numbers Below 10 (List Comprehension)

list_comprehension_below_10 = list(filter(lambda x: x >= 10, rand_list))
# Filter Numbers Below 10 (Using filter)
