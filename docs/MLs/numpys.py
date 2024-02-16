py_list = [[1,2]
           ,[3,4]
           ,[5,6]]  # list
import numpy as np
np_array = np.array([[7, 8]
                    ,[9,10]
                    ,[11,12]])  # 행렬 = array
pass


# 타입 구분을 위한 확인
type(py_list)
# <class 'list'>
type(np_array)
# <class 'numpy.ndarray'>

# python의 list에는 별도의 계산 가능한 function이 없어서 
# 계산을 위한 수식을 별도로 꾸려줘야 하지만 
# numpy의 array는 기능을 품고 있다.
np_array.sum()
# 57.

# axis=0 은 array의 row끼리 작용한다.
np_array.sum(axis=0)
# array([27, 30])
# 위와 사용 방법만 조금 다른 같은 방식의 구문
np.sum(np_array,axis=0)
# array([27, 30])


# axis=0 은 array의 column끼리 작용한다.
np_array.sum(axis=1)
# array([15, 19, 23])
# 위와 사용 방법만 조금 다른 같은 방식의 구문
np.sum(np_array,axis=1)
# array([15, 19, 23])

np.array(py_list)               # py_list를 np의 array 클라스로 변경
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
np_array_second = np.array(py_list)         # np array second라는 변수에 담음.
type(np_array_second)           # np array second 타입 확인
# <class 'numpy.ndarray'>
np.concatenate((np_array,np_array_second),axis=0)       # np_array와 np_array_second를 row단위로 병합
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])
# 5:33
np.concatenate((np_array,np_array_second),axis=1)       # np_array와 np_array_second를 column단위로 병합
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])

# reshape() : 기존 배열을 재배열
# 1차원 배열 생성
arr = np.arange(10)
print("원본 1차원 배열:")
print(arr)
pass

## reshape : 내가 원하는 항목을 끌어모아줌
arr.reshape(5,2)
# array([[0, 1],
#        [2, 3],
#        [4, 5],
#        [6, 7],
#        [8, 9]])
arr
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# * 마이너스(-)가 붙으면 알아서 정렬해줌
arr.reshape(-1,2)
# array([[0, 1],
#        [2, 3],
#        [4, 5],
#        [6, 7],
#        [8, 9]])
arr.reshape(-1,1)
# array([[0],
#        [1],
#        [2],
#        [3],
#        [4],
#        [5],
#        [6],
#        [7],
#        [8],
#        [9]])