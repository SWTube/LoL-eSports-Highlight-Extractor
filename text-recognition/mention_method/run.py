# coding: utf-8

import re
import csv
import requests

VIDEO_ID = 666718347
OFFSET = 10
CACHE = []

SKT_T1 = [
    {'player': 'Canna', 'name': '김창동', 'line': 'top'},
    {'player': 'Roach', 'name': '김강희', 'line': 'top'},
    {'player': 'Cuzz', 'name': '문우찬', 'line': 'jungle'},
    {'player': 'Ellim', 'name': '최엘림', 'line': 'jungle'},
    {'player': 'Faker', 'name': '이상혁', 'line': 'mid'},
    {'player': 'Clozer', 'name': '이주현', 'line': 'mid'},
    {'player': 'Teddy', 'name': '박진성', 'line': 'bot'},
    {'player': 'Gumayusi', 'name': '이민형', 'line': 'bot'},
    {'player': 'Effort', 'name': '이상호', 'line': 'support'},
    {'player': 'Kuri', 'name': '최원영', 'line': 'support'},
]

DWG = [
    {'player': 'Nuguri', 'name': '장하권', 'line': 'top'},
    {'player': 'Flame', 'name': '이호종', 'line': 'top'},
    {'player': 'Canyon', 'name': '김건부', 'line': 'jungle'},
    {'player': 'ShowMaker', 'name': '허수', 'line': 'mid'},
    {'player': 'Nuclear', 'name': '신정현', 'line': 'bot'},
    {'player': 'Ghost', 'name': '장용준', 'line': 'bot'},
    {'player': 'Hoit', 'name': '류호성', 'line': 'support'},
]

SKT_VARIATION = []
DWG_VARIATION = []


def load_data() -> list:
    with open('../{0}_comments.csv'.format(VIDEO_ID), newline='\n', encoding='utf-8') as csv_file:
        comments = [{'content_offset_seconds': float(row[0]),
                     'commenter': row[1],
                     'message': row[2]}
                    for row in csv.reader(csv_file)]
    return comments


def is_hangul(text: str) -> bool:
    hangul_count = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
    return hangul_count > 0


def english_to_korean(text: str) -> str:
    # https://github.com/muik/transliteration
    data = {'input': text}
    r = requests.post('https://transliterator.herokuapp.com/', data=data)
    result = r.json()
    if result.get('learned') is False:
        print("[ INFO ] {0} is an unlearned word.".format(text))
    return result.get('output')


def get_variation(text: str) -> list:
    # 신격화 단어
    deification = ['갓', '킹', '황']
    return [d + text[1:] for d in deification]


def set_SKT_mentions() -> list:
    SKT_VARIATION.extend(['t1', '티원',])

    for player in SKT_T1:
        for key, value in player.items():
            SKT_VARIATION.append(value)
            # 신격화 검사
            if not is_hangul(value):
                value = english_to_korean(value)
            if len(value) < 2:
                continue
            SKT_VARIATION.extend([text for text in get_variation(value)])


def main():
    set_SKT_mentions()

    comments = load_data()
    last_chat_time = comments[-1].get('content_offset_seconds')
    result = []
    for i in range(0, int(last_chat_time - OFFSET) + 1):
        mention_count = 0
        comments_in_offset = [comment for comment in comments
                              if i <= comment.get('content_offset_seconds') < i + OFFSET]

        position = int(100 * i / last_chat_time)
        print("[ INFO ] {0}% Done".format(position))

        messages = [comment.get('message') for comment in comments_in_offset]
        for message in messages:
            for variation in SKT_VARIATION:
                if variation in message:
                    mention_count += 1
        print(mention_count)
        result.append(mention_count)

    tmp_result = [r for r in result if r is not 0]
    print("[ INFO ] 평균 10초당 SKT T1 언급 수 : 약 {0}회"
          .format(sum(tmp_result) / len(tmp_result)))

    # TODO: result 기반으로 하이라이트 추출하는 알고리즘 짜기


if __name__ == '__main__':
    main()
