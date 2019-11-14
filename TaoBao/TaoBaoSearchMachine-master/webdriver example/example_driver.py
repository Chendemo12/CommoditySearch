from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://login.taobao.com/member/login.jhtml?spm=a21wu.241046-my.754894437.1.4519fd50dPXaMM&f=top&redirectURL=https%3A%2F%2Fworld.taobao.com%2F%3Fspm%3Da21bp.8077467.1417485807582.1.6449e6bcStIj9X")

username = driver.find_element_by_id("TPL_username_1")
password = driver.find_element_by_id("TPL_password_1")
username.send_keys("yenng3")
password.send_keys("12345678abc")
login = driver.find_element_by_id("J_SubmitStatic")
login.click()
'''
usrname = driver.find_element_by_id("TPL_username_1")
'''
