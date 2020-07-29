import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def convert_window_freestyle(name: str) -> None:
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    return None

def choose_frame(path:str,interval:int)->list:
    """
    동영상의 규격은 1초당 약 60frame, frame은 위와같은 정보
    궁극기를 존재하기 전의 앞부분 frame은 자름.


    arg:
        interval: in all frames, cut frame into this interval
    return:
        list: 각 프레임의 이미지가 binary로 들어가 있음. 첫번째 프레임. 그리고 interval frame.

    raises: accuracy function 호출함
    """
    cap = cv.VideoCapture(path)
    k = 0
    start_frame = 4*60*60 # after 4 minute frame in 60FPS
    number_of_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)
    result_list = []
    while True:
        cap.set(cv.CAP_PROP_POS_FRAMES, start_frame + k * interval)
        if start_frame + k * interval > number_of_frames:
            break
        k += 1
        ret, frame = cap.read()

        if not ret:
            print("error")
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        result_list.append(frame)
        convert_window_freestyle("frame")
        cv.imshow('frame', frame)
        key = cv.waitKey(0)
        if key == 27:
            break
    cap.release()
    cv.destroyAllWindows()
    return result_list

def choose_ultimate_skill_part(frame_list)->list:
    return None

def champion():
    """
    인게임 플레이어에서
    예외적인 친구는 점수가 없음,
    궁극기의 쿨타임이 일정 이상인 친구들에게 점수를 줌.
    {'aatrox': '120/100/80', 'ahri': '130/105/80', 'akali': '100/80/60', 'alistar': '120/100/80', 'amumu': '150/125/100', 'anivia': '6', 'annie': '120/100/80', 'aphelios': '120/110/100', 'ashe': '100/90/80', 'aurelionsol': '110/90/70', 'azir': '120/105/90', 'bard': '110/95/80', 'blitzcrank': '60/40/20', 'brand': '105/90/75', 'braum': '140/120/100', 'caitlyn': '90/75/60', 'camille': '140/115/90', 'cassiopeia': '120/100/80', 'chogath': '80', 'corki': '2', 'darius': '120/100/80', 'diana': '100/90/80', 'dr_mundo': '110/100/90', 'draven': '100/90/80', 'ekko': '110/80/50', 'elise': '4', 'evelynn': '140/110/80', 'ezreal': '120', 'fiddlesticks': '140/110/80', 'fiora': '110/90/70', 'fizz': '100/85/70', 'galio': '200/180/160', 'gangplank': '180/160/140', 'garen': '120/100/80', 'gnar': '90/60/30', 'gragas': '120/100/80', 'graves': '120/90/60', 'hecarim': '140/120/100', 'heimerdinger': '100/85/70', 'illaoi': '120/95/70', 'irelia': '140/120/100', 'ivern': '140/130/120', 'janna': '150/135/120', 'jarvan': '120/105/90', 'jax': '80', 'jayce': '6', 'jhin': '120/105/90', 'jinx': '90/75/60', 'kaisa': '110/90/70', 'kalista': '150/120/90', 'karma': '45/42/39/36', 'karthus': '200/180/160', 'kassadin': '5/3.5/2', 'katarina': '90/60/45', 'kayle': '160/120/80', 'kayn': '120/100/80', 'kennen': '120', 'khazix': '100/85/70', 'kindred': '180/150/120', 'kled': '160/140/120', 'kogmaw': '2/1.5/1', 'leblanc': '60/45/30', 'leesin': '110/85/60', 'leona': '90/75/60', 'lillia': '130/110/90', 'lissandra': '120/100/80', 'lucian': '110/100/90', 'lulu': '110/95/80', 'lux': '80/60/40', 'malphite': '130/105/80', 'malzahar': '140/110/80', 'maokai': '120/100/80', 'masteryi': '85', 'missfortune': '120/110/100', 'mordekaiser': '140/120/100', 'morgana': '120/110/100', 'nami': '120/110/100', 'nasus': '120', 'nautilus': '120/100/80', 'neeko': '90', 'nidalee': '3', 'nocturne': '150/125/100', 'nunu': '110 / 100 / 90', 'olaf': '100/90/80', 'orianna': '110/95/80', 'ornn': '140/120/100', 'pantheon': '180/165/150', 'poppy': '140/120/100', 'pyke': '120/100/80', 'qiyana': '120', 'quinn': '3', 'rakan': '130/110/90', 'rammus': '100/80/60', 'reksai': '100/90/80', 'renekton': '120', 'rengar': '110/90/70', 'riven': '120/90/60', 'rumble': '100/85/70', 'ryze': '210/180/150', 'sejuani': '120/100/80', 'senna': '160/140/120', 'sett': '120/100/80', 'shaco': '100/90/80', 'shen': '200/180/160', 'shyvana': '0', 'singed': '120/110/100', 'sion': '140/100/60', 'sivir': '120/100/80', 'skarner': '120/100/80', 'sona': '140/120/100', 'soraka': '160/145/130', 'swain': '120', 'sylas': '100/80/60', 'syndra': '120/100/80', 'tahmkench': '140/130/120', 'taliyah': '180/150/120', 'talon': '100/80/60', 'taric': '180/150/120', 'teemo': '0.25', 'thresh': '140/120/100', 'tristana': '120/110/100', 'trundle': '120/100/80', 'tryndamere': '110/100/90', 'twistedfate': '180/150/120', 'twitch': '90', 'udyr': '6', 'urgot': '100/85/70', 'varus': '130/100/70', 'vayne': '100/85/70', 'veigar': '120/100/80', 'velkoz': '120/100/80', 'vi': '120/100/80', 'viktor': '120/100/80', 'vladimir': '150/135/120', 'volibear': '160/140/120', 'warwick': '110/90/70', 'wukong': '120/105/90', 'xayah': '160/145/130', 'xerath': '130/115/100', 'xinzhao': '120/110/100', 'yasuo': '80/55/30', 'yorick': '160/130/100', 'yuumi': '130/110/90', 'zac': '130/115/100', 'zed': '120/90/60', 'ziggs': '120/95/70', 'zilean': '120/90/60', 'zoe': '11/8/5'}

    """
    return None

