import time

from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    """
    A class that retreives a web page from a URL, and interacts with it.
    """

    def __init__(self, browser: WebDriver):
        """
        Parameters
        ----------
        browser : WebDriver
            The chrome web driver.
        """

        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        """Returns the web page's quotes.

        Returns
        -------
        List[QuoteParser]
            A list of QuoteParser representing the web page's quotes.
        """

        quote_tags = self.browser.find_elements_by_css_selector(
            QuotesPageLocators.QUOTE)
        quote_parsers = [QuoteParser(e) for e in quote_tags]
        return quote_parsers

    @property
    def author_dropdown(self) -> Select:
        """Selects and returns the author dropdown menu.

        Returns
        -------
        Select
            The author drop down menu.
        """

        element = self.browser.find_element_by_css_selector(
            QuotesPageLocators.AUTHOR_DROPDOWN)
        # puts element in Select wrapper (dropdown)
        select_element = Select(element)

        return select_element  # puts element in Select wrapper (dropdown)

    @property
    def tags_dropdown(self) -> Select:
        """Selects and returns the tag dropdown menu.

        Returns
        -------
        Select
            The tags drop down menu.
        """

        element = self.browser.find_element_by_css_selector(
            QuotesPageLocators.TAG_DROPDOWN)
        # puts element in Select wrapper (dropdown)
        select_element = Select(element)

        return select_element

    @property
    def search_button(self) -> WebElement:
        """Returns the search button.

        Returns
        -------
        WebElement
            The author drop down menu.
        """

        element = self.browser.find_element_by_css_selector(
            QuotesPageLocators.SEARCH_BUTTON)
        return element

    def select_author(self, author_name: str):
        """Selects author name in dropdown.

        Parameters
        ----------
        author_name : str
            The author name to be selected.
        """

        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        """Gets available tags from dropdown.

        Returns
        -------
        List[str]
            The list of options in the tag drop down menu.
        """

        available_tags = [option.text.strip()
                          for option in self.tags_dropdown.options]
        return available_tags

    def select_tag(self, tag_name: str):
        """Selects tag in dropdown.

        Parameters
        ----------
        tag_name : str
            The string value of the tag name to be selected.
        """

        self.tags_dropdown.select_by_visible_text(tag_name)

    def search_for_quotes(self, author_name: str,
                          tag_name: str) -> List[QuoteParser]:
        """Searches for quotes by author name and tag name
        and returns quotes if found.

        Parameters
        ----------
        author_name : str
            The quote author to search by.
        tag_name : str
            The quote tag to search by.

        Returns
        -------
        List[QuoteParser]
            The list of parsed quotes.
        """

        self.select_author(author_name)

        # wait up to 10 seconds until tag drop down value option appears
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN_VALUE_OPTION)
            )
        )

        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author `{author_name}` does not have any question tagged" +
                f" with `{tag_name}`."
            )

        self.search_button.click()

        return self.quotes


class InvalidTagForAuthorError(ValueError):
    """Class to be raised in the event of an invalid tag being provided."""
    pass
