from selenium import webdriver
import pandas as pd
import time

def scrape(keyword, DataSize, Filename):
    url = "https://www.google.com/maps/search/"+keyword.replace(" ", "+")+"/"
    driver = webdriver.Chrome()
    driver.get(url)

    #Data frame
    df = pd.DataFrame(columns=["name", "rating", "reviews", "address", "phone", "url"])

    # Scroll Element
    scroll_element = driver.find_element(by = "xpath", value = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')

    if(DataSize > 6):
        print('Loading please wait...')
        while(True):
            cards_xpath = driver.find_elements(by = "xpath", value = '//div[@class="Nv2PK THOPZb CpccDe "]')
            if(len(cards_xpath) > DataSize):
                break
            try:
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_element)
                time.sleep(3)
            except:
                print("Scroll Error")
    else:
        cards_xpath = driver.find_elements(by = "xpath", value = '//div[@class="Nv2PK THOPZb CpccDe "]')
        time.sleep(3)
            
    i = 1
    for card in cards_xpath:
        if(i > DataSize):
            print("Saving data...")
            break

        print("progressing : {} / {}".format(i, DataSize))

        try:
            card.click()
            driver.execute_script("arguments[0].scrollTop = 100", scroll_element)
        except Exception as error:
            print(error)
            print("Not able to click")

        time.sleep(3)

        try:
            try:
                cafe_name_element = driver.find_element(by = "xpath", value = '//h1[@class="DUwDvf fontHeadlineLarge"]')
                cafe_name = cafe_name_element.text
            except:
                cafe_name = "NA"
            
            try:
                cafe_rating_element = driver.find_element(by = "xpath", value = '//div[@class="F7nice "]/span/span')
                cafe_rating = float(cafe_rating_element.text)
            except:
                cafe_rating = "NA"

            try:
                cafe_reviews_element = driver.find_element(by = "xpath", value = '//div[@class="F7nice "]/span[2]/span/span')
                cafe_reviews = int((cafe_reviews_element.text).replace("(", "").replace(")", "").replace(",", ""))
            except:
                cafe_reviews = "NA"
            
            try:
                cafe_address_element = driver.find_element(by = "xpath", value = '//div[@class="AeaXub"]/div[2]/div')
                cafe_address = cafe_address_element.text
            except:
                cafe_address = "NA"

            try:
                cafe_phone_element = driver.find_elements(by = "xpath", value = '//div[@class="m6QErb "]/div[@class="RcCsl fVHpi w4vB1d NOE9ve M0S7ae AG25L "]/button/div/div[@class="rogA2c "]/div[@class="Io6YTe fontBodyMedium kR99db "]')
                text_list = [(element.text).replace(" ", "") for element in cafe_phone_element]
                phone = [(next(int(d) for d in text_list if d.isdigit() and len(d) == 11))]
                cafe_phone = phone[0]
            except:
                cafe_phone = "NA"

            try:
                cafe_url_element = card.find_element(by = "xpath", value = "./a")
                url = cafe_url_element.get_attribute("href")
                cafe_urls = url
            except:
                cafe_urls = "NA"
        except:
            print("Element not found")
            break
        
        newData = {"name": cafe_name, "rating": cafe_rating, "reviews" : cafe_reviews  ,"address" : cafe_address, "phone" : cafe_phone, "url" : cafe_urls}
        df = df.append(newData, ignore_index=True)
        i += 1

    df.to_csv(Filename, index = False)
    return