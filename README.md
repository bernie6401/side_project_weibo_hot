# side_project_weibo_hot

## Side Project Background
* Inspired by Bilingual Podcast is the best podcast channel in Taiwan that introduces interesting news happening around the world. They said they had a problem that they can not get the hot news from Weibo immediately before Xi made it disappear. For instance, Shuai Peng(彭帥) and Zhang Gaoli(張高麗) event. So, I wrote a side project about an automatic web system that can refresh the web page and download it automatically and keep the data safe.


## Installation
```bash
pip install pyautogui
pip install selenium
```


## Some Set-Up
1.	Make sure your web driver is the latest version. You can download it here(https://chromedriver.chromium.org/)
2.	Make sure your desktop is the idle one in your home that you'll not use it for a while.
3.	Make sure your desktop language keyboard is for English.


## Something can solve in the future
* The content data you download may not be the same as the latest because I just verify the hot news title before downloading.(Solved, I refresh the news_list.txt every day and then the page with the same title will download again.)

* Maybe someone can write about the login part that not only needs account and password but the id verification. This is very hard to solve in this system.

* (Solved)Someone can use a more efficient searching Algorithm instead of linear searching and clean up the news list in the file to speed up the searching time. For instance, clean up all titles saved a week ago and always make the list lighter. I used the method that I mentioned above that cleans up the news_list.txt every day and that'll make the searching time more efficient.

* (Solved)When you refresh the page many times, the server will reject the request from your desktop. So I add a file named run.py to solve this problem that used subprocess function independently in a while loop. That can lead the web to close completely and reboot again and again.

* The web driver will shut down when the times up. But that will make the downloading file be aborted. So, maybe someone can add a function to detect whether the download process succeed or not.

* To be continued...