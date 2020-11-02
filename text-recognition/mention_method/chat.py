import csv




# Get key-word
# Pre : chat_data(type : list in list), min, max should be initialized
#  - chat_data : database in .csv file

def extract_most_word_in_chat(chat_data, min, max):
    print('----exract_most_word_in_chat----')
    chat_list = []
    resulting_list = []
    counting_list = []
    completed_list = []

    # slice chat by ' ' into words
    for row_in_csv in chat_data:
        seperated_chat = row_in_csv.split(' ')
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
        print(resulting_list[counting_list.index(copied_counting_list[top10_index])])
        completed_list.append(resulting_list[counting_list.index(copied_counting_list[top10_index])])

    return completed_list

# 10 times on 5sec -> highlight
def find_highlight_clip(word, chat_db, times_list):
    print('----fin_highlight_clip : ', word, '----')
    result = []
    count = 0
    for chat in chat_db:
        if chat.find(word) != -1:
            chtidx = chat_db.index(chat)
            count = 0
            index_count = 0
            while (times_list[chtidx + count] - times_list[chtidx]) <= 5:
                if chat_db[chtidx + count].find(word) != -1:
                    index_count += 1

                if index_count > 9:
                    result.append(chtidx)
                    break

                if(chtidx + count) >= len(chat_db):
                    break
                count += 1

    print("chat ", word, " is finished!")
    return result

    print(time_list)
    return time_list

#666718347_comments.csv
def get_list(csv_filename):
    print('----main----')
    chat_file = open(csv_filename, encoding='utf-8')
    chat_data = csv.reader(chat_file)
    chat_lists = []
    chat_time = []
    resulting_list = []

    for chat in chat_data:
        chat_lists.append(chat[2])
        chat_time.append(float(chat[0]))

    result_list = extract_most_word_in_chat(chat_lists, 0, 20)

    for key_word in result_list:
        print(key_word, "for")
        print(find_highlight_clip(key_word, chat_lists, chat_time))
        resulting_list.append(find_highlight_clip(key_word, chat_lists, chat_time))

    print(resulting_list)
    print("---------------")
    chat_file.close()

get_list("666718347_comments.csv")