# scrapy-indya
This is a Scrapy project to scrape www.houseofindya.com

## How to install the project on your local machine:
```
git clone https://github.com/AbhinandanM/scrapy-indya.git

cd ~/scrapy-indya

pip install requirements.txt

```
## Extracted data
```
[
  {
    "product_name": "Gold Maroon Kundan Floral Necklace Set",
    "product_price": "2250.00", 
    "product_img_url": "https://img.faballey.com/Images/Product/ZNS00058/1.jpg"},
    .....
    .....
  }
]
```
## Running the spiders
You can run a spider using the scrapy crawl command, such as:
```
scrapy crawl Items
```
To generate a CSV file, run command:
```
scrapy crawl Items -o <FILENAME>.csv
```
To generate a JSON file, run command:
```
scrapy crawl Items -o <FILENAME>.json
```
## Project Structure
```
indyascrape:
│   requirements.txt
│   scrapy.cfg
│
└───indyascrape
    │   items.py
    │   middlewares.py
    │   pipelines.py
    │   settings.py
    │   __init__.py
    │
    └───spiders
            necklace_scrape.py
            __init__.py
```
