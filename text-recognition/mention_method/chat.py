import csv

def extract_most_word_in_chat(chat_data, min, max):
    print('----exract_most_word_in_chat----')
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

    for top10_index in range(min, max):
#        print(resulting_list[counting_list.index(copied_counting_list[top10_index])])
        completed_list.append(resulting_list[counting_list.index(copied_counting_list[top10_index])])

    return completed_list

#    for chat_string in resulting_list:
 #       print(chat_string, ", ", counting_list[resulting_list.index(chat_string)])



#    for target_word in completed_list:
#        extract_time(target_word, completed_list)

# 키워드 5초 내 10번 이상 중복 시 하이라이트
def find_highlight_clip(word, chat_db):
    print('----fin_highlight_clip----', word)
    time_list = []
    for chat in chat_db:
        print(chat, ", ", word)
        if chat[2].find(word) != -1:
            while True:
                count = 0
                index_count = 0
                print("word is in chat, ", count)
                if chat_db[chat_db.index(chat) + 1][0] <= (chat[0] + 5):
                    if word in chat_db[chat_db.index(chat) + 1][2]:
                        index_count += 1
                if index_count > 9:
                    time_list.append(chat[0])
                    time_list.append(chat[0] + 20)
    return time_list

#666718347_comments.csv
def main():
    print('----main----')
    csv_filename = input()
    chat_file = open(csv_filename, encoding='utf-8')
    chat_data = csv.reader(chat_file)
    result_list = extract_most_word_in_chat(chat_data, 10, 20)

    print(result_list)

    chat_list = []

    for i in chat_data:
        print(i[2])
    print("chat_list: ", chat_list)

    resulting_list = []

    for key_word in result_list:
        print(find_highlight_clip(key_word, chat_data))

    print("---------------")

    # 채팅 전체를 대상으로 중복된 횟수가 많은 순서대로 나열
    for row_in_csv in chat_data:
        if (row_in_csv not in resulting_list):
            print("row_in_csv ", row_in_csv)
            resulting_list.append(row_in_csv)
            counting_list.append(1)
        else:
            counting_list[resulting_list.index(row_in_csv)] += 1

    for chat_string in resulting_list:
        print(chat_string, ", ", counting_list[resulting_list.index(chat_string)])
    """
    for list_index in counting_list:
        print(list_index)

    for list_index in resulting_list:
        print(list_index)
    """
    chat_file.close()


main()
    # 채팅의 길이로 판단?
