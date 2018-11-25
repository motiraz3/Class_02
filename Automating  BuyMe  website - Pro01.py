# A - Registration screen
import time
#from selenium.webdriver.support.ui import Select
from selenium import webdriver
driver = webdriver.Chrome(executable_path ="C:\\Users\Moti\Downloads\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(15)
driver.get("https://buyme.co.il/")
#####Enter The website#####
driver.find_element_by_xpath('.//*[@id="ember577"]/div/ul[1]/li[3]/a/span[1]').click()
#####"Press on button " כניסה  |הרשמה"#####
# driver.find_element_by_xpath('//*[@id="ember558"]/div/div[1]/div/div/div[3]/p/span').click()
# #####Press on button "להרשמה"#####
# driver.find_element_by_id("ember973").send_keys("מרדכי רז")
# #####Registration Enter first name#####
# driver.find_element_by_id("ember975").send_keys("moti@energyteam.co.il")
# #####Enter email address#####
# driver.find_element_by_id("ember976").send_keys("123Qwe4r")
# time.sleep(2)
# #####Enter password#####
# driver.find_element_by_id("ember978").send_keys("123Qwe4r")
# #####Enter password again#####
# driver.find_element_by_xpath('//*[@id="ember980"]/label/i').click()
# #####Press on radio button "אני מסכים"#####
# driver.find_element_by_xpath('//*[@id="ember982"]/label/i').click()
# time.sleep(2)
# ##### Press on radio button "לא לקבל עידכונים"#####
# driver.find_element_by_xpath('//*[@id="ember971"]/button').click()
#####Press button  הרשמה" ...#####


driver.find_element_by_xpath('//*[@id="ember959"]').send_keys('moti@energyteam.co.il')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ember962"]').send_keys('123Qwe4r')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ember952"]/button').click()
###### login for B+C+D ######

#B. Home Screen
time.sleep(5)
driver.find_element_by_id("ember650_chosen").click()
driver.find_element_by_xpath ("//div[@id='ember650_chosen']/div/ul/li[5]").click()
#Pick a price point

driver.find_element_by_id("ember665_chosen").click()
driver.find_element_by_xpath ("//div[@id='ember665_chosen']/div/ul/li[3]").click()
#Pick the area

driver.find_element_by_id("ember674_chosen").click()
driver.find_element_by_xpath ("//div[@id='ember674_chosen']/div/ul/li[8]").click()
#Pick category

driver.find_element_by_id('ember709').click()
#Press the search button

time.sleep(5)
driver.get('https://buyme.co.il/supplier/20620')
#C- Choose business screen

driver.find_element_by_xpath('//*[@id="ember829"]').send_keys(200)
#Pick a Buisness Type a price

driver.find_element_by_xpath('//*[@id="ember828"]/div[2]/div/button').click()
#D - Sender & Receiver  # information screen

driver.find_element_by_xpath('//*[@id="ember971"]/label[1]/span[1]').click()
#Press radio button "למישהו אחר"

driver.find_element_by_xpath('//*[@id="ember1004"]').clear()
driver.find_element_by_xpath('//*[@id="ember1004"]').send_keys("אלונה רז")
#Enter receiver name

driver.find_element_by_xpath('//*[@id="ember1006"]').clear()
driver.find_element_by_xpath('//*[@id="ember1006"]').send_keys("מוטי רז")
# Enter sender name

driver.find_element_by_xpath('//*[@id="ember1014_chosen"]').click()
driver.find_element_by_xpath("//div[@id='ember1014_chosen']/div/ul/li[4]").click()
# Pick the event(Wedding / birthday)

driver.find_element_by_css_selector('textarea').clear()
driver.find_element_by_css_selector('textarea').send_keys("תודה רבה על הכל . אוהב אותך!!!")
# Enter a blessing

driver.find_element_by_name("fileUpload").send_keys('C:\\Users\\Moti\\Documents\\logo.png')
#Upload a picture

driver.find_element_by_xpath('//*[@id="ember964"]/div[3]/div/div[1]/label[1]').click()
#Press radio button "מיד אחרי התשלום"

driver.find_element_by_xpath('//*[@id="ember964"]/div[4]/div/div[1]/div[1]/div/button/span/span[2]').click()
#Pick Email / SMS option

driver.find_element_by_xpath('//*[@id="ember1479"]').clear()
driver.find_element_by_xpath('//*[@id="ember1479"]').send_keys ('0507135710')
driver.find_element_by_xpath('//*[@id="resendReciver"]').clear()
driver.find_element_by_xpath('//*[@id="resendReciver"]').send_keys('0504534536')
#Enter address / number and press

driver.find_element_by_xpath('//*[@id="ember964"]/div[4]/div/div[4]/div[2]/button[2]').click()
#save submit

driver.quit()6
#uuyuyuyuy