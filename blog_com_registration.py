#!/usr/bin/env python 
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: latin-1 -*-
# -*- coding: utf-42 -*-
# -*- coding: utf-8 -*-

import firebug_proxy
import time 
import blog_com_verification


def login_n_submission(driver,email,password,age,title,content,tag):
        driver.get("http://blog.com/wp-login.php")
        elem = driver.find_element_by_name("log")
        elem.clear()
        elem.send_keys(email)
        elem = driver.find_element_by_name("pwd")
        elem.send_keys(password)
        elem = driver.find_element_by_name("wp-submit")
        elem.click()
        time.sleep(7)
        elem = driver.find_element_by_name("post_title")
        elem.send_keys(title)
        elem = driver.find_element_by_name("content")
        elem.send_keys(content)
        elem = driver.find_element_by_name("tags_input")
        elem.send_keys(tag)
        elem = driver.find_element_by_name("publish")
        elem.click()
        time.sleep(3)   
        logout = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/p/a[2]")
        logout.click()


def registration(email,password,age,title,content,tag):
    link = "http://blog.com/wp-signup.php"
    html, driver = firebug_proxy.main(link)
    try:
        elem = driver.find_element_by_name("user_email")
        elem.send_keys(email) 
        elem = driver.find_element_by_name("password_1")
        elem.send_keys(password)
        elem = driver.find_element_by_name("password_2")
        elem.send_keys(password)
        elem = driver.find_element_by_name("adcopy_response")
        captcha = raw_input("enter adcopy_response: ")
        #elem.send_keys(age)
        elem.send_keys(captcha)
        driver.find_element_by_name("submit_btn").click()
        elem = driver.find_element_by_name("blog_title")
        elem.send_keys(title)
        driver.find_element_by_name("submit").click()
        element = driver.find_element_by_xpath("/html/body/div[4]/div/div/table/tbody/tr[7]/td[3]/a/span")
        elem = element
        elem.click() 
        blog_com_verification.open_connection(email,password)
        login_n_submission(driver,email,password,age,title,content,tag)  
        driver.close()   
    except: 
        login_n_submission(driver,email,password,age,title,content,tag)
        print driver.current_url
        driver.close()

    

if __name__=="__main__":
    email = "xxxxxx@hotmail.com"
    password="xxxxxxx"
    age="24"
    title="motivation3"
    content='''Achieving goals is not a matter of having "discipline". It’s a matter of motivating yourself, and keeping your focus on your goal. Follow these hacks, or any combination of them that works for you, and you should have the motivation and focus you need. ''' 
    content= unicode(content, errors='ignore')

    tag = "motivation"
    registration(email,password,age,title,content,tag)

