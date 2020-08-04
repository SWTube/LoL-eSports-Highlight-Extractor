import csv


def extract_num_of_chats_in_5sec(filename) -> list:  # 5초안에 25개의 채팅이 입력되면 하이라이트로 처리
    chat_file = open('{}_comments.csv'.format(filename), 'r', encoding='UTF-8')

    df_lol_chat = csv.reader(chat_file)
    df_time_column = []
    df_chat_column = []

    for line in df_lol_chat:
        df_time_column.append(line[0])
        df_chat_column.append(line[2])

    del df_time_column[0]
    del df_chat_column[0]

    chat_file.close()

    num_start = 0
    num_end = 1
    highlight_time = []

    while True:
        try:
            if (float(df_time_column[num_end]) - float(df_time_column[num_start])) > 5:
                number_of_chat = (num_end - num_start)
                if number_of_chat > 50:
                    highlight_time.append(df_time_column[num_start])
                num_start += 1
                num_end = num_start + 1
                continue

            num_end += 1

        except:
            break

    return highlight_time


def extract_time_of_100chat(filename) -> list:  # 50개의 채팅이 10초안에 입력되면 하이라이트로 처리

    chat_file = open('{}_comments.csv'.format(filename), 'r', encoding='UTF-8')

    df_lol_chat = csv.reader(chat_file)
    df_time_column = []
    df_chat_column = []

    for line in df_lol_chat:
        df_time_column.append(line[0])
        df_chat_column.append(line[2])

    del df_time_column[0]
    del df_chat_column[0]

    chat_file.close()

    num_start = 0
    num_end = 100
    highlight_time = []

    while True:
        try:
            if (float(df_time_column[num_end]) - float(df_time_column[num_start])) < 10:
                highlight_time.append(df_time_column[num_end])
            num_end += 1
            num_start += 1

        except:
            break

    return highlight_time


def add_highlight_time_list(filename) -> list:
    time_based_highlight = extract_num_of_chats_in_5sec("{}".format(filename))
    num_of_chats_based_highlight = extract_time_of_100chat("{}".format(filename))
    total_highlight_time_list = time_based_highlight + num_of_chats_based_highlight

    return total_highlight_time_list


def extract_highlight_section(highlight_list):
    highlight_list.reverse()
    highlight_start = highlight_list.pop()
    highlight_end = highlight_list.pop()
    num_of_highlight = 1

    while True:
        try:

            while (float(highlight_list[-1]) - float(highlight_end)) < 10:
                highlight_end = highlight_list.pop()
            if (float(highlight_end) - float(highlight_start)) > 5:
                print("{}번째 하이라이트 구간: {}~{}".format(num_of_highlight, highlight_start, highlight_end))
                num_of_highlight += 1
            highlight_start = highlight_list.pop()
            highlight_end = highlight_list.pop()

        except:
            break


def main(filename):
    highlight_list = add_highlight_time_list(filename)

    extract_highlight_section(highlight_list)

