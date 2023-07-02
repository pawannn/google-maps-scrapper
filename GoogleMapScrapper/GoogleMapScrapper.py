from selenium import webdriver
import pandas as pd
import time

def scrape(keyword, DataSize):
    url = "https://www.google.com/maps/search/"+keyword.replace(" ", "+")+"/"
    driver = webdriver.Chrome()
    driver.get(url)

    if(DataSize > 6):
        print('Loading please wait...')
        scroll = (DataSize % 7) + 20
        i = 1
        while(i < scroll):
            try:
                section_element = driver.find_element(by = "xpath", value = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", section_element)
                i += 1
                time.sleep(3)
            except:
                print("Scroll Error")
    
    cafe_name = []
    cafe_rating = []
    cafe_reviews = []
    cafe_address = []
    cafe_phone = []
    cafe_urls = []

    def checkphone(numbers):
        for i in numbers:
            number = i.replace(" ",'')
            if(number.isdigit() and (len(number) == 11)):
                return(int(number))
        return('NA')
            
    i = 1
    try:
        cards_xpath = driver.find_elements(by = "xpath", value = '//div[@class="Nv2PK THOPZb CpccDe "]')
        print(len(cards_xpath))
    except:
        print("Element not found")

    for card in cards_xpath:
        isClicked = False
        print("progressing : {} / {}".format(i, DataSize))
        if(i == DataSize+1):
            print("Saving data...")
            break

        try:
            card.click()
            isClicked = True
            driver.execute_script("arguments[0].scrollTop = 100", section_element)
        except Exception as error:
            print(error)
            print("Not able to click")

        time.sleep(3)

        if(isClicked):

            try:
                try:
                    cafe_name_element = driver.find_element(by = "xpath", value = '//h1[@class="DUwDvf fontHeadlineLarge"]')
                    cafe_name.append(cafe_name_element.text)
                except:
                    cafe_name.append("NA")
                
                try:
                    cafe_rating_element = driver.find_element(by = "xpath", value = '//div[@class="F7nice "]/span/span')
                    cafe_rating.append(cafe_rating_element.text)
                except:
                    cafe_rating.append("NA")

                try:
                    cafe_reviews_element = driver.find_element(by = "xpath", value = '//div[@class="F7nice "]/span[2]/span/span')
                    cafe_reviews.append(cafe_reviews_element.text)
                except:
                    cafe_reviews.append("NA")
                
                try:
                    cafe_address_element = driver.find_element(by = "xpath", value = '//div[@class="AeaXub"]/div[2]/div')
                    cafe_address.append(cafe_address_element.text)
                except:
                    cafe_address.append("NA")

                try:
                    cafe_phone_element = driver.find_elements(by = "xpath", value = '//div[@class="m6QErb "]/div[@class="RcCsl fVHpi w4vB1d NOE9ve M0S7ae AG25L "]/button/div/div[@class="rogA2c "]/div[@class="Io6YTe fontBodyMedium kR99db "]')
                    text_list = [element.text for element in cafe_phone_element]
                    phno = checkphone(text_list)
                    cafe_phone.append(phno)
                except:
                    cafe_phone.append("NA")

                try:
                    cafe_url_element = card.find_element(by = "xpath", value = "./a")
                    url = cafe_url_element.get_attribute("href")
                    cafe_urls.append(url)
                except:
                    cafe_urls.append("NA")
            except:
                print("Element not found")
                break
            i += 1

    df = pd.DataFrame({"Name" : cafe_name, "rating" : cafe_rating, "reviews" : cafe_reviews, "Address" : cafe_address, "phone" : cafe_phone, 'url': cafe_urls})
    df.to_csv('data.csv', index = False)
    return