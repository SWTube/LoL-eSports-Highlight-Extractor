# coding: utf-8

import csv


class Game:
    def __init__(self):
        self.comments = []
        self.video_id = 666718347
        self.offset = 10

        self.blue_team = {
            'name': 'T1',
            'team_kor': '티원',
            'players': [
                {'player': 'Canna', 'player_kor': '칸나', 'name': '김창동', 'line': '탑'},
                {'player': 'Roach', 'player_kor': '로치', 'name': '김강희', 'line': '탑'},
                {'player': 'Cuzz', 'player_kor': '커즈', 'name': '문우찬', 'line': '정글'},
                {'player': 'Ellim', 'player_kor': '엘림', 'name': '최엘림', 'line': '정글'},
                {'player': 'Faker', 'player_kor': '페이커', 'name': '이상혁', 'line': '미드'},
                {'player': 'Clozer', 'player_kor': '클로저', 'name': '이주현', 'line': '미드'},
                {'player': 'Teddy', 'player_kor': '테디', 'name': '박진성', 'line': '바텀'},
                {'player': 'Gumayusi', 'player_kor': '구마유시', 'name': '이민형', 'line': '바텀'},  # 봇, 바텀
                {'player': 'Effort', 'player_kor': '에포트', 'name': '이상호', 'line': '서포트'},
                {'player': 'Kuri', 'player_kor': '구리', 'name': '최원영', 'line': '서포트'},   # 서폿, 서포트
            ],
        }
        self.blue_team_variation = []

        self.blue_team_mention_count = []
        print(self.load_cache())
        if self.load_cache() is False:
            self.load_data()
            self.set_variation()
            self.get_mention_counts()

    def load_data(self) -> list:
        with open('../{0}_comments.csv'.format(self.video_id), newline='\n', encoding='utf-8') as csv_file:
            self.comments = [{'content_offset_seconds': float(row[0]),
                         'commenter': row[1],
                         'message': row[2]}
                        for row in csv.reader(csv_file)]
        return self.comments

    def load_cache(self):
        try:
            with open('result.txt', 'r') as f:
                cache = list(map(int, f.read().split(',')))
                if len(cache) < 10:
                    return False
                self.blue_team_mention_count = cache
                return True

        except Exception as e:
            print(f'[ ERROR ] {e}')
            return False

    def get_variation(self, text: str) -> list:
        # 신격화 단어
        deification = ['갓', '킹', '황']
        return [text] + [d + text[1:] for d in deification]

    def set_variation(self):
        self.set_blue_team_variation()

    def set_blue_team_variation(self):
        for player in self.blue_team['players']:
            self.blue_team_variation.extend(self.get_variation(player['name']))
            self.blue_team_variation.extend(self.get_variation(player['player_kor']))

    def get_mention_counts(self):
        last_chat_time = self.comments[-1].get('content_offset_seconds')
        result = []
        for i in range(0, int(last_chat_time - self.offset) + 1):
            mention_count = 0
            comments_in_offset = [comment for comment in self.comments
                                  if i <= comment.get('content_offset_seconds') < i + self.offset]

            position = int(100 * i / last_chat_time)
            if position % 5 == 0:
                print("[ INFO ] {0}% Done".format(position))

            messages = [comment.get('message') for comment in comments_in_offset]
            for message in messages:
                for variation in self.blue_team_variation:
                    if variation in message:
                        mention_count += 1
            # print(mention_count)
            self.blue_team_mention_count.append(mention_count)

        with open('result.txt', 'w') as f:
            f.write(','.join(map(str, self.blue_team_mention_count)))

    def get_highlights(self) -> list:
        offset = 1
        highlights = []
        last_sec = 0

        for sec in range(0, len(self.blue_team_mention_count)):
            if sec < last_sec:
                continue

            inclines = []
            t = 0
            while True:
                t += 1
                try:
                    incline = (self.blue_team_mention_count[sec + t + offset] - self.blue_team_mention_count[sec + t]) / offset

                    if t == 1:
                        inclines.append(incline)
                        continue

                    if incline < 0:
                        break

                    if incline < inclines[-1] and t > 30:
                        highlights.append((sec, sec + t + offset))
                        last_sec = sec + t
                        break

                    elif incline < inclines[-1]:
                        break

                    inclines.append(incline)

                except IndexError:
                    break

        return highlights

