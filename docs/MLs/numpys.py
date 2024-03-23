py_list = [[1,2]
           ,[3,4]
           ,[5,6]]  # list
import numpy as np
np_array = np.array([[7, 8]
                    ,[9,10]
                    ,[11,12]])  # 행렬 = array

# axis 축이 중요
# 행을 읽을지 열로 읽을지에 대한 부분을 명확히 해야함

## 디버깅 콘솔
# 구분 위한 type 확인
type(py_list)
# <class 'list'>
type(np_array)
# <class 'numpy.ndarray'>

# # class 타입 따른 편리성
py_list.sum()
# # Traceback (most recent call last):
# #   File "<string>", line 1, in <module>
# # AttributeError: 'list' object has no attribute 'sum'
# # <module 'numpy' from 'c:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\numpy\\__init__.py'>
np_array.sum()
# 57

# 0은 series 단위, 1은 column단위로 이루어진다. 
np_array.sum(axis=0)    # row(세로) 단위 연산
# # array([27, 30])    # 27=7+9+11, 30=8+10+12
np.sum(np_array, axis=0)
# # array([27, 30])
np_array.sum(axis=1)    # column(가로) 단위 연산
# # array([15, 19, 23]) # 15=7+8, 19=9+10, 23=11+12
np.sum(np_array, axis=1)
# array([15, 19, 23])

np.array(py_list)
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
np_array_second = np.array(py_list)
type(np_array_second)
# <class 'numpy.ndarray'>
np.concatenate((np_array, np_array_second),axis=0)
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])

# 병합
np_array_second = np.array(py_list)
type(np_array_second)
# <class 'numpy.ndarray'>
np.concatenate((np_array, np_array_second), axis=0) # row 단위 병합
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])
np.concatenate((np_array, np_array_second), axis=1) # column 단위 병합
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])
pass