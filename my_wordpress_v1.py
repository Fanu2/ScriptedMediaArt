import requests
from requests.auth import HTTPBasicAuth

# WordPress site URL and REST API endpoint
wp_site_url = 'https://your-wordpress-site.com/wp-json/wp/v2/posts'

# API credentials (username and application password or API token)
username = 'singh1021'
application_password = 'Taruana61*'

# Data for the new post
post_data = {
    'title': 'My New Post',
    'content': 'This is the content of my new post.',
    'status': 'publish'  # Status can be 'publish', 'draft', etc.
}

# Make the POST request to create a new post
response = requests.post(
    wp_site_url,
    auth=HTTPBasicAuth(username, application_password),
    json=post_data
)

# Check the response
if response.status_code == 201:
    print('Post created successfully!')
    post = response.json()
    print(f"Post ID: {post['id']}")
    print(f"Post URL: {post['link']}")
else:
    print(f"Failed to create post. Status code: {response.status_code}")
    print(f"Response: {response.text}")
