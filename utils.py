import numpy as np
from scipy.spatial.transform import Rotation as Rot
from sympy import symbols, cos, sin, pi, simplify, sqrt, atan2
from sympy.matrices import Matrix

def rotation_to_transformation_matrix(R):
    """
    It converts from 3x3 Rotation matrix to 4x4 Transformation matrix
    """
    R = Matrix(R)
    T = R.col_insert(3, Matrix([0., 0., 0.]))
    T = T.row_insert(3, Matrix([[0., 0., 0., 1.]]))
    return T

def Jcol(T):
    return [T(0,3), T(1,3), T(2,3), T(2,1), T(0,2), T[1,0]]

def Rz(q):
    R = Matrix([[cos(q), -sin(q), 0.],
                [sin(q), cos(q), 0.],
                [0., 0., 1.]])

    return rotation_to_transformation_matrix(R)

def Ry(q):
    R = Matrix([[cos(q), 0., sin(q)],
                [0., 1., 0.],
                [-sin(q), 0., cos(q)]])
    return rotation_to_transformation_matrix(R)

def Rx(q):
    R = Matrix([[1., 0., 0.],
                [0., cos(q), -sin(q)],
                [0., sin(q), cos(q)]
                ])
    return rotation_to_transformation_matrix(R)

def Rxd(q):
    R = Matrix([[0, 0, 0, 0],
                [0, -sin(q), -cos(q), 0],
                [0, cos(q), -sin(q), 0],
                [0, 0, 0, 0]])
    return R

def Ryd(q):
    R = Matrix([[-sin(q), 0, cos(q), 0],
                [0, 0, 0, 0],
                [-cos(q), 0, -sin(q), 0],
                [0, 0, 0, 0]])
    return R

def Rzd(q):
    R = Matrix([[-sin(q), -cos(q), 0, 0],
                [cos(q), -sin(q), 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]])
    return R

def Tx(d):

    T = Matrix([[1., 0., 0., d],
                [0., 1., 0., 0.],
                [0., 0., 1., 0.],
                [0., 0., 0., 1.]
                ])
    return T

def Ty(d):

    T = Matrix([[1., 0., 0., 0.],
                [0., 1., 0., d],
                [0., 0., 1., 0.],
                [0., 0., 0., 1.]
                ])
    return T

def Tz(d):

    T = Matrix([[1., 0., 0., 0.],
                [0., 1., 0., 0.],
                [0., 0., 1., d],
                [0., 0., 0., 1.]
                ])
    return T

def Txd(d):

    T = Matrix([[0., 0., 0., 1.],
                [0., 0., 0., 0.],
                [0., 0., 0., 0.],
                [0., 0., 0., 0.]
                ])
    return T

def Tyd(d):

    T = Matrix([[0., 0., 0., 0.],
                [0., 0., 0., 1.],
                [0., 0., 0., 0.],
                [0., 0., 0., 0.]
                ])
    return T

def Tzd(d):

    T = Matrix([[0., 0., 0., 0.],
                [0., 0., 0., 0.],
                [0., 0., 0., 1.],
                [0., 0., 0., 0.]
                ])
    return T

def KukaKR10R11000_2_configurations():
    q = [0,-pi/2,0,0,0,0]
    d = [400,0,0,515,0,90]
    a = [25,560,25,0,0,0]
    alpha = [-pi/2,0,-pi/2,pi/2,-pi/2,0]
    return q, d,a, alpha

if __name__ == "__main__":
    q = 1
    print(Rot.from_euler('x', q).as_matrix())

    print("=============")
    print(rotation_to_transformation_matrix(Rot.from_euler('x', q).as_matrix()))