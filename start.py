from PyQt5 import QtCore, QtGui, QtWidgets
from style import Ui_MainWindow
from style_2 import Ui_Dialog
import sys
import os
import psutil
import asyncio
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time
from datetime import datetime
from threading import Timer
from threading import Thread
import typing
import re
import logging
import asyncio
import json

run = False
restart = False
prov = 0
sleep = True

class MyThread_1(Thread):
    """
    A threading example
    """
    
    def __init__(self, delay, peer_id, command):
        """Инициализация потока"""
        Thread.__init__(self)
        self.delay = delay
        self.peer_id = peer_id
        self.command = command
    
    def run(self):
        asyncio.run(friends_lp.add_friends_conversations(self.delay, self.peer_id, self.command))

class MyThread_2(Thread):
    """
    A threading example
    """
    
    def __init__(self, delay, peer_id, command):
        """Инициализация потока"""
        Thread.__init__(self)
        self.delay = delay
        self.peer_id = peer_id
        self.command = command
    
    def run(self):
        asyncio.run(online.online(self.delay, self.peer_id, self.command))

class MyThread_3(Thread):
    """
    A threading example
    """
    
    def __init__(self, delay, peer_id, command):
        """Инициализация потока"""
        Thread.__init__(self)
        self.delay = delay
        self.peer_id = peer_id
        self.command = command
    
    def run(self):
        asyncio.run(info_lp.read(self.delay, self.peer_id, self.command))
    
class MyThread_sleep(Thread):
    """
    A threading example
    """
    
    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)
    
    def run(self):
        while sleep == True:
            print("Ждём токен")
            time.sleep(5)
        
class MyThread(Thread):
    """
    A threading example
    """
    
    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)
    
    def run(self):
        global run

        app = QtWidgets.QApplication(sys.argv)

        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        Dialog = QtWidgets.QDialog()
        ui_2 = Ui_Dialog()
        ui_2.setupUi(Dialog)
        MainWindow.show()

        def start_token():
            global prov
            token = ui.lineEdit.text()
            print(token)

            if token == "Ваш токен" or token == "":
            	print("токен не перезаписан")
            else:
        	    data = {"token": token}
        	    with open("database_token.json", "w", encoding="utf-8") as file:
        	        file.write(json.dumps(data, ensure_ascii=False, indent=4))
        	    print("токен перезаписан")
        	    
            prov = 1


        def start_main():
            global run
            global prov
            global sleep
            MainWindow.close()
            run = True
            sleep = False
            Dialog.show()
            prov = 1

        def stop_main():
            global run
            global restart
            global sleep
            Dialog.close()
            run = False
            restart = True
            sleep = False
            MainWindow.show()

        def exit():
            global sleep
            sleep = False
            p = psutil.Process(os.getpid())
            for main in p.get_open_files() + p.connections():
                os.close(handler.fd)
            python = sys.executable
            os.execl(python, python, *sys.argv)

        ui.pushButton_2.clicked.connect(start_main)
        ui.pushButton.clicked.connect(start_token)
        ui_2.pushButton_2.clicked.connect(exit)
        ui_2.pushButton.clicked.connect(stop_main)

        #sys.exit(app.exec_())
        test = app.exec_()
        if test == 0:
            global sleep
            sleep = False
            p = psutil.Process(os.getpid())
            for main in p.get_open_files() + p.connections():
                os.close(handler.fd)
            python = sys.executable
            os.execl(python, python, *sys.argv)
        
