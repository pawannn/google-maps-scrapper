# Google Maps Scrapper

- It helps to scrape places that you wanna search and stores the result in an Excell sheet

## How to Use

- Clone the Github Repo or Download the repository.
- The main Code looks like This :
```python
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
```

- You can change the `search` vairable string as per your search.
- The `dataSize` refers to the amount of data that you need, You can change as per your need.

- Run the program using the command `python main.py`
- The Chromedriver will open up automated and You may see the progress in the terminal.
- After the program is completed, You can view scraped data in the ".csv" file.

Thank You