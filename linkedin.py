from selenium import webdriver
from  selenium.webdriver.common.by import By
import time

class Login():
    def test(self):
        baseURL = "https://www.linkedin.com/"
        driverLocation = "C:\\Users\\No Distraction\\PycharmProjects\\GithubAutomator\\driver\\chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        '''  Sign in part   '''
        sign_btn = driver.find_element(By.LINK_TEXT,"Sign in")
        sign_btn.click()
        userName = "Cpusendra@gmail.com"
        user = driver.find_element(By.ID, "username")

        user.send_keys(userName.lower())
        time.sleep(1)

        password = driver.find_element(By.ID,'password')
        password.clear()
        password.send_keys("kanchi123")
        time.sleep(1)
        signIn = driver.find_element(By.XPATH,"//button[@class='btn__primary--large from__button--floating']")
        signIn.click()

        time.sleep(5)

        Network_btn = driver.find_element(By.ID,"mynetwork-tab-icon")
        Network_btn.click()
        time.sleep(2)

        connection_btn = driver.find_element(By.CSS_SELECTOR,"div.mn-community-summary__entity-info>li-icon.mr4>svg")
        connection_btn.click()

        search_with_filters = driver.find_element(By.CSS_SELECTOR,"div.mn-connections__search-container.ember-view>a")
        search_with_filters.click()

        current_company_btn = driver.find_element(By.XPATH,"//span[text()='Current companies']")
        current_company_btn.click()
        time.sleep(5)

        dropdown = driver.find_elements(By.CSS_SELECTOR,"p.search-s-facet-value__text.display-flex>span")
        companies = []
        for item in dropdown:
            if item.text not  in companies:
                companies.append(item.text)

        company = "Leapfrog"

        for item in companies:
            if company in item:
                company = item

        for item in dropdown:
            if item.text == company:
                company_btn = driver.find_element(By.XPATH,f"//span[text()='{company}']")
                company_btn.click()

        time.sleep(5)
        apply_btn = driver.find_elements(By.XPATH,"//button[@class='facet-collection-list__apply-button ml2 artdeco-button artdeco-button--2 artdeco-button--primary ember-view']//span[text()='Apply']")
        apply_btn[2].click()

        time.sleep(10)

        company_employee = driver.find_elements(By.CSS_SELECTOR,'.actor-name-with-distance.search-result__title.single-line-truncate.ember-view')
        company_name_post = driver.find_elements(By.XPATH,'//p[contains(@class,"subline-level-1 t-14 t-black t-normal search-result__truncate")]')
        employee = []
        post_company_name =[]



        for i in range(len(company_employee)):
            post_company_name.append([company_employee[i].text,company_name_post[i].text])

        my_file = open("linkeden_connection.txt", "w")

        for item in post_company_name:
            my_file.write(" ".join(item) + "\n")

        my_file.close()










ll = Login()
ll.test()

