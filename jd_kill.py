# 导入要使用到的模块(工具)
import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import win32com.client
from selenium.webdriver.support.wait import WebDriverWait

import myPlatform

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# 秒杀时间 算盘--软件 browser=浏览器
times = '2023-09-04 10:08:00'
# 打开浏览器
browser = webdriver.Chrome()

parm = myPlatform.PlatformParamsFactory.create_params(myPlatform.PlatformName.HUAWEI)

# 进入京东网页
browser.get(parm.url)
time.sleep(3)
# 扫码登录


browser.find_element(By.LINK_TEXT, parm.login).click()
print(f"登录 ={parm.login}")

if parm.loginWay is not None:
    browser.find_element(By.LINK_TEXT, parm.loginWay).click()

wait = WebDriverWait(browser, 1)

target_string = parm.target

found = False

while not found:
    try:
        # 查找页面上的元素\
        print("开始查找字符串")
        element = browser.find_element(By.PARTIAL_LINK_TEXT, target_string)
        print("目标字符串已找到：", target_string)
        found = True
        break  # 找到目标字符串后跳出循环
    except:
        pass  # 如果找不到元素，继续循环
# 打开购物车页面
if parm.platform is myPlatform.PlatformName.JD:
    browser.get("https://cart.jd.com/cart_index")
    time.sleep(5)
'''
1、打开浏览器
2、登录京东账号
3、扫码登录
4、进入购物车
5、选中需要购买的商品
6、对比时间
7、到抢购时间 点击结算按钮
'''

# 全选购物车
# while True:
#     if browser.find_element_by_class_name("jdcheckbox"):
#         browser.find_element_by_class_name("jdcheckbox").click()
#         break

while True:
    # 获取电脑现在的时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # 对比时间，时间到的话就点击结算
    print(now)
    # 判断是不是到了秒杀时间?
    if now > times:
        # 点击结算按钮
        while True:
            try:
                print("正在寻找---立即下单---入口")
                if browser.find_element(By.LINK_TEXT, parm.order):
                    print("立即下单显示出来了 ")
                    order = wait.until(browser.find_element(By.LINK_TEXT, parm.order))
                    order.click()
                    browser.find_element(By.ID, parm.submit)
                    print(f"主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单")
                    # speaker.Speak(f"主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单")
                    break

                if browser.find_element(By.ID, "pro-operation"):
                    print("here")
                    browser.find_element(By.LINK_TEXT, parm.order).click()
                    print(f"主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单")
                    speaker.Speak(f"主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单")
                    pass
            except:
                print("没有找到下单入口，正在进行下一次查找")
                pass
        # 点击提交订单按钮
        while True:
            try:
                if browser.find_element(By.ID, parm.submit):
                    browser.find_element(By.ID, parm.submit).click()
                    print(f"抢购成功，请尽快付款")
                    break
                if browser.find_element(By.LINK_TEXT, "提交订单"):
                    browser.find_element(By.LINK_TEXT, "提交订单").click()
                    print(f"抢购成功，请尽快付款")
                    break
            except:
                print(f"主人,我已帮你抢到商品啦,您来支付吧")
                time.sleep(0.01)
