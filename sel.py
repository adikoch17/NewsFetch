import time
from selenium import webdriver

inpVal = input("what do you want to search?")
url = 'https://edition.cnn.com/search?size=10&q='+inpVal

fl = open("file.txt",'w')


driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
articles = driver.find_elements_by_class_name('cnn-search__result-contents')
for i in articles:
    fl.write(i.text + '\n\n')


