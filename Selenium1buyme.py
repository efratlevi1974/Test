from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/home/efat/Documents/DevOps/Selenium/chromedriver")

driver.get('https://buyme.co.il') #login to byme web site
driver.find_element_by_class_name("seperator-link").click() # כניסה-הרשמה
driver.find_element_by_xpath("//div[@class='lightbox-content']/p[@class='switch-text']/span[@class='text-btn']").click() #להרשמה
driver.find_element_by_xpath("//div[@class='field'][1]/label[@id='ember972']/input[@id='ember973']").send_keys("efrat levi")
driver.find_element_by_xpath("//div[@class='option oldschool']/form[@id='ember971']/div[@class='field'][2]/label[@id='ember974']/input[@id='ember975']").send_keys("leefrat@walla.com")
driver.find_element_by_xpath("//div[@class='field'][3]/label[@id='ember976']/input[@id='valPass']").send_keys("Efrat1974")
driver.find_element_by_xpath("//div[@class='option oldschool']/form[@id='ember971']/div[@class='field'][4]/label[@id='ember978']/input[@id='ember979']").send_keys("Efrat1974")
driver.find_element_by_xpath("//div[@class='option oldschool']/form[@id='ember971']/div[@id='ember980']/label/i[@class='fa fa-check ']").click() #אני מסכים לתנאי התקנון
driver.find_element_by_xpath("//div[@class='main-container main-padding']/div[@class='ui-lightbox login']/div[@class='inner']/div[@class='box']/div[@class='lightbox-content']/div[@class='main-form']/div[@class='option oldschool']/form[@id='ember971']/button[@class='ui-btn orange large']").click() # הרשמה ל BUYME
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html[@class='chrome']/body[@class='rtl ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember558']/div[@class='main-container main-padding']/div[@class='ui-lightbox login']/div[@class='inner']/div[@class='box']/div[@class='lightbox-content']/p[@class='switch-text']/span[@class='text-btn']").click() #לכניסה
driver.find_element_by_xpath("/html[@class='chrome']/body[@class='rtl ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember558']/div[@class='main-container main-padding']/div[@class='ui-lightbox login']/div[@class='inner']/div[@class='box']/div[@class='lightbox-content']/div[@class='main-form']/div[@class='option oldschool']/form[@id='ember984']/div[@class='field']/label[@id='ember985']/input[@id='ember986']").send_keys("leefrat@walla.com")
driver.find_element_by_xpath("/html[@class='chrome']/body[@class='rtl ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember558']/div[@class='main-container main-padding']/div[@class='ui-lightbox login']/div[@class='inner']/div[@class='box']/div[@class='lightbox-content']/div[@class='main-form']/div[@class='option oldschool']/form[@id='ember984']/div[@class='field last']/label[@id='ember987']/input[@id='ember988']").send_keys("Efrat1974")
driver.find_element_by_xpath("/html[@class='chrome']/body[@class='rtl ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember558']/div[@class='main-container main-padding']/div[@class='ui-lightbox login']/div[@class='inner']/div[@class='box']/div[@class='lightbox-content']/div[@class='main-form']/div[@class='option oldschool']/form[@id='ember984']/button[@class='ui-btn orange large']").click() # BUYME כניסה ל

#driver.find_element_by_class_name("social-btn.facebook").click()



#driver.find_element_by_xpath("/html[@class='chrome']/body[@class='rtl ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember558']/div[@class='main-container main-padding']/div[@class='ui-lightbox login']/div[@class='inner']/div[@class='box']/div[@class='lightbox-content']/div[@class='main-form']/div[@class='option oldschool']/form[@id='ember971']/div[@class='field'][1]/label[@id='ember972']/input[@id='ember973']").send_keys("efrat levi")




