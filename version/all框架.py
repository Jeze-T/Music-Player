import requests  # 用于获取网页内容的模块
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

import io
import pygame
import sys
from music_player import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QStringListModel, QTimer
from mutagen.mp3 import MP3


class musicFunc(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(musicFunc, self).__init__(parent)
        self.setupUi(self)
        self.B_search.clicked.connect(self.getSong)
        self.song_table.doubleClicked.connect(self.line)
        self.Bup.clicked.connect(self.click_up)
        self.Bdown.clicked.connect(self.click_down)
        self.Bpause.clicked.connect(self.pause)

        self.Bnetease.setCheckable(True)
        self.Bnetease.setEnabled(False)

        self.Bnetease.clicked.connect(self.netease)
        self.Bbaidu.clicked.connect(self.baidu)
        self.Bkuwo.clicked.connect(self.kuwo)
        self.Bnpr.clicked.connect(self.npr)

        self.label_song.setText('Welcome')
        self.label_artist.setText('')
        self.label_info.setText('')

        self.index = ''
        self.datalist = []
        self.pause_state = 1
        self.searchIn = ''
        self.time_length = float(0)
        self.source = 'netease'

        self.timer1 = QTimer()
        self.timer_switch_flag = False
        self.timer1.start(100)  # 每s启动一次
        self.timer1.timeout.connect(self.show_time)

    def getInfo(self):
        desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
        desired_capabilities["pageLoadStrategy"] = "none"#当html下载完成之后，不等待解析完成，selenium会直接返回，加快速度

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        driver = webdriver.Chrome(r"E:\Users\Jeze.T\Documents\python\python_spider\python-\chromedriver.exe",
                                  options=options)
        # 要搜索的链接
        driver.get("https://music.163.com/#/search/m/?s=" + self.searchIn + "&type=1")

        find_div = driver.find_elements_by_tag_name("iframe")  # 因为直接获取不到iframe的内容，因此使用web_driver
        driver.switch_to.frame(find_div[0])  # 关键步骤，跳转到iframe里面，就可以获取HTML内容

        res = driver.find_elements_by_xpath("//div[contains(@class,'item f-cb h-flag')]")

        for i in range(len(res)):
            data = []
            num = str(i)
            data.append(num)
            song = res[i].find_element_by_xpath(
                ".//div[@class='td w0']//div[@class='sn']//div[@class='text']//a//b").text
            data.append(song)
            artist = res[i].find_element_by_xpath(".//div[@class='td w1']//div[@class='text']//a").text
            data.append(artist)
            album = res[i].find_element_by_xpath(".//div[@class='td w2']//div[@class='text']//a").text
            data.append(album)
            id = res[i].find_element_by_xpath(
                ".//div[@class='td w0']//div[@class='sn']//div[@class='text']//a").get_attribute('href').replace(
                "https://music.163.com/song?id=", "")
            data.append(id)
            self.datalist.append(data)

    def line(self,index):
        self.index = index
        self.song = self.datalist[index.row()]
        self.info()

    def info(self):
        self.song_id = self.song[4]
        # self.source =
        self.song_name = self.song[1]
        self.song_artist = self.song[2]
        self.song_num = self.song[0]
        self.play()

    def play(self):
        headers = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Cookie": "BIDUPSID=3462ADA9DAD1297B8A802A091F3A1F8D; PSTM=1604243305; __yjs_duid=1_bfdc1ab59d6e702f682925e36cc331711619834907464; MAWEBCUID=web_tOeXvJOFvBhPSCMjgshotDYrrvLDyQzIDKDrUBappiXmaMLHMC; BAIDUID=0C57B51E04C945AEB6A3FC64443905E9:FG=1; BDSFRCVID_BFESS=NX0OJeC62rO8dvbHli0nesnLjeh8gWrTH6aohfLyJalmWqO7YODEEG0Phf8g0Ku-hD88ogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=JbAtoKD-JKvJfJjkM4rHqR_Lqxby26nwynR9aJ5nJDoK8Ing5451h-cQhxoe2f7B5C-O0M3-QpP-HJ7dbxvBy4_jhJJDW5bkB2n4Kl0MLnntbb0xyn_VMM3beMnMBMnrteOnan673fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-Xjj30jN3P; BAIDUID_BFESS=0C57B51E04C945AEB6A3FC64443905E9:FG=1; BD_UPN=12314753; baikeVisitId=1b4b0792-99b6-4e00-a829-3a3e32ac4c2c; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=1344_0_8_9_10_41_0_2_8_7_4_0_1557297_0_0_0_1644224812_0_1644980831%7C9%23517117_127_1639885104%7C9; H_PS_645EC=61628yiJhNsbuOC4w8F8sM2WXJUfqIFOSNfz1QZvkaRrdLrB2jynmCCk94A; BD_HOME=1; H_PS_PSSID=35105_31253_35766_35865_34584_35490_35872_35245_35796_35317_26350_35746; BA_HECTOR=85800184810084agql1h0pdv80q"
        }
        song_link = "http://music.163.com/song/media/outer/url?id=" + self.song_id + ".mp3"
        response = requests.get(song_link, headers=headers).content
        self.label_song.setText(self.song_name)
        self.label_artist.setText(self.song_artist)

        self.pause_state = 0
        self.Bpause.setText('⏸')

        pygame.mixer.init()  # 初始化
        byte = io.BytesIO(response)
        pygame.mixer.music.load(byte)
        self.time_length = MP3(byte).info.pprint().split(',')[-1].replace('seconds','').strip()
        pygame.mixer.music.play(1)

    def show_time(self):
        if self.time_length != float(0):
            all_m,all_s = divmod(float(self.time_length),60)
            all_time = str(int(all_m)) + ':' + str(int(all_s))
            get_time = pygame.mixer.music.get_pos() / 1000
            get_m, get_s = divmod(float(get_time), 60)
            now_time = str(int(get_m)) + ':' + str(int(get_s))
            self.label_info.setText(now_time + '/' + all_time)
            if not pygame.mixer.music.get_busy():
                self.Bpause.setText('▶')
                self.label_info.setText(all_time + '/' + all_time)

    def pause(self):
        if self.pause_state == 0:
            pygame.mixer.music.pause()
            self.Bpause.setText('▶')
            self.label_song.setText(self.song_name)
            self.label_artist.setText(self.song_artist)
            self.pause_state = 1
        else:
            pygame.mixer.music.unpause()
            self.Bpause.setText('⏸')
            self.label_song.setText(self.song_name)
            self.label_artist.setText(self.song_artist)
            self.pause_state = 0

    def click_up(self):
        self.song = self.datalist[int(self.song_num)+1]
        self.info()

    def click_down(self):
        self.song = self.datalist[int(self.song_num)-1]
        self.info()

    def source_init(self):
        self.Bnetease.setCheckable(False)
        self.Bbaidu.setCheckable(False)
        self.Bkuwo.setCheckable(False)
        self.Bnpr.setCheckable(False)
        self.Bnetease.setEnabled(True)
        self.Bbaidu.setEnabled(True)
        self.Bkuwo.setEnabled(True)
        self.Bnpr.setEnabled(True)

    def netease(self):
        self.source = 'netease'
        self.source_init()
        self.Bnetease.setCheckable(True)
        self.Bnetease.setEnabled(False)

    def baidu(self):
        self.source = 'baidu'
        self.source_init()
        self.Bbaidu.setCheckable(True)
        self.Bbaidu.setEnabled(False)

    def kuwo(self):
        self.source = 'kuwo'
        self.source_init()
        self.Bkuwo.setCheckable(True)
        self.Bkuwo.setEnabled(False)

    def npr(self):
        self.source = 'npr'
        self.source_init()
        self.Bnpr.setCheckable(True)
        self.Bnpr.setEnabled(False)


    def getSong(self):
        self.searchIn = self.Edit_input.text()
        self.datalist = []
        self.songlist = []
        self.getInfo()
        for da in self.datalist:
            self.songname = da[1]
            self.singer = da[2]
            self.albumname = da[3]
            self.songlist.append(self.songname+';'+self.singer+';'+self.albumname)
        list_model = QStringListModel()
        list_model.setStringList(self.songlist)
        self.song_table.setModel(list_model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    music = musicFunc()
    music.show()
    sys.exit(app.exec_())