from http.client import PAYMENT_REQUIRED
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #send keys on keyboard

'''hault the page until it find some label appear on the page'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''imitate the action that human execute on mouse and keyboard'''
from selenium.webdriver.common.action_chains import ActionChains

'''to do some keyboard instruction-'''
import pyautogui
import time

def linearsearch(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return False
    return True


def read_write_file(type, write_data = None):
    file_path = 'D:/NTUST/Side_Project/Bilingual_weibo/news_list.txt'
    # file_path = 'E:/家裡電腦資料/Bernie/Bilingual_weibo/news_list.txt'
    if type == 'r':
        f = open(file_path, 'r', encoding="utf-8") #u must add encoding parameter
        arr = []
        for line in f.readlines():
            arr.append(line)
        f.close()
        return arr
    elif type == 'a':
        f = open(file_path, 'a', encoding='UTF-8')
        f.write(write_data + '\n')
        f.close()

    


while True:
    '''initial the driver'''
    PATH = 'D:/NTUST/Side_Project/Bilingual_weibo/chromedriver.exe'
    # PATH = 'E:/家裡電腦資料/Bernie/Bilingual_weibo/chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get('https://weibo.com/hot/weibo/102803')
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "app")))
    except:
        driver.close()
        continue
    driver.maximize_window()


    '''access to the hot news page'''
    hot_new_tap = driver.find_element_by_class_name("NavItem_text_3Z0D7")
    hot_new_tap.click()
    print(hot_new_tap)
    hot_new_tap = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/div/div/div/a[4]/div/span")


    '''read file'''
    hot_tiltle_save = read_write_file('r')
    t = time.localtime()
    origin_current_time = time.strftime("%Y%m%d%H%M", t)
    current_time = time.strftime("%Y%m%d%H%M", t)
    len_page = 1


    '''infinity loop for the main goal'''
    while True:
        '''refresh the page'''
        hot_new_tap.click()
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "HotTopic_tit_eS4fv")))
        except:
            driver.close()
            break
        hot_titles = driver.find_elements_by_class_name("HotTopic_tit_eS4fv")

        save_or_not = True
        for i in range(1, 4):
            #use linear search to verify the page has saved or not
            save_or_not = linearsearch(hot_tiltle_save, len(hot_tiltle_save), hot_titles[i].text + '\n')


            if save_or_not == True:
                hot_tiltle_save.append(hot_titles[i].text + '\n')
                print(hot_titles[i].text)
                read_write_file('a', hot_titles[i].text)    #write to the news list
                search = driver.find_element_by_class_name("woo-input-main")
                search.send_keys(Keys.CONTROL + "a")
                search.send_keys(Keys.DELETE)
                search.send_keys(hot_titles[i].text)
                time.sleep(2)
                while len(driver.window_handles) == len_page:
                    search.send_keys(Keys.RETURN)   #to make sure the new page has redirected
                len_page = len(driver.window_handles)
                

                #change the sub page
                print(driver.current_window_handle)
                driver.switch_to.window(driver.window_handles[-1])
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-act")))
                except:
                    driver.refresh()
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-act")))
                search = driver.find_element_by_class_name("woo-input-main")
                search.send_keys(Keys.CONTROL + "a")
                search.send_keys(Keys.CONTROL + "c")
                print(driver.window_handles)


                '''download the file and rename it'''
                pyautogui.hotkey('ctrl','s')
                time.sleep(3)

                t = time.localtime()
                if time.strftime("%Y%m%d%H%M", t) != current_time:
                    current_time = time.strftime("%Y%m%d%H%M", t)

                #rename part
                for k in range(4):
                    pyautogui.press('num' + current_time[k])
                pyautogui.press('_')
                for k in range(2):
                    pyautogui.press('num' + current_time[k + 4])
                pyautogui.press('_')
                for k in range(2):
                    pyautogui.press('num' + current_time[k + 6])
                pyautogui.press('_')
                pyautogui.hotkey('ctrl','v')
                for k in range(3):
                    pyautogui.press('tab')
                pyautogui.press('enter')
                time.sleep(3)


                #close the sub page
                driver.switch_to.window(driver.window_handles[0])
                
        
        time.sleep(10)

        t = time.localtime()
        current_time = time.strftime("%Y%m%d%H%M", t)
        #when the programm run through 3 mins or 1 hr then restart the driver
        if len(driver.window_handles) >= 11 or int(current_time) == int(origin_current_time) + 1 or int(current_time) % 100 == 0:
            driver.close()
            break