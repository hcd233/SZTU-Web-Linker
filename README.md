# SZTU-Web-Linker
## 基于python的深技大校园网连接脚本
### requirement:selenium webdriver-manager (pip装最新的就行)
```
pip install selenium
pip install webdriver-manager
```
### 可以编译成exe用 我是用pyinstaller打包成exe用的
```
pyinstaller -D main.py -i icon.jpg
# -D是连库打包，可以在没有安装selenium和wm的情况下用， -i 可选，选择图片作打包的exe的图标
```
### 第一次用需要输入账号密码，本地保存在config.py上面，用的是Edge浏览器，改改代码可以换，然后需要在有网络的情况下可以自动下driver，之后就不用了，比较懒狗，如果浏览器不更新之后都不用更新这个driver，如果更新了需要重新在有网的环境下下一下，连接校园网不需要有网（不然我写这个脚本干嘛orz）
#### 欢迎fork、star、pull request、谢谢啦~
