# code UTF-8


from os.path import exists
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import judge_config_exist, write_info
from strategy import make_strategy, unlink_network

print("SZTU-Network-AutoLinker.")
print("Copyright 2021~2022 By Huang Chengdong.")

URL = r"http://47.98.217.39/lfradius/login.php?c=login&a=showlogin"
HOST = r"http://47.98.217.39/lfradius/home.php/user/online"
INFO = judge_config_exist()

WebDriver = INFO['WebDriver']
OPT = Options()
OPT.headless = False
OPT.add_experimental_option('excludeSwitches', ['enable-logging'])
while True:
    MODE = eval(
        input("请选择需要的服务:\n\t0.更新驱动(需要联网)\n\t1.自动连校园网(无需联网,如果闪退请先更新驱动)\n选择[0/1] "))
    if MODE == 0 or MODE == 1:
        break
    else:
        print("输入错误:请重输[0/1],如要退出可以直接关闭")

if MODE:
    Account = INFO['Account']
    Password = INFO['Password']
    if not exists(WebDriver):
        print("请先下载驱动，需要网络")
        quit(114514)
    # print(WebDriver)
    DRIVER = webdriver.Edge(service=EdgeService(WebDriver), options=OPT)
    DRIVER.get(URL)

    account_input = DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/form[2]/div[2]/div/div[1]/div/div/input')
    password_input = DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/form[2]/div[2]/div/div[2]/div/div/input')
    account_input.clear()
    password_input.clear()
    account_input.send_keys(Account)
    password_input.send_keys(Password)
    DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/form[2]/div[2]/div/div[3]/div/input').click()
    DRIVER.get(HOST)
    unlink_network(make_strategy(DRIVER))
    link_network = DRIVER.find_element(By.XPATH, '/html/body/div[2]/nav/div[2]/button[1]')
    DRIVER.execute_script("arguments[0].click()", link_network)
else:
    try:
        print("正在下载驱动...")
        WebDriver = EdgeChromiumDriverManager().install()
        print(f"驱动已下载至: {WebDriver}\n接下来为你打开浏览器测试是否成功")
        # print(INFO)
        write_info(WebDriver)
    except:
        input("驱动下载失败,请检查网络.按任意键退出")
        quit(1919)
    DRIVER = webdriver.Edge(service=EdgeService(WebDriver), options=OPT)
    DRIVER.get(URL)
    input("是否成功？成功了可以退出程序,下一次需要联网可以使用~\n不成功可以联系HCD.\n按任意键退出.")
    quit(810)
    DRIVER.minimize_window()
