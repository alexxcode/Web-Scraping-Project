import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from textblob import TextBlob
import pandas as pd

url = 'http://blog.samaltman.com'
dir_name = 'sam-altman'

# Function to download html posts

def PostInDir(a, b):

    url = a
    dir_name = b

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


# Function Sentiment Analysis 

def Sentiment(a, b):

    url = a
    user_input = b
    fav_url = user_input.lower().replace('?', ' ').replace(',', ' ').replace('-', ' ').replace("'", " ").split()
    fav_url = '-'.join(fav_url)
    full_url = url + '/' + fav_url
    print('Accessing webpage {}'.format(full_url))
    res = requests.get(full_url)
    try:
        res.raise_for_status()
        html_content = res.text
        print("Successfully downloaded the post: {}".format(fav_url))
    except Exception as exc:
        print('Problem {}'.format(exc))

    soup2 = BeautifulSoup(html_content, 'html.parser')
    paragraphs = [p.get_text() for p in soup2.find_all('p')]

    str1 = ''.join(paragraphs)
    
    cleanP = re.sub(r'[^\w\s]', '', str1)

    blob = TextBlob(cleanP)
    sentiment = blob.sentiment.polarity
    
    x = sentiment

    if x < -0.19:
        print("=======================")
        print("Post most likely Angry! :/")
        print("=======================")
    elif x > 0.19:
        print("=======================")
        print("Post most likely Happe! :)")
        print("=======================")
    else:
        print("=======================")
        print("Post most likely Neutral -.-")
        print("=======================")


def Post1(a, b):

    url = a
    dir_name = b

    os.makedirs(dir_name, exist_ok=True)  # Create a directory 
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
        full_url = url 
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


    
def get_titles(url):
    url_base = url
    numpags = 12
    alltitles = []

    for n in range(1, numpags + 1):
        url_pag = f"{url_base}?page={n}"
        try:
            response = requests.get(url_pag)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            titles = soup.find_all("h2")  # Change 'h2' ccording to the blog
            titles_pag = [title.text.strip() for title in titles]
            alltitles.extend(titles_pag)
        except Exception as e:
            print(f"Error getting page titles {n}: {e}")

    return alltitles




def menu():
    while True:
        print("Menu:")
        print("1. Search all post titles on Sam Altman's blog")
        print("2. Show the titles of Sam Altman's blog posts")
        print("3. Download Sam Altman's posts in sam-altman directory")
        print("4. Analyse de Sentiment of certain Sam Altman's post")
        print("5. Option 5 (BUILDING)")
        print("6. Exit")
        opcion = input("Select yout option number ")
        if opcion == "1":
                print("=======================")
                titles=get_titles(url)
                df_titles=pd.DataFrame(titles)
                df_titles.to_csv('san_titles.csv', index=False)
                print("=======================")
        elif opcion == "2":
                print("=======================")
                df_titles= pd.read_csv('san_titles.csv')
                print(df_titles)
                print("=======================")
        elif opcion == "3":
                PostInDir(url, dir_name)
        elif opcion == "4":
                b=input("Type the post's title to analyse: ")
                print("=======================")
                Sentiment(url, b)
                print("=======================")
        elif opcion == "5":
            fun()
        elif opcion == "6":
            return
        else:
            print(" Invalid option. Try again.")


def fun():
    print("BUILDING")
    