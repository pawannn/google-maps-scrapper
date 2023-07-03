import GoogleMapScrapper.GoogleMapScrapper as GoogleMapScrapper

if __name__ == "__main__":
    search = "cafe in bangalore"
    dataSize = 100
    filename = search.replace(" ", "_") + ".csv"
    print("Starting the scrapper...")
    try:
        GoogleMapScrapper.scrape(search, dataSize, filename)
    except Exception as error:
        print(error)
    finally:    
        print("Scrapping Completed...")
        print("Data Saved in", filename)