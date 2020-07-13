# coding: utf-8

import requests
import csv


def main():
    params = {'client_id': 'wekbkeyd24lx8f78y6ofhihjd525ft'}
    video = 666718347

    r = requests.get('https://api.twitch.tv/v5/videos/{0}'.format(video), params)
    metadata = r.json()

    params['cursor'] = ''

    csvfile = open('{0}_comments.csv'.format(video), 'w', newline='', encoding='utf-8')
    csvwriter = csv.writer(csvfile)

    while params['cursor'] is not None:
        r = requests.get('https://api.twitch.tv/v5/videos/{0}/comments'.format(video), params)
        r.raise_for_status()

        data = r.json()
        for comment in data['comments']:
            print(comment)
            row = (comment['content_offset_seconds'],
                   comment['commenter']['display_name'],
                   comment['message']['body'])
            csvwriter.writerow(row)

            print("[{0}] {1}\t: {2}".format(comment['content_offset_seconds'],
                                            comment['commenter']['display_name'],
                                            comment['message']['body']))

        params['cursor'] = data.get('_next')

        if data['comments']:
            pos = int(100 * data['comments'][-1]['content_offset_seconds'] / metadata['length'])
            print('[*] Downloading chat [{0}%]...'.format(pos))


if __name__ == '__main__':
    main()
