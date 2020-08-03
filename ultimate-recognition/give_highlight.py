import numpy as np
import find_region_of_interest
def give_frame_point(frame_point_list:list)->list:
    """첫번째 frame은 궁극기 표준을 저장함. -> 꺼져있는 것.
    어두울수록 가까운 곳에 점수를 준다.
    궁극기 쿨타임이 길수록 많이준다.
    return:
    standard_frame,    compare_frame2...
    [{left1:s_point    {left1:point-s_point #작을수록 궁쓴지 얼마 안 되었다는 것.
      left2:s_point     left2:point-s_point
      left3:s_point},   left3:point-s_point}]

    """
    standard = frame_point_list[0] #궁극기가 꺼져있을 때.
    for compare_frame in frame_point_list[1:]:
        return None

def give_darkness_piont(ultimate_frame_list:list)->list:
    """궁극기 frame의 darkness를 측정해서 점수로 바꿈
    각 frame의 어두운 정도를 dictionary 값에 반환함.
    (20,15)짜리 ndarray가 들어있는 dictionary list
    return:
    ex)
    index_frame1,   index_frame2...
    [{left1:point   {left1:point
      left2:point    left2:point
      left3:point},  left3:point}]
    """
    result_list=[]
    for each_frame in ultimate_frame_list:
        for k in range(1,6):
            print(k)
            each_frame['left{0}'.format(k)] = each_frame['left{0}'.format(k)].sum()
            each_frame['right{0}'.format(k)] = each_frame['right{0}'.format(k)].sum()
        result_list.append(each_frame)
    return result_list

def main():
    test = np.arange(300)
    test = test.reshape(20, 15)
    value = test
    tst = {num: value
           for num in ['left1', 'left2', 'left3', 'left4', 'left5', 'right1', 'right2', 'right3', 'right4', 'right5']}
    print(give_darkness_piont([tst]))

if __name__ == '__main__':
    main()