from time import sleep
from selenium import webdriver


#Logging In
browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys('ketocouncil')
password_input.send_keys('*****')

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(10)

save_info = browser.find_element_by_xpath("//button[@type='button']")
save_info.click()
sleep(3)
notifications_btn = browser.find_element_by_class_name("bIiDR")
notifications_btn.click()

sleep(10)

# Searching for Hashtag

search_bar = browser.find_element_by_class_name('XTCLo')
search_bar.send_keys('#keto')
sleep(3)
search_link = browser.find_element_by_class_name('yCE8d')
search_link.click()
sleep(7)


# Entering Gallery
top_post = browser.find_element_by_class_name('v1Nh3')
top_post.click()
sleep(6)

# Liking Post 

like_button = browser.find_element_by_class_name('wpO6b')
like_button.click()
sleep(4)

# Cycling to next post
right_pagination = browser.find_element_by_class_name('coreSpriteRightPaginationArrow')
right_pagination.click()
sleep(9)

#Adding Comment
comment_box = browser.find_element_by_class_name('Ypffh')
comment_box.click()
sleep(1)
comment_box_focus = browser.find_element_by_class_name('focus-visible')
comment_box_focus.send_keys('Yum!')
sleep(2)
comment_box_focus.submit()



Closing Browser
browser.close()