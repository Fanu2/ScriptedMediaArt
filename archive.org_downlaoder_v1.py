import os
import requests
from bs4 import BeautifulSoup


def search_archive_org(query):
    search_url = f"https://archive.org/search.php?query={query.replace(' ', '+')}"
    response = requests.get(search_url)

    if response.status_code != 200:
        print("Failed to retrieve search results.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='item-ttl')

    items = []
    for result in results:
        title = result.a.text.strip()
        url = 'https://archive.org' + result.a['href']
        items.append((title, url))

    return items


def list_files(item_url):
    response = requests.get(item_url)

    if response.status_code != 200:
        print("Failed to retrieve item page.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    file_list = []

    for file_link in soup.find_all('a', class_='stealth'):
        file_url = 'https://archive.org' + file_link['href']
        file_list.append(file_url)

    return file_list


def download_file(file_url, download_dir):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    local_filename = os.path.join(download_dir, file_url.split('/')[-1])

    with requests.get(file_url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print(f"Downloaded: {local_filename}")


if __name__ == "__main__":
    query = input("Enter your search query: ")
    download_dir = "downloads"

    print("Searching Archive.org...")
    items = search_archive_org(query)

    if not items:
        print("No items found.")
    else:
        print(f"Found {len(items)} items.")
        for i, (title, url) in enumerate(items):
            print(f"{i + 1}. {title} - {url}")

        choice = int(input("Enter the number of the item to download files from: ")) - 1
        item_url = items[choice][1]

        print(f"Listing files from: {item_url}")
        files = list_files(item_url)

        if not files:
            print("No files found.")
        else:
            print(f"Found {len(files)} files.")
            for i, file_url in enumerate(files):
                print(f"{i + 1}. {file_url.split('/')[-1]}")

            file_choice = input(
                "Enter the numbers of the files to download (comma-separated), or 'all' to download all: ")

            if file_choice.lower() == 'all':
                for file_url in files:
                    download_file(file_url, download_dir)
            else:
                selected_files = [files[int(i) - 1] for i in file_choice.split(',')]
                for file_url in selected_files:
                    download_file(file_url, download_dir)
