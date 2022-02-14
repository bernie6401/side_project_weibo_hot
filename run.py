import subprocess
import time


if __name__ == "__main__":
    while True:
        subprocess.call('python weibo_hot.py')
        time.sleep(10)