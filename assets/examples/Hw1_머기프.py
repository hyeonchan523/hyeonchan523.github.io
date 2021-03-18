import matplotlib.pyplot as plt
import numpy as np

def calculate_coordinate(angles):
    angles = angles * np.pi/180
    t_1, p_1, t_2, p_2 = angles[:,0], angles[:,1], angles[:,2], angles[:,3]
    x = (np.sin(t_2)-np.sin(t_1) + (np.tan(p_1)*np.cos(t_1) -np.tan(p_2)*np.cos(t_2)))/(np.tan(p_1) - np.tan(p_2))
    y = np.tan(p_1)*x + np.sin(t_1) - np.tan(p_1)*np.cos(t_1)
    r = (x**2 + y**2)**0.5
    theta = np.arctan(y/x)
    
    return np.array([x,y,r,theta]).T

def to_degree(angle):
    deg = angle.astype(dtype = np.int)
    minute = angle - deg
    angle = deg + minute/0.6
    return angle

if __name__ == '__main__':
    brahe = np.array([[159.23, 135.12, 115.21, 182.08],
                     [5.47, 284.18, 323.26, 346.56],
                     [85.53, 3.04, 41.42, 49.42],
                     [196.50, 168.12, 153.42, 218.48],
                     [179.41, 131.48, 136.06, 184.42],
                     ])
    havard = np.array([[180,118,136,168],
                       [210, 151, 167, 204],
                       [121, 66, 76, 123],
                       [178, 108, 135, 153],
                       ])
    
    brahe_processed = to_degree(brahe)
    havard_processed = to_degree(havard)
    
    brahe_result = calculate_coordinate(brahe_processed)
    havard_result = calculate_coordinate(havard_processed)
    print('Brahe')
    print(brahe_result)
    print('Havard')
    print(havard_result)
    
    plt.figure()
    plt.plot(brahe_result[:,0], brahe_result[:,1],'.')
    plt.title('Brahe\'s')
    plt.savefig('Brahe\'s')
    
    plt.figure()
    plt.plot(havard_result[:,0], havard_result[:,1],'.')
    plt.title('Havard\'s')
    plt.savefig('Havard\'s')
    
    
    plt.figure()
    plt.plot(brahe_result[:,0], brahe_result[:,1],'.')
    plt.plot(havard_result[:,0], havard_result[:,1],'.')
    plt.legend(['Brahe', 'Havard'])
    plt.title('concat\'s')
    plt.savefig('concat\'s')
    
    
    