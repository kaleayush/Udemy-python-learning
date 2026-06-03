from asyncio import threads
import threading
import requests
from bs4 import BeautifulSoup


urls=[
    "https://docs.langchain.com/oss/python/deepagents/overview",
    "https://docs.langchain.com/oss/python/deepagents/quickstart",
    "https://docs.langchain.com/oss/python/deepagents/customization"
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'fetch {len(soup.text)} charaters from {url}')

threads= []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print("allwebpagesfetch")