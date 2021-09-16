from selenium import webdriver



def webget(keyword):
    browser.get(url.format(keyword))
    return None

if __name__ == '__main__':
    options = webdriver.S
    options.add_argument('--headless')
    url = '''http://iwencai.com/unifiedwap/result?token=8f296e89eeeaecb88395eb3a3dabc295?w=%E6%B6%A8%E5%81%9C'''
    browser = webdriver.Safari(options=options)
    webget('')

