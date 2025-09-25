import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



url = "https://timesofindia.indiatimes.com/"

response = requests.get(url)


html_content = response.text


soup = BeautifulSoup(html_content, 'html.parser')


pretty_html = soup.prettify()

print(pretty_html) 

# print("Page Title:", soup.title.string)

def show_menu():
    print("\n=== Main Menu ===")
    print("1. Search for links in the web page.")
    print("2. Search for images in the web page.")
    print("3. Search for videos in the web page.")

def links():
    links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        full_link = urljoin(url, href)
        links.append(full_link)
    
    print("\n--- Links ---")
    for l in links:
        print(l)
        
def images():
    images = []
    for img in soup.find_all("img"):
        img_url = img.get("src")
        if img_url:
            full_img_url = urljoin(url, img_url) 
            images.append(full_img_url)

    print("\n--- Images ---")
    for i in images:
        print(i)

def videos():
    videos = []
    for video in soup.find_all("video"):
        src = video.get("src")
        if src:
            videos.append(urljoin(url, src))
        
       
        for source in video.find_all("source"):
            src = source.get("src")
            if src:
                videos.append(urljoin(url, src))

    print("\n--- Videos ---")
    if videos:
        for v in videos:
            print(v)
    else:
        print("No videos found.")

 



while True:
    show_menu()
    choice = input("Enter your choice (1-3): ").strip()

    match choice:
        case '1':
            links()

        case '2':
            images()
            
        case '3':
            videos()
            break

        case _:
            print("Invalid choice. Please try again.")