def cut_ultimate_skill_region(frame_list:list)->list:
    result_list = []
    for frame in frame_list:
        coordinate = {"left1": frame[155:175, 65:80],
                      "left2": frame[260:275, 65:80],
                      "left3": frame[365:375, 65:80],
                      "left4": frame[465:480, 65:80],
                      "left5": frame[570:585, 65:80],
                      "right1": frame[155:175, 1840:1855],
                      "right2": frame[260:275, 1840:1855],
                      "right3": frame[365:375, 1840:1855],
                      "right4": frame[465:480, 1840:1855],
                      "right5": frame[570:585, 1840:1855]}
        result_list.append(coordinate)
    return result_list

    return None

def accuracy(player:dict)->dict:
    """choose frame의 정확도를 계산함.
    interval을 늘리면 정확도는 떨어질 것임. 하지만 빨라질 것임.
    interval을 줄이면 정확도는 올라갈 것임. 하지만 느려질 것임.
    return하는 것은
    """
    {'aatrox': '120/100/80', 'ahri': '130/105/80', 'akali': '100/80/60', 'alistar': '120/100/80',
     'amumu': '150/125/100', 'anivia': '6', 'annie': '120/100/80', 'aphelios': '120/110/100', 'ashe': '100/90/80',
     'aurelionsol': '110/90/70'}
    cap = cv.VideoCapture(path)
    cap.get(cv.CAP_PROP_FRAME_COUNT)
    return None

#shape_list[n번째 frame][어디쪽 player]

all_list = choose_frame("raw3.mp4",1000) # 약 17초
shaped_list = cut_ultimate_skill_region(all_list)
print(shaped_list)
print(shaped_list[0]['right1'].shape)
