# coding=utf-8
from selenium import webdriver
def browser():
    dr=webdriver.Chrome()
    # dr=webdriver.Firefox()
    # dr=webdriver.Ie()
    # dr.get("http://assptest.oppein.com")
    return dr
#调试运行
if __name__=='__main__':
    browser()