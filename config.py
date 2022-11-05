from json import dump,load
from os.path import exists
from base64 import b64encode,b64decode
CONFIG_FILE = "./config.json"


def judge_config_exist():
    if not exists(CONFIG_FILE):
        inp = input_config()
        with open(CONFIG_FILE, 'w+') as fj:
            dump(inp, fj, indent=4, ensure_ascii=False)
    return read_info()


def input_config():
    print("欢迎使用，第一次使用请输入账号密码")
    account = str(input("输入账号：")).encode('gbk')
    password = str(input("输入密码：")).encode('gbk')
    print("录入完毕，接下来请在有网络的情况更新驱动才能使用")
    # code = int(input("为防止密码泄露及防止误操作，请设置启动码："))
    Account = b64encode(account).decode()
    Password = b64encode(password).decode()
    WebDriver = 'MTE0NTE0MTkxOTgxMA=='
    config = {
        'Account': Account,
        'Password': Password,
        'WebDriver': WebDriver
        # 'code':code
    }
    return config


def read_info():
    with open(CONFIG_FILE, "r") as file:
        info = load(file)
        decode_info = {
            'Account': b64decode(info['Account']).decode(),
            'Password': b64decode(info['Password']).decode(),
            'WebDriver': b64decode(info['WebDriver']).decode()
        }
        # print(decode_info['Account'],decode_info['Password'])
        return decode_info


def write_info(web_driver):
    config = read_info()
    config['Account'] = b64encode(config['Account'].encode("UTF-8")).decode()
    config['Password'] = b64encode(config['Password'].encode("UTF-8")).decode()
    config['WebDriver'] = b64encode(web_driver.encode("UTF-8")).decode()
    with open(CONFIG_FILE, "w", encoding='UTF-8') as file:
        dump(config, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    url = r"C:\Users\hcd18\.wdm\drivers\edgedriver\win64\107.0.1418\msedgedriver.exe"
    enc1 = b64encode((url.encode("UTF-8")))
    dec1 = b64decode(enc1.decode())
    print(enc1)
    print(dec1)
    res = judge_config_exist()
    print(res)
    write_info(url)
    res = judge_config_exist()
    print(res)
    # read_info(CONFIG_FILE)

    # print(read_info(CONFIG_FILE)['Account'],read_info(CONFIG_FILE)['Password'])
