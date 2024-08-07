import requests                        # 用于获取网页内容的模块
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import io
import pygame

from music_player import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def getInfo(searchIn):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(r"E:\Users\Jeze.T\Documents\python\python_spider\python-\chromedriver.exe", options=options)
    # 要搜索的链接
    driver.get("https://music.163.com/#/search/m/?s=" + searchIn + "&type=1")

    find_div = driver.find_elements_by_tag_name("iframe")  # 因为直接获取不到iframe的内容，因此使用web_driver
    driver.switch_to.frame(find_div[0])  # 关键步骤，跳转到iframe里面，就可以获取HTML内容

    res = driver.find_elements_by_xpath("//div[contains(@class,'item f-cb h-flag')]")

    datalist = []

    for i in range(len(res)):
        data = []
        num = i
        data.append(num)
        song = res[i].find_element_by_xpath(".//div[@class='td w0']//div[@class='sn']//div[@class='text']//a//b").text
        data.append(song)
        artist = res[i].find_element_by_xpath(".//div[@class='td w1']//div[@class='text']//a").text
        data.append(artist)
        album = res[i].find_element_by_xpath(".//div[@class='td w2']//div[@class='text']//a").text
        data.append(album)
        id = res[i].find_element_by_xpath(".//div[@class='td w0']//div[@class='sn']//div[@class='text']//a").get_attribute('href').replace("https://music.163.com/song?id=", "")
        data.append(id)
        datalist.append(data)
    return datalist



def play_song(num, datalist):
    """
    datalist 是一个列表
    num 是一个str
    """
    pygame.mixer.init()   #初始化
    if isinstance(int(num), int):
        num = int(num)
        if num >= 0 and num <= len(datalist):
            song_id = datalist[num][4]
            song_link = "http://music.163.com/song/media/outer/url?id=" + song_id + ".mp3"  # 根据歌曲的 ID 号拼接出下载的链接。歌曲直链获取的方法参考文前的注释部分。
            print("请稍等...")
            headers = {
                "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Connection": "keep-alive",
                "Cookie": "BIDUPSID=3462ADA9DAD1297B8A802A091F3A1F8D; PSTM=1604243305; __yjs_duid=1_bfdc1ab59d6e702f682925e36cc331711619834907464; MAWEBCUID=web_tOeXvJOFvBhPSCMjgshotDYrrvLDyQzIDKDrUBappiXmaMLHMC; BAIDUID=0C57B51E04C945AEB6A3FC64443905E9:FG=1; BDSFRCVID_BFESS=NX0OJeC62rO8dvbHli0nesnLjeh8gWrTH6aohfLyJalmWqO7YODEEG0Phf8g0Ku-hD88ogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=JbAtoKD-JKvJfJjkM4rHqR_Lqxby26nwynR9aJ5nJDoK8Ing5451h-cQhxoe2f7B5C-O0M3-QpP-HJ7dbxvBy4_jhJJDW5bkB2n4Kl0MLnntbb0xyn_VMM3beMnMBMnrteOnan673fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-Xjj30jN3P; BAIDUID_BFESS=0C57B51E04C945AEB6A3FC64443905E9:FG=1; BD_UPN=12314753; baikeVisitId=1b4b0792-99b6-4e00-a829-3a3e32ac4c2c; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=1344_0_8_9_10_41_0_2_8_7_4_0_1557297_0_0_0_1644224812_0_1644980831%7C9%23517117_127_1639885104%7C9; H_PS_645EC=61628yiJhNsbuOC4w8F8sM2WXJUfqIFOSNfz1QZvkaRrdLrB2jynmCCk94A; BD_HOME=1; H_PS_PSSID=35105_31253_35766_35865_34584_35490_35872_35245_35796_35317_26350_35746; BA_HECTOR=85800184810084agql1h0pdv80q"
            }
            response = requests.get(song_link, headers=headers).content
            byte = io.BytesIO(response)
            pygame.mixer.music.load(byte)
            pygame.mixer.music.play()
            pygame.display.set_mode([50,50])   #pygame是做游戏的，要打开界面
            # 设置打开界面的关闭方法，没有的话打开的界面没法关闭。
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
            '''
            f = open(datalist[num][1] + ".mp3", 'wb')  # 以二进制的形式写入文件中
            f.write(response)
            f.close()
            print("下载完成.nr")
            '''
        else:
            print("你输入的数字不在歌曲列表范围，请重新输入")
    else:
            print("请输入正确的歌曲序号")


if __name__ == '__main__':
    searchIn = input("请输入你想要搜索的关键词：")
    #searchIn = "张钰琪"
    datalist = getInfo(searchIn)
    print("%3s %-35s %-20s %-20s " % ("序号", "  歌名", "歌手", "专辑"))
    for i in range(len(datalist)):
        data = datalist[i]
        print("%3s %-35s %-20s %-20s " % (data[0], data[1], data[2], data[3]))
    num = input("请输入你想要播放歌曲的序号/please input the num you want to listen：")
    play_song(num, datalist)