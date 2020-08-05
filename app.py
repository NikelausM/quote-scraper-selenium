import os

from selenium import webdriver

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError


# if in script form
if __name__ == "__main__":

    try:
        BASE_URL = "http://quotes.toscrape.com/search.aspx"
        chrome = webdriver.Chrome(executable_path=os.environ["CHROME_DRIVER"])
        chrome.get(BASE_URL)
        page = QuotesPage(chrome)

        author = input("Enter the author you'd like quotes from: ")
        tag = input("Enter your tag: ")

        print(page.search_for_quotes(author, tag))
    except InvalidTagForAuthorError as e:
        print(e)
    except Exception as e:
        print(e)
        print("An unknown error occurred. Please try again.")
