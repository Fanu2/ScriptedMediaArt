from facebook_scraper import get_posts
import json

# Define your page name and the number of posts to scrape
page_name = 'https://www.facebook.com/rosabusybee'  # Replace with the Facebook page name
num_posts = 10  # Adjust the number of posts to scrape

# Scrape posts from the page
posts = []
for post in get_posts(page_name, pages=num_posts):
    posts.append(post)

# Save posts to a JSON file
with open('facebook_posts.json', 'w') as f:
    json.dump(posts, f, indent=4)

print(f'Successfully saved {num_posts} posts to facebook_posts.json')
