"""
#  File Name: audio_processing.py
#       Team: audio_recognition
#   Programmer: J2onJaeHyeon
#   Start: 08/03/20
#   Last Update: August 22, 2020
#   Purpose: Import audio file (format: wave)
"""


from pydub import AudioSegment
import random

def divide_section(sound : AudioSegment) -> dict:
    """
    value 값이 중복되면 앞서 입력된 key가 사라지는 것을 방지하기 위해 1000 곱하고 세자리 수 난수를 더해줌
    어짜피 크기 줄 세우는 건 변하지 않으니
    """
    section_sec = 1000  # 1 section = 3 sec
    number_of_section = int(len(sound) / section_sec)
    amplitude_dict = {}
    for index in range(number_of_section) :
        section = sound[section_sec * index : section_sec * (index + 1)]
        high_amplitude = section.max
        high_amplitude = high_amplitude * 1000 + random.randrange(1,1000)
        amplitude_dict[index] = high_amplitude

        if ((index + 1) == number_of_section):
            high_amplitude = sound[section_sec * (index + 1):].max
            amplitude_dict[(index + 1)] = high_amplitude
        else :
            continue

    return amplitude_dict

def descending_amps(amp_dict : dict) -> list:
    amps_list = list(amp_dict.values())
    amps_list.sort(reverse = True)

def score_amps(amp_dict : dict) -> dict:
    amps_list = list(amp_dict.values())
    amps_list.sort(reverse=True)
    top_sound = amps_list[0]

    for index in range (len(amp_dict)) :
        amp_dict[index] = round((amp_dict[index] / top_sound) * 100, 4)

    """
    top_10pct = amps_list[int(len(amps_list) * (1 / 10))]
    top_20pct = amps_list[int(len(amps_list) * (2 / 10))]
    top_30pct = amps_list[int(len(amps_list) * (3 / 10))]
    top_50pct = amps_list[int(len(amps_list) * (5 / 10))]
    
    for index in range(len(amp_dict)) :
        key = index
        this_amp = amp_dict[key]
        if (this_amp >= top_10pct) :
            amp_dict[key] = 20
        elif (this_amp >= top_20pct and this_amp < top_10pct):
            amp_dict[key] = 15
        elif (this_amp >= top_30pct and this_amp < top_20pct) :
            amp_dict[key] = 10
        elif (this_amp >= top_50pct and this_amp < top_30pct) :
            amp_dict[key] = 5
        else :
            amp_dict[key] = 0
    """
    return amp_dict

def filter_amps(amp_dict : dict) -> dict :
    """
    앞서 스코어링한 딕셔너리 파일에서 필요한 부분 외에는 삭제하는 함수
    """
    for index in range(len(amp_dict)) :
        if (amp_dict[index] < 40) : # 임의의 값 설정
            del amp_dict[index]
        else :
            continue

    time_list = list(amp_dict.keys())

    # 5초 안에 연결되지 않은 하이라이트 시점이 있다면 연결함
    for k in range(10) :
        for index in range(1, len(amp_dict)):
            if ((time_list[index] - time_list[index - 1]) <= 5):
                for num in range(1, time_list[index] - time_list[index - 1]):
                    time_list.append(time_list[index - 1] + num)
    # 중복성 제거
    temp_list = []
    for time in time_list :
        if time not in temp_list :
            temp_list.append(time)
        else :
            continue
    time_list = temp_list

    time_list.sort()

    #테이블 형식으로 이어져 있는 시간들을 리스트로 묶어 리스트 in 리스트로 제작. 3개 이하의 리스트는 삭제할 것
    time_table = []
    temp_index = 0
    for index in range(len(time_list) - 1) :
        if ((time_list[index] + 1) != time_list[index + 1]) :
            small_list = time_list[temp_index : index + 1]
            time_table.append(small_list)
            temp_index = index + 1

    empty_list = []
    for index in range(len(time_table)) :
        if (len(time_table[index]) >= 3) :
            empty_list.append(time_table[index])
        else :
            continue
    time_table = empty_list
    print(time_table)
    return time_list



def print_dict(amp_dict: dict) -> None:
    print(amp_dict.items())


def print_list(amplitude_list : list) -> None:
    '''
    :param amplitude_list: just print list yeah
    :return: None
    '''
    print("len(list) : ", len(amplitude_list))
    num = 0
    for index in range(len(amplitude_list)):
        if(amplitude_list[index] > 50):
            num = num + 1
            print(amplitude_list[index])
    print("num : ", num)

"""
def divide_section(sound : AudioSegment) -> list:
    section_sec = 3000  # 1 section = 3 sec
    number_of_section = int(len(sound) / section_sec)
    amplitude_list = []
    for index in range(number_of_section) :
        section = sound[section_sec * index : section_sec * (index + 1)]
        high_amplitude = section.max
        amplitude_list.append(high_amplitude)

        if ((index + 1) == number_of_section):
            high_amplitude = sound[section_sec * (index + 1):].max
            amplitude_list.append(high_amplitude)
        else :
            continue

    return amplitude_list



def print_list(amplitude_list : list) -> None:
    '''
    :param amplitude_list: just print list yeah
    :return: None
    '''
    print("len(list) : ", len(amplitude_list))
    for index in range(len(amplitude_list)):
        print(amplitude_list[index])
"""
def main():
    sound = AudioSegment.from_file("T1 vs SANDBOX Game 2 - LCK 2020 Spring Split W4D3 - SK Telecom T1 vs SBG G2.wav", format="wave")
    amps_dict = divide_section(sound)
    amps_dict = score_amps(amps_dict)
    #amps_list = list(amps_dict.values())
    #amps_list.sort(reverse = True)
    time_list = filter_amps(amps_dict)
    #print_list(amps_list)
    print(len(amps_dict), amps_dict)
    print(len(time_list), time_list)

    return None

if __name__ == '__main__':
    main()

"""   
    peak_amplitude = sound.max
    print(peak_amplitude)

new_wave = sound[0:26709]
print(new_wave.max)
print(len(sound))
"""

