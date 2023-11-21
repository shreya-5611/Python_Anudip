import numpy as np


my_list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]


for arr in my_list:
    mean_value = np.mean(arr)
    print(f"Mean of {arr}: {mean_value}")
    
'''   
output:
Mean of [3 2 8 9]: 5.5
Mean of [ 4 12 34 25 78]: 30.6
Mean of [23 12 67]: 34.0
'''
