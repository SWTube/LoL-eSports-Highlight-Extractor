import pandas as pd
import os
import csv

chat_file = open('666718347_comments.csv','r', encoding= 'UTF-8')

df_lol_chat = csv.reader(chat_file)
df_time_column = []
df_chat_column = []

for line in df_lol_chat:
    df_time_column.append(line[0])
    df_chat_column.append(line[2])

del df_time_column[0]
del df_chat_column[0]

chat_file.close()


def extract_num_of_chats_in_5sec() -> float: # 5초안에 25개의 채팅이 입력되면 하이라이트로 처리
    num_start = 0
    num_end = 1
    highlight_time = []


    while True:
        try:
            if (float(df_time_column[num_end]) - float(df_time_column[num_start])) > 5:
                number_of_chat = (num_end - num_start)
                if number_of_chat > 25:
                    highlight_time.append(df_time_column[num_start])
                num_start += 1
                num_end = num_start + 1
                continue

            num_end += 1

        except:
            break

    highlight_time.reverse()
    highlight_start = highlight_time.pop()
    highlight_end = highlight_time.pop()
    num_of_highlight = 1


    while True:
        try:

            while (float(highlight_time[-1]) - float(highlight_end)) < 10:
                highlight_end = highlight_time.pop()
            print("{}번째 하이라이트 구간: {}~{}".format(num_of_highlight,highlight_start,highlight_end))
            highlight_start = highlight_time.pop()
            highlight_end = highlight_time.pop()
            num_of_highlight += 1

        except:
            break



def extract_time_of_50chat() -> float: #50개의 채팅이 10초안에 입력되면 하이라이트로 처리

    num_start = 0
    num_end = 50
    highlight_time = []

    while True:
        try:
            if (float(df_time_column[num_end]) - float(df_time_column[num_start])) < 10 :
                highlight_time.append(df_time_column[num_end])
            num_end += 1
            num_start += 1

        except:
            break


    highlight_time.reverse()
    highlight_start = highlight_time.pop()
    highlight_end = highlight_time.pop()
    num_of_highlight = 1
    while True:
        try:

            while (float(highlight_time[-1]) - float(highlight_end)) < 10:
                highlight_end = highlight_time.pop()
            print("{}번째 하이라이트 구간: {}~{}".format(num_of_highlight, highlight_start, highlight_end))
            highlight_start = highlight_time.pop()
            highlight_end = highlight_time.pop()
            num_of_highlight += 1
        except:
            break