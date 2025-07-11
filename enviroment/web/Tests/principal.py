from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
from selenium import webdriver
import os



def configurardatos():
    urldeweb = 'https://qa-practice.netlify.app/'
    opt = Options()
    opt.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--incognito")
    opt.add_argument("--disable-extensions")
    opt.add_argument('--ignore-certificate-errors')
    opt.add_argument('log-level=3')
    opt.add_argument('--disable-dev-shm-usage')
    # opt.add_argument('--remote-debugging-port=9222')
    #  opt.add_argument('--aggressive-cache-discard')
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])

    if os.path.exists('/usr/local/bin/chromedriver'):
        service = Service('/usr/local/bin/chromedriver')
        opt.add_argument('--headless')
        driver = webdriver.Chrome(service=service, options=opt)
    else:
        driver = webdriver.Chrome(options=opt)

    return urldeweb, driver
