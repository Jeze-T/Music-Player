import requests
import re
from multiprocessing import Pool
import time
import traceback
import sys
import os
import eyed3


def download_mp3(audios, music_index, headers, already_downloads):
    try:
        date = audios[2]  # 文件前添加日期，便于排序
        music_name = date + '_' + audios[0] + '.mp3'
        music_url = audios[1]

        if music_name in already_downloads:  # 避免被重复下载
            print(f'{music_index}已存在，跳过下载')
            pass
        else:
            try:
                print(f'{music_index}下载中...')
                flag = 1  # 设置下载成功标志
                music_rt = requests.get(music_url, headers=headers)
                music_rt = music_rt.content  # 以bytes形式接收（接收后，以二进制写入文件即下载文件。也可以通过decode来转码变换为str），.text是以str形式接收
                with open(f'.//downloads//{music_name}', 'wb') as f:
                    f.write(music_rt)
            except:
                flag = 0
                print(f'{music_index}需要重新下载，或翻墙下载！')  # 偶尔会存在 需要重新下载或者翻墙下载的链接，跳过，存下url
                with open('download_error_urls.txt', 'a') as f:
                    write_str = music_name + ":" + music_url + '\n'
                    f.write(write_str)
                pass
            if flag:  # 如果下载成功，就修改音频标签
                audiofile = eyed3.load(f'.//downloads//{music_name}')  # 读取文件
                audiofile.initTag()  # 删除所有标签信息
                audiofile.tag.artist = u"JaysonTeng"  # 参与创作的艺术家
                audiofile.tag.album = u"NPR NEWS"  # 唱片集
                audiofile.tag.album_artist = u"NPR"  # 唱片艺术家
                audiofile.tag.title = u"%s" % (music_name)  # 标题
                audiofile.tag.track_num = 6  # 音轨编号，专辑内歌曲编号："#"
                audiofile.tag.save()  # 保存修改标签的文件

                print(f'{music_index}下载完成！')

    except:  # 捕获异常，写入文件
        error_info = sys.exc_info()
        with open('download_error.txt', 'a') as f:
            f.write(music_name + '，' + time.strftime("%Y-%m-%d %H:%M:%S") + '：\n')
            print(error_info[0], '：', error_info[1], '\n', file=f)
            traceback.print_tb(error_info[2], file=f)
            f.write('\n' + '=' * 50 + '\n')


if __name__ == '__main__':
    url = 'https://www.npr.org/proxy/listening/v2/recommendations?channel=cleplayer'  # 每日更新音频的链接（40个左右链接），早上和晚上八九点左右更新最多，其他时间会更新少量
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    rt = requests.get(url, headers=headers)
    rt = rt.text
    #audio_orurls = re.findall('title":"(.*?)","audioTitle.*?"date":"(.*?)T.*?audio\\\\\/mp3","href":"(.*?mp3)\?', rt,
    #                         re.S)  # 获取音频下载链接、标题、日期
    audio_orurls = re.findall('title":"(.*?)","date":"(.*?)T.*?audio\\\\\/mp3","href":"(.*?mp3)\?', rt,
                              re.S)  # 获取音频下载链接、标题、日期
    audio_urls = []
    for mus_ora in audio_orurls:
        title = mus_ora[0].replace('\/', ' ').encode('utf-8').decode('unicode_escape').replace('\\', '').replace(':',
                                                                                                                 '：').replace(
            '?', '？').replace('<', '《').replace('>', '》').replace('*', ' ').replace('\"', '\'').replace('|',
                                                                                                        ' ')  # 处理不规范的字符，windows文件名不支持部分特殊字符
        title = title[:-3] + title[-3:].replace(' ', '').replace('.', '')
        date = mus_ora[1].replace('-', '')
        url = mus_ora[2].replace('\\', '')
        audio_urls.append([title, url, date])
    already_downloads = os.listdir('.//downloads')

    pool = Pool(6)  # 采用多进程进行下载（注意windows系统 jupyter里面不能用多进程），若不想用多进程，可以直接调用download_mp3函数即可
    for music_index, audios in enumerate(audio_urls):
        pool.apply_async(download_mp3, (audios, music_index, headers, already_downloads))
        time.sleep(0.5)  # 各个进程之间有个时间差，避免一个ip同时访问多个连接失败
    pool.close()
    pool.join()