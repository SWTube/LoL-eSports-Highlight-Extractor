import csv


class extract_highlight:
    def __init__(self):
        self.filename = "666718347"

    # 5초안에 50개 이상의 채팅이 입력되면 하이라이트로 처리
    def extract_num_of_chats_in_5sec(self) -> list:
        # return : list(highlight time)
        self.chat_file = open('{}_comments.csv'.format(self.filename), 'r', encoding='UTF-8')
        # extract chating time from chat_file
        df_lol_chat = csv.reader(self.chat_file)
        df_time_column = []

        for line in df_lol_chat:
            df_time_column.append(line[0])

        del df_time_column[0]

        self.chat_file.close()

        num_start = 0
        num_end = 1

        highlight_time = []
        # If the number of chats exceeds 50 for 5 seconds, the time is saved

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

    # 100개의 채팅이 10초안에 입력되면 하이라이트로 처리
    def extract_time_of_100chat(self) -> list:
        # return: list(highlight time)
        self.chat_file = open('{}_comments.csv'.format(self.filename), 'r', encoding='UTF-8')
        # extract chating time from chat_file
        df_lol_chat = csv.reader(self.chat_file)
        df_time_column = []

        for line in df_lol_chat:
            df_time_column.append(line[0])

        del df_time_column[0]

        self.chat_file.close()

        num_start = 0
        num_end = 100
        highlight_time = []
        # if the time for 100chat is less than 10sec, the time is saved.
        while True:
            try:
                if (float(df_time_column[num_end]) - float(df_time_column[num_start])) < 10:
                    highlight_time.append(df_time_column[num_end])
                num_end += 1
                num_start += 1

            except:
                break

        return highlight_time

    # combine the result of two function.
    def add_highlight_time_list(self) -> list:
        # return : list(result of extract_num_of_chats_in_5sec + extract_time_of_100chat)
        time_based_highlight = self.extract_num_of_chats_in_5sec()
        num_of_chats_based_highlight = self.extract_time_of_100chat()
        total_highlight_time_list = time_based_highlight + num_of_chats_based_highlight

        return total_highlight_time_list

    def extract_highlight_section(self, frame_num):
        # input: frame_num
        # return: None
        # output : highlight section, expressed in feames or times.
        total_highlight_time_list = self.add_highlight_time_list()
        total_highlight_time_list.reverse()
        highlight_start = total_highlight_time_list.pop()
        highlight_end = total_highlight_time_list.pop()
        num_of_highlight = 1

        while True:
            try:
                while (float(total_highlight_time_list[-1]) - float(highlight_end)) < 10:
                    highlight_end = total_highlight_time_list.pop()
                if (float(highlight_end) - float(highlight_start)) > 5:
                    if frame_num == "30":

                        print("{}번째 하이라이트 구간: {}~{}".format(num_of_highlight, (float(highlight_start) - 3) // 1 * 30,
                                                            (float(highlight_end) - 3) // 1 * 30))

                    elif frame_num == "60":
                        print("{}번째 하이라이트 구간: {}~{}".format(num_of_highlight, (float(highlight_start) - 3) // 1 * 60,
                                                            (float(highlight_end) - 3) // 1 * 60))

                    elif frame_num == "sec":
                        print("{}번째 하이라이트 구간: {}~{}".format(num_of_highlight, int((float(highlight_start) - 3) // 1),
                                                            int((float(highlight_end) - 3) // 1)))
                    else:
                        print("Please enter 30 or 60 or sec")
                        break
                    num_of_highlight += 1
                highlight_start = total_highlight_time_list.pop()
                highlight_end = total_highlight_time_list.pop()

            except:
                break

