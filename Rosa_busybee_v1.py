from facebook_scraper import get_posts
from requests.exceptions import HTTPError

page_name = 'ultimately4u'  # Replace with the actual page name
num_posts = 10
cookies = {
    'cookie_name': 'cookie_value',  # Replace with your actual cookie names and values
    # Add other cookies if needed
}

try:
    for post in get_posts(page_name, pages=num_posts, cookies=cookies):
        print(post)
except HTTPError as e:
    print(f"An error occurred: {e}")
