# Decathlon US Scraper

## Description

This project is a Python-based web scraper designed to extract product data from the Decathlon website. It utilizes the Scrapy framework to collect information such as product names, prices, descriptions, and more from the "Bags & Backpacks" category.

Read the step by step tutorial on [Scrape Shopify Data with Python: A Comprehensive Shopify Scraper Tutorial](https://rayobyte.com/community/scraping-project/scrape-shopify-data-with-python-a-comprehensive-shopify-scraper-tutorial/)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Extraction Process](#data-extraction-process)
- [Scrapy Settings](#scrapy-settings)
- [Proxy Rotation (Optional)](#proxy-rotation-optional)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Comprehensive Data Collection**: Extracts various attributes including:
  - Category
  - Brand
  - Product Name
  - Star Rating
  - Number of Reviews
  - Description
  - Product ID
  - Color and Size Variations
  - Regular and Previous Prices
  - Image URLs

- **CSV Output**: Data is stored in a CSV file for easy analysis.
- **Ethical Scraping Practices**: Adheres to responsible scraping guidelines.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ainacodes/decathlonUS_scraper.git
   cd decathlonUS_scraper
2. **Install Scrapy**:
   ```bash
   pip install scrapy

## Usage

To run the scraper, execute the following command in your terminal:
```bash
scrapy crawl bag_backpacks
```

This command initiates the scraping process, and the results will be saved in `products_details.csv`.

## Data Extraction Process

The scraper follows these steps:
1. **Retrieve Category URLs**: Collects all relevant URLs within the "Bags & Backpacks" category.
2. **Extract Product URLs**: Gathers individual product links for detailed scraping.
3. **Scrape Product Details**: For each product, it extracts:
    - Category, Brand, Product Name, Star Rating, Number of Reviews, Description.
    - Color and Size variations, Regular Price, Previous Price.
    - Image URLs (Feature and Carousel).
4. **Store Data**: Compiles all extracted data into a CSV file.


## Scrapy Settings

Adjust settings in `settings.py` for optimal performance:

```python
BOT_NAME = "decathlonUS_scraper"
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 8
DOWNLOAD_DELAY = 2
FEEDS = {
    'products_details.csv': {
        'format': 'csv',
        'overwrite': True,
    },
}
```

## Proxy Rotation (Optional)
Using proxy rotation can help prevent your IP from being blocked when scraping at scale. To implement this:
1. Obtain a list of proxies (e.g., from [Rayobyte](https://rayobyte.com/)).
2. Configure your Scrapy middleware inside `settings.py` to use these proxies.
   ```python
   DOWNLOADER_MIDDLEWARES = {
    "decathlonUS_scraper.middlewares.DecathlonusScraperDownloaderMiddleware": 543,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
   }

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.


## License
This project is licensed under the MIT License.
