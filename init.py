import requests
from bs4 import BeautifulSoup

def search_amazon_germany(product_name):
    base_url = "https://www.amazon.de"
    search_url = f"{base_url}/s?field-keywords={product_name}"

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")

    product_list = []

    for item in soup.find_all("div", class_="s-include-content-margin"):
        title = item.find("span", class_="a-text-normal")
        price = item.find("span", class_="a-offscreen")
        if title and price:
            product_list.append({
                "title": title.text.strip(),
                "price": price.text.strip()
            })

    return product_list

def search_allegro_poland(product_name):
    base_url = "https://allegro.pl"
    search_url = f"{base_url}/listy?string={product_name}"

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")

    product_list = []

    for item in soup.find_all("div", class_="_9c44d_2IaLu"):
        title = item.find("a", class_="ebc9909")
        price = item.find("div", class_="_9c44d_1uURC")
        if title and price:
            product_list.append({
                "title": title.text.strip(),
                "price": price.text.strip()
            })

    return product_list

if __name__ == "__main__":
    product_name = "Garbage bags"
    
    amazon_germany_results = search_amazon_germany(product_name)
    allegro_poland_results = search_allegro_poland(product_name)
    
    print("Amazon Germany Results:")
    for idx, product in enumerate(amazon_germany_results, start=1):
        print(f"{idx}. {product['title']} - {product['price']}")

    print("\nAllegro Poland Results:")
    for idx, product in enumerate(allegro_poland_results, start=1):
        print(f"{idx}. {product['title']} - {product['price']}")
