from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    """
    A class that retreives a web page from a URL, and parses it for quotes.
    """

    def __init__(self, browser):
        """
        Parameters
        ----------
        soup : bs4.BeautifulSoup
            The url of the web page.
        """
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        """Returns the web page's quotes.

        Returns
        -------
        list
            A list of QuoteParser representing the web page's quotes.
        """

        quote_tags = self.browser.find_elements_by_css_selector(
            QuotesPageLocators.QUOTE)
        return [QuoteParser(e) for e in quote_tags]

    @property
    def author_dropdown(self) -> Select:
        """Selects and returns the author dropdown menu."""

        element = self.browser.find_element_by_css_selector(
            QuotesPageLocators.AUTHOR_DROPDOWN)
        return Select(element)  # puts element in Select wrapper (dropdown)

    @property
    def tags_dropdown(self) -> Select:
        """Selects and returns the tag dropdown menu."""

        element = self.browser.find_element_by_css_selector(
            QuotesPageLocators.TAG_DROPDOWN)
        return Select(element)  # puts element in Select wrapper (dropdown)

    @property
    def search_button(self):
        """Returns the search button."""

        return self.browser.find_element_by_css_selector(
            QuotesPageLocators.SEARCH_BUTTON)

    def select_author(self, author_name: str):
        """Select author name in dropdown.
        """

        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        """Get available tags from dropdown."""
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_tag(self, tag_name: str):
        """Select tag in dropdown"""
        self.tags_dropdown.select_by_visible_text(tag_name)

    def search_for_quotes(self, author_name: str,
                          tag_name: str) -> List[QuoteParser]:
        self.select_author(author_name)
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
    pass
