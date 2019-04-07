# Install the Python Requests library:
# `pip install requests`

import requests
from pprint import pprint
import json


def get_listings():
    '''
    Get a list of WM Listings for a specific area
    '''

    try:
        response = requests.get(
            url="https://api-g.weedmaps.com/discovery/v1/listings",
            params={
                "filter[any_retailer_services][]": "storefront",
                "filter[region_slug[deliveries]]": "east-la",
                "filter[region_slug[dispensaries]]": "east-la",
                "filter[region_slug[doctors]]": "east-la",
                "page_size": "100",
                "size": "100",
            },
        )
        listings_response = json.loads(response.content)
        listings_data = listings_response.get('data',{}).get("listings",[])
        slugs=[]
        for listing in listings_data:
            slug = listing["slug"]
            slugs.append(slug)
        return slugs
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

def get_menu():
    url = "https://api-g.weedmaps.com/discovery/v1/listings/dispensaries/cali-culture/menu_items"
    params = {
                "page": "1",
                "page_size": "150",
                "limit": "150",
                "filter[category_names][]": "concentrate",
    }
    try:
        response = requests.get(url=url, params=params)
        menu_response = json.loads(response.content)
        item_name = menu_response.get('data',{}).get('menu_items',[])
        pprint(item_name)
        # pprint(menu_response)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')




get_listings()
get_menu()