my_thread = MyThread()
my_thread.start()
thread_sleep = MyThread_sleep()
thread_sleep.start()
while True:
    if prov == 1:
        with open("database_token.json", "r", encoding="utf-8") as file:
          data = json.loads(file.read())
        token = data['token']
        vk = vk_api.VkApi(app_id=6146827, token=token)
        longpoll = VkLongPoll(vk, wait=0)
        import messages
        import vk_info
        import ping_lp
        import info_lp
        import friends_lp
        import sms
        import bomb 
        import online
        import press_f_1
        import press_f_2
        import gb
        import xz
        import anim_templates
        import templates_lp
        import conv
        import random
        try:
            for event in longpoll.listen():
            # Если пришло новое сообщение
                 if event.type == VkEventType.MESSAGE_NEW:

                      if event.from_me:
                        command = event.text
                        delay = 0
                        peer_id = event.peer_id
                        if run == False:
                            print("лп не запущен")
                        else:
                            try:
                                asyncio.run(info_lp.info_msg(delay, peer_id, command))
                                asyncio.run(bomb.bomb(delay, peer_id, command))
                                my_thread_1 = MyThread_1(delay, peer_id, command)
                                my_thread_1.start()
                                my_thread_2 = MyThread_2(delay, peer_id, command)
                                my_thread_2.start()
                                my_thread_3 = MyThread_3(delay, peer_id, command)
                                my_thread_3.start()
                                asyncio.run(press_f_1.pressf(delay, peer_id, command))
                                asyncio.run(press_f_2.pressf(delay, peer_id, command))
                                asyncio.run(gb.gb(delay, peer_id, command))
                                asyncio.run(xz.xz(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim_info(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim1(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim2(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim3(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim4(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim5(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim6(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim7(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim8(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim9(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim10(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim11(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim12(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim13(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim14(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim15(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim16(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim17(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim18(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim19(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim20(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim21(delay, peer_id, command))
                                asyncio.run(templates_lp.create_templates(delay, peer_id, command))
                                asyncio.run(templates_lp.templates(delay, peer_id, command))
                                asyncio.run(templates_lp.one_templates(delay, peer_id, command))
                                asyncio.run(templates_lp.delete_templates(delay, peer_id, command))
                                asyncio.run(templates_lp.create_dtemplates(delay, peer_id, command))
                                asyncio.run(templates_lp.dtemplate(delay, peer_id, command))
                                asyncio.run(templates_lp.red_dtemplates(delay, peer_id, command))
                                asyncio.run(templates_lp.dele_dtemplates(delay, peer_id, command))
                                asyncio.run(templates_lp.dtemplates(delay, peer_id, command))
                                asyncio.run(templates_lp.dtemplates_temp(delay, peer_id, command))
                                asyncio.run(templates_lp.delete_dtemplates(delay, peer_id, command))
                                asyncio.run(ping_lp.ping_info(delay, peer_id, command))
                                asyncio.run(conv.fonts(delay, peer_id, command))
                                asyncio.run(conv.font(delay, peer_id, command))
                                asyncio.run(info_lp.info(delay, peer_id, command))
                                asyncio.run(info_lp.execute(delay, peer_id, command))
                                asyncio.run(conv.convert(delay, peer_id, command))
                                asyncio.run(info_lp.info_user(delay, peer_id, command))
                                asyncio.run(info_lp.bind(delay, peer_id, command))
                                asyncio.run(info_lp.idm(delay, peer_id, command))
                                asyncio.run(info_lp.chats(delay, peer_id, command))
                                asyncio.run(info_lp.chats_name(delay, peer_id, command))
                                asyncio.run(info_lp.chats_del(delay, peer_id, command))
                                asyncio.run(info_lp.read_on(delay, peer_id, command))
                                asyncio.run(info_lp.read_off(delay, peer_id, command))
                                asyncio.run(sms.dd_sms(delay, peer_id, command))
                                asyncio.run(sms.del_sms(delay, peer_id, command))
                                asyncio.run(sms.del_sms_from_user(delay, peer_id, command))
                                asyncio.run(sms.add_sms(delay, peer_id, command))
                                asyncio.run(sms.add_vsms(delay, peer_id, command))
                                asyncio.run(sms.add_spam(delay, peer_id, command))
                                asyncio.run(sms.ban_user(delay, peer_id, command))
                                asyncio.run(sms.add_user(delay, peer_id, command))
                                asyncio.run(friends_lp.add_friends(delay, peer_id, command))
                                asyncio.run(friends_lp.del_friends(delay, peer_id, command))
                                asyncio.run(online.offline(0, event.peer_id, command))
                                asyncio.run(online.online_on(0, event.peer_id, command))
                            except:
                                print("Произошла ошибка")
                                #time.sleep(4)
                                continue
        except:
           print("Скрипт перезапущен")
           pass 

if restart == True:
    restart = False
    pass

    

