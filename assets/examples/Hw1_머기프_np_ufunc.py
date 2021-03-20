import matplotlib.pyplot as plt
import numpy as np
import time

def calculate_coordinate(angles):
    angles = angles * np.pi/180
    t_1, p_1, t_2, p_2 = angles[:,0], angles[:,1], angles[:,2], angles[:,3]
    x = (np.sin(t_2)-np.sin(t_1) + (np.tan(p_1)*np.cos(t_1) -np.tan(p_2)*np.cos(t_2)))/(np.tan(p_1) - np.tan(p_2))
    y = np.tan(p_1)*x + np.sin(t_1) - np.tan(p_1)*np.cos(t_1)
    
    return np.array([x,y]).T

def to_degree(angle):
    deg = angle.astype(dtype = np.int)
    minute = angle - deg
    angle = deg + minute/0.6
    return angle

def inefficient_calculate_coordinate(angles):
    [num_i, num_j] = angles.shape
    x = np.zeros(num_i)
    y = np.zeros(num_i)
    for i in range(num_i):
        for j in range(num_j):
            angles[i,j] = angles[i,j] * np.pi/180

    for i in range(num_i):
        t_1, p_1, t_2, p_2 = angles[i,0], angles[i,1], angles[i,2], angles[i,3]
        x[i] = (np.sin(t_2)-np.sin(t_1) + (np.tan(p_1)*np.cos(t_1) -np.tan(p_2)*np.cos(t_2)))/(np.tan(p_1) - np.tan(p_2))
        y[i] = np.tan(p_1)*x[i] + np.sin(t_1) - np.tan(p_1)*np.cos(t_1)
    
    return np.array([x,y]).T

def inefficient_to_degree(angle):
    [num_i, num_j] = angle.shape
    
    for i in range(num_i):
        for j in range(num_j):
            deg = int(angle[i,j])
            minute = angle[i,j] - deg
            angle[i,j] = deg + minute/0.6
    return angle


if __name__ == '__main__':
    observations = np.array([[159.23, 135.12, 115.21, 182.08],
                             [5.47, 284.18, 323.26, 346.56],
                             [85.53, 3.04, 41.42, 49.42],
                             [196.50, 168.12, 153.42, 218.48],
                             [179.41, 131.48, 136.06, 184.42],
                             [180.0,118,136,168],
                             [210, 151, 167, 204],
                             [121, 66, 76, 123],
                             [178, 108, 135, 153],
                             ])
    
    start = time.perf_counter()
    brahe_processed = to_degree(observations)
    brahe_result = calculate_coordinate(brahe_processed)
    
    efficient_time = time.perf_counter() - start
    print('>>> Efficient Calculation : ', efficient_time)
    
    
    start = time.perf_counter()
    brahe_processed_ineffi = inefficient_to_degree(observations)
    brahe_result_ineffi = inefficient_calculate_coordinate(brahe_processed_ineffi)

    inefficient_time = time.perf_counter() - start
    print('>>> Inefficient Calculation : ',inefficient_time)
    print('>>> Ratio : ',inefficient_time/efficient_time)
    
    