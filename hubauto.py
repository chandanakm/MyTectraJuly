import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(r'C:\Users\Karthik\Downloads\chromedriver.exe')
driver.get('https://app.hubspot.com/login')
driver.maximize_window()
print("completed level-1")
time.sleep(3)
driver.find_element_by_xpath('//*[@class="google-sign-in"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('chandana.sathnur@gmail.com')
driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@class="whsOnd zHQkBf"]').send_keys('brumamurthy')
driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click()
time.sleep(10)
print("completed level-2")
mainmenu = driver.find_element_by_link_text("Contacts")
action=ActionChains(driver)
action.move_to_element(mainmenu).perform()
mainmenu.click()
submenu = wait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nav-secondary-contacts")))
submenu.click()
print("completed level-3")












'''

a= ActionChains(driver)
a.move_to_element(driver.find_element_by_css_selector("a[href='https://app.hubspot.com/contacts/6891827/contacts']")).perform()
print("complete3")
time.sleep(20)
driver.find_element_by_css_selector("a[href='https://app.hubspot.com/contacts/6891827/contacts']").sendKeys(Keys.ENTRY)
driver.close()
select = Select(driver.find_element_by_xpath('//*[@class="primary-link"]'))
print("nav complete")
select.select_by_visible_text('Contacts')



driver.find_element_by_xpath('//*[@class="uiButton private-button--primary private-button private-button--default private-button--non-link"]').click()
#driver.find_element_by_xpath(".//*[@class='mobile-nav-left-container']")
#driver.find_element_by_xpath(".//div[@class='nav-links']")
#driver.find_element_by_xpath(".//ul[@class='primary-links']")
#driver.find_element_by_xpath(".//li[@class='expandable']").click()
driver.find_element_by_xpath('//*[@class="navSecondaryLink"]').click()
print("nav complete")



select = Select(driver.find_element_by_xpath('//*[@id="/html/body/div[2]/nav/div/div[1]/div[1]/div/div/ul/li[2]/a"]'))
print("nav complete")
select.select_by_visible_text('Contacts')

WebElement testDropDown = driver.find_element_by_class_name("expandable"))
Select dropdown= new Select(testDropDown)

sd=Select(driver.find_element_by_id('nav-primary-contacts-branch'))
sd.select_by_visible_text('Contacts')

myselect = Select(driver.find_element_by_class_name("expandable active"))
myselect.select_by_value("0")

select = Select(driver.find_element_by_xpath('//*[@class="primary-link"]'))
print("nav complete")
select.select_by_visible_text('Contacts')

#Select      = new Select(driver.find_element_by_xpath('//@id="nav-primary-contacts-branch"]')
s1.Select_by_visible_text('contacts')
                             
navigation = driver.find_element_by_xpath("//[@class='navbar-inner']")
leftnav = driver.find_element_by_xpath("//[@class='desktop-nav-left-container']")
ull = driver.find_element_by_xpath("ul//[@class='primary-links']")
contacts=driver.find_element_by_xpath("li//[@class='expandable']")

Actions action = new Actions(driver)
action.moveToElement(navigation).click().perform()
action.moveToElement(leftnav).click().perform()
action.moveToElement(ull).click().perform()
action.moveToElement(contacts).click().perform()
Thread.sleep(3000)


//*[@id="nav-primary-contacts-branch"]

/html/body/div[2]/nav/div/div[1]/div[1]/div/div/ul/li[2]/a

driver.find_element_by_link('https//app.hubspot.com/demo-tour/6891827/no-more-spreadsheets/flowId=new-ic').click()

a= ActionChains(driver)
a.move_to_element(driver.find_element_by_css_selector("a[href='https://app.hubspot.com/contacts/6891827/contacts']")).build().perform()
print("complete3")
#a.moveToElement(driver.findElement_by_css_selector("a[href='']").build().perform()
#driver.findElement_by_cssSelector("a[href='']").sendKeys(Keys.ENTRY)


ids = driver.find_elements_by_xpath('//*[@href]')
for ii in ids:
    print(ii.get_attribute('href'))
time.sleep(4)
print("complete3")
'''

