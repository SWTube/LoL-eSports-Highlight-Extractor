"""
#  File Name: audio_processing.py
#       Team: audio_recognition
#   Programmer: J2on
#   Start: 08/03/20
#   Last Update: September 4, 2022
#   Purpose: To derive the times with the highest volume for each section (format: wave)
"""


from pydub import AudioSegment

def divide_section(sound : AudioSegment) -> dict:
    """

        Divide section every second And measure highest amplitude of audio section

    """
    section_sec = 1000  # sound(AudioSegment) divided into 0.001 sec / 45min -> 272811 section
    number_of_section = int(len(sound) / section_sec) # reduced the number of sections / section : 272811 -> 2728

    amplitude_dict = {}
    for index in range(number_of_section) :
        section = sound[section_sec * (index) : section_sec * (index + 1)]
        high_amplitude = section.max
        high_amplitude = high_amplitude
        amplitude_dict[index] = high_amplitude

        if ((index + 1) == number_of_section):
            high_amplitude = sound[section_sec * (index + 1):].max
            amplitude_dict[(index + 1)] = high_amplitude
        else :
            continue

    return amplitude_dict

def score_amps(amp_dict : dict) -> dict:
    amps_list = list(amp_dict.values())
    amps_list.sort(reverse = True)
    top_sound = amps_list[0]

    for index in range (len(amp_dict)) :
        amp_dict[index] = round((amp_dict[index] / top_sound) * 100, 4)

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
    for index in range(1, len(amp_dict)):
        if ((time_list[index] - time_list[index - 1]) <= 5):
            for num in range(1, time_list[index] - time_list[index - 1]):
                time_list.append(time_list[index - 1] + num)
    time_list.sort()

    #테이블 형식으로 이어져 있는 시간들을 리스트로 묶어 리스트 in 리스트로 제작. 원소가 3개 미만의 리스트는 삭제
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

    return time_table
    # 이 과정 이후 time_table에는 list in list 방식으로 구간마다 list로 짜여짐

def expend_timelist(time_table : list) -> None : #전후과정을 알 수 있게 앞뒤 2초씩 추가
    for time_list in time_table :
        start_num = time_list[0]
        end_num = time_list[-1]
        if (start_num >= 2) :
            temp_list = [start_num - 2, start_num - 1, end_num + 1, end_num + 2]
            time_list.extend(temp_list)
            time_list.sort()

def main():
    sound = AudioSegment.from_file("T1 vs SANDBOX Game 2 - LCK 2020 Spring Split W4D3 - SK Telecom T1 vs SBG G2.wav", format = "wave")
    amps_dict = divide_section(sound)
    amps_dict = score_amps(amps_dict)
    time_table = filter_amps(amps_dict)
    expend_timelist(time_table)
    print(time_table)

    return None

if __name__ == '__main__':
    main()


