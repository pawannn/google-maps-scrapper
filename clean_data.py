import GoogleMapScrapper.GoogleMapScrapper as GoogleMapScrapper
import pandas as pd
import os

if __name__ == "__main__":
    search = "cafe in bangalore"
    dataSize = 50
    print("Starting the scrapper...")
    GoogleMapScrapper.scrape(search, dataSize)
    
    print("Scrapping Completed...")
    print("cleaning data")

    df = pd.read_csv('data.csv')

    df['reviews'] = df['reviews'].apply(lambda x : int(x.replace('(', '').replace(')', '').replace(',', '')))
    df['rating'] = df['rating'].apply(lambda x : float(x))

    filename = search.replace(" ", "_")+".csv"
    df.to_csv(filename, index=False)
    print("Data saved in {}".format(filename))
    try:
        os.remove('data.csv')
    except:
        print("Error in removing file")
    finally:
        print("Successfully Completed")