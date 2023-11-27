import os
import requests
from selenium import webdriver



url = 'http://blog.samaltman.com'
dir_name = 'sam-altman'
os.makedirs(dir_name, exist_ok=True)  # Create a directory for saving all favorite blog posts
path = os.path.join(os.getcwd(), dir_name)

# Get user input for blog post titles
user_input = input("Enter the titles of Sam Altman's blog posts (separated by commas): ")
user_titles = [title.strip() for title in user_input.split(",")]

error_count = 0
downloaded = 0
incorrect_urls = []
for user_title in user_titles:
    fav_url = user_title.lower().replace('?', ' ').replace(',', ' ').replace('-', ' ').replace("'", " ").split()
    fav_url = '-'.join(fav_url)
    full_url = url + '/' + fav_url
    print('Accessing webpage {}'.format(full_url))
    res = requests.get(full_url)
    try:
        res.raise_for_status()
        file_path = os.path.join(path, fav_url + ".html")
        with open(file_path, 'wb') as file:
            for chunk in res.iter_content(100000):
                file.write(chunk)
        print("Successfully downloaded {}".format(fav_url))
        downloaded += 1
    except Exception as exc:
        print('Problem {}'.format(exc))
        error_count += 1
        incorrect_urls.append(fav_url)
    print()

print("Successfully downloaded {} blog posts and "
      "encountered problems with {} blog posts, namely: {}."
      .format(downloaded, error_count, incorrect_urls))

browser = webdriver.Chrome()
for i in incorrect_urls:
    i = i.replace('-', '+')
    browser.get("https://www.google.com/search?q=" + i + " sam altman")
    matched_elements = browser.find_elements_by_xpath('//a[contains(@href, "samaltman.com")]')
    if matched_elements:
        matched_elements[0].click()
        i = i.replace('+', '-')
        file_path = os.path.join(path, i + ".html")
        with open(file_path, 'w') as file:
            file.write(browser.page_source)

browser.quit()


