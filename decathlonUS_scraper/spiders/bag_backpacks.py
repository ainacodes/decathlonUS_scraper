import scrapy


class BagBackpacksSpider(scrapy.Spider):
    name = "bag_backpacks"
    allowed_domains = ["decathlon.com"]
    start_urls = ["https://www.decathlon.com/collections/backpacks-bags"]
    base_url = "https://decathlon.com"

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_url_categories)

    def parse_url_categories(self, response):
        categories = response.css('ul.de-u-listReset ul.de-u-listReset')
        category_urls = categories[2].css('a::attr(href)').getall()
        for relative_url in category_urls:
            url = self.base_url + relative_url
            yield scrapy.Request(url, callback=self.parse_product_url)

    def parse_product_url(self, response):
        product_urls = response.css(
            'a.js-de-ProductTile-link::attr(href)').getall()
        unique_product_urls = list(set(product_urls))
        for product_url in unique_product_urls:
            url = self.base_url + product_url
            yield scrapy.Request(url, callback=self.parse_product)

    def parse_product(self, response):
        breadcrumb_links = response.css('nav.breadcrumb a::text').getall()
        category = ' / '.join(breadcrumb_links).strip()
        brand = response.css(
            'span.de-u-textGrow2.de-u-md-textGrow3.de-u-lg-textGrow4.de-u-textBold::text').get().strip()
        product_name = response.css('h1::text').get().strip()
        star_rating = response.css('span.de-StarRating.de-u-spaceRight06 span.de-u-hiddenVisually::text').get(
        ).strip().replace('(Average rating: ', '').replace(' out of 5 stars,', '')
        reviews = response.css(
            'span.de-u-textMedium.de-u-textSelectNone.de-u-textBlue::text').get().strip()
        description = response.css('ul.about-this-item li::text').getall()
        all_description = '\n'.join(description)

        # Items that change depending on the variations
        details = response.css('select#productSelect option::text').getall()

        colors = []
        sizes = []
        product_ids = []
        regular_prices = []

        for detail in details:
            parts = detail.split(' / ')
            color = parts[0].strip()
            size = parts[1]

            infos = parts[2].split(' - ')
            product_id = infos[0]
            price = infos[1].replace('USD', '').strip()

        # Check if the price is not "Sold out"
            if price != "Sold out":
                # Append the extracted values to their respective lists
                colors.append(color)
                sizes.append(size)
                product_ids.append(product_id)
                regular_prices.append(price)
            else:
                continue  # Skip the "Sold out" case entirely

        prev_price = response.css(
            'del.js-de-CrossedOutPrice span.js-de-PriceAmount::text').get().strip()
        if prev_price:
            previous_price = prev_price
        else:
            previous_price = ''
        feature_imgs = response.css(
            'img.de-CarouselFeature-image::attr(data-src)').getall()
        feature_img = [f'https:{img}' for img in feature_imgs]
        carousel_imgs = response.css(
            'div.de-CarouselThumbnail-slide img::attr(data-src)').getall()
        carousel_img = [f'https:{img}' for img in carousel_imgs]
        url = response.url

        item = {
            'Category': category,
            'Brand': brand,
            'Product Name': product_name,
            'Star Rating': star_rating,
            'Number of reviews': reviews,
            'Description': all_description,
            'Product ID': ', '.join(product_ids),
            'Color': ', '.join(colors),
            'Size': ', '.join(sizes),
            'Regular Price': ', '.join(regular_prices),
            'Previous Price': previous_price,
            'Feature Image URLs': ', '.join(feature_img),
            'Carousel Image URLs': ', '.join(carousel_img),
            'URL': url
        }

        yield item
