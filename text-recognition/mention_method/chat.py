import csv

def extract_most_word_in_chat(chat_data):
    chat_list = []

    resulting_list = []
    #resulting_list_by_whole_chat = []

    counting_list = []
    copied_counting_list = []

    completed_list = []

    # 채팅을 ' '로(단어로) 슬라이싱 후 중복된 횟수가 많은 순서대로 나열
    for row_in_csv in chat_data:
        seperated_chat = row_in_csv[2].split(' ')

        for seperated_chat_word in seperated_chat:
            chat_list.append(seperated_chat_word)

    for chat_word in chat_list:
        if (chat_word not in resulting_list):
            resulting_list.append(chat_word)
            counting_list.append(chat_list.count(chat_word))

    copied_counting_list = counting_list

    copied_counting_list.sort()
    copied_counting_list.reverse()

    for chat_string in resulting_list:
        print(chat_string + ", " + counting_list[resulting_list.index(chat_string)])

    for top10_index in range(10, 20):
        print(resulting_list[counting_list.index(copied_counting_list[top10_index])])
        completed_list.append(resulting_list[counting_list.index(copied_counting_list[top10_index])])

    for target_word in completed_list:
        extract_time(target_word, completed_list)


def find_highlight_clip(word, chat_db):
    highlight = []
    start_time = 0
    start_index = 0
    chat_stack = 0
    for chat_index in chat_db:
        if word in chat_index[2] :
            start_index = index(chat_index)
            start_time = chat_index[0]
            while chat_index[0 + chat_stack] != start_time + 5:
                if word in chat_db[start_index + chat_stack]:



def main():

    csv_filename = input(string)

    chat_file = open(csv_filename, encoding='utf-8')

    chat_data = csv.reader(chat_file)

    extract_most_word_in_chat(chat_data)




    # 리스트 초기화(다른 방식을 쓰기 위해)
    resulting_list.clear()
    counting_list.clear()
    chat_list.clear()
    copied_counting_list.clear()
    completed_list.clear()


    # 채팅 전체를 대상으로 중복된 횟수가 많은 순서대로 나열
    for row_in_csv in chat_data:
        if (row_in_csv not in resulting_list):
            resulting_list.append(row_in_csv)
            counting_list.append(1)
        else:
            counting_list[resulting_list.index(row_in_csv)] += 1

    for chat_string in resulting_list:
        print(chat_string + ", " + counting_list[resulting_list.index(chat_string)])



    """
    for list_index in counting_list:
        print(list_index)

    for list_index in resulting_list:
        print(list_index)
    """

    chat_file.close()

    # 채팅의 길이로 판단?
