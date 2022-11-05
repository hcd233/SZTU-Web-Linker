# code UTF-8

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def make_strategy(web_driver):
    global web_drivers
    web_drivers = web_driver
    grobal_status = web_drivers.find_element(By.XPATH, '/html/body/div[3]/ol/li[1]').text
    online_num = int(grobal_status[-2])
    print(f"当前在线的设备一共有{online_num}台")
    if online_num <= 2:
        print("选取策略为：直接连接")
        return 'Direct'
    elif online_num == 3:
        print("选取策略为：踢最后一个")
        return 'Last'
    elif online_num > 3:
        print("选取策略为：全踢")
        return 'All'
    else:
        print("制定策略出错！")
        sleep(1000)
        return None


def unlink_network(strategy):
    if strategy == 'Direct':
        print("无需踢人~")
    elif strategy == 'Last':
        index = -1
        count = 0
        print("正在踢除最后一个用户")
        for i in range(1, 10):
            if web_drivers.find_element(By.XPATH, f'/html/body/div[3]/div/table/tbody/tr[{i + 1}]/td[4]').text == '在线':
                count += 1
                index = i
            if count == 3:
                # 第一个第二个用户的xpath
                # /html/body/div[3]/div/table/tbody/tr[2]/td[2]/button
                # /html/body/div[3]/div/table/tbody/tr[3]/td[2]/button
                # 确定按钮
                # /html/body/div[5]/div/div/div[3]/button[1]
                # /html/body/div[5]/div/div/div[3]/button[1]
                unlink_button = web_drivers.find_element(By.XPATH,
                                                        f'/html/body/div[3]/div/table/tbody/tr[{index+1}]/td[2]/button')
                web_drivers.execute_script("arguments[0].click()", unlink_button)
                sure = web_drivers.find_element(By.XPATH, '/html/body/div[5]/div/div/div[3]/button[1]')
                web_drivers.execute_script("arguments[0].click()", sure)
                print("操作完毕")
                # sleep(200)
                break
    elif strategy == "All":
        for i in range(5):
            print("正在下线全部用户")
            unlink_all = web_drivers.find_element(By.XPATH, '/html/body/div[3]/ol/li[3]/button[2]')
            web_drivers.execute_script("arguments[0].click()", unlink_all)
            sleep(0.25)
            sure = web_drivers.find_element(By.XPATH, '/html/body/div[5]/div/div/div[3]/button[1]')
            web_drivers.execute_script("arguments[0].click()", sure)
            sleep(0.25)
            print("操作完毕")


if __name__ == '__main__':
    web_link = r"C:\Users\hcd18\Desktop\深圳技术大学学生宿舍校园网 用户自助平台2.html"
    driver = webdriver.Edge()
    driver.get(web_link)
    print(make_strategy(driver))
    unlink_network(make_strategy(driver))
