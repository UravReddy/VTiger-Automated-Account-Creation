from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


usernameStr = 'username'
passwordStr = 'password'

browser = webdriver.Chrome()

browser.get(('http://10.0.0.101/mixvas'))

# fill in username and hit the next button

username = browser.find_element_by_id('username')
username.send_keys(usernameStr)

username = browser.find_element_by_id('password')
username.send_keys(passwordStr)

username.send_keys(Keys.ENTER)

agentUN = ['User1','User2','User3','User4','User5'] #Username
AgentFN = ['User1','User2','User3','User4','User5'] #First Name
agentLN = ['User1','User2','User3','User4','User5'] #LastName
agentPW = ['qa24','qa10','qa3','qa25','qa23'] #Password
l= len(agentUN)

for x in range(l):
        #vtiger url for creating accounts
        browser.get(('http://10.0.0.101/mixvas/index.php?module=Users&parent=Settings&view=List')) 
        vari1 = browser.find_element_by_xpath('//*[@id="page"]/div[3]/div/div[2]/div/div[2]/span[1]/span[2]/button')
        vari1.click()    
        #select field and input list value
        username =browser.find_element_by_id('Users_editView_fieldName_user_name')
        username.send_keys(agentUN[x])
        firstname= browser.find_element_by_id('Users_editView_fieldName_first_name')
        firstname.send_keys(AgentFN[x])
        password= browser.find_element_by_id('Users_editView_fieldName_user_password')
        password.send_keys(agentPW[x])  
        mail= browser.find_element_by_id('Users_editView_fieldName_email1')
        mail.send_keys('youremailaddress')
        lastname =browser.find_element_by_id('Users_editView_fieldName_last_name')
        lastname.send_keys(agentLN[x])
        password= browser.find_element_by_id('Users_editView_fieldName_confirm_password')
        password.send_keys(agentPW[x])
        role=browser.find_element_by_id('Users_editView_fieldName_is_admin')

        #Select the desired user role from drop down
        role.send_keys(Keys.TAB, Keys.DOWN, Keys.DOWN, Keys.DOWN,Keys.DOWN,Keys.ENTER,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.ENTER)
        save=browser.find_element_by_xpath('//*[@id="EditView"]/div[1]/span[2]/span/button')
        save.click()
        #sleep for 4 seconds        
        time.sleep(4)
        browser.get(('http://10.0.0.101/mixvas/index.php?module=Users&parent=Settings&view=List'))

