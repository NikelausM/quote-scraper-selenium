from typing import List

from locators.quote_locators import QuoteLocators
from selenium.webdriver.remote.webelement import WebElement


class QuoteParser:
    """
    Given one of the specific quote divs, found out the data about the quote
    (quote content, author, tags).
    """

    def __init__(self, parent: WebElement):
        """
        Parameters
        ----------
        parent : selenium.webdriver.remote.webelement.WebElement
            The html content to be parsed.
        """

        self.parent = parent

    def __repr__(self) -> str:
        """Returns the string representation of a QuoteParser object.

        Returns
        ------
        str
            A string representing the QuoteParser object.
        """

        repr_str = f"<Quote {self.content}, by {self.author}>"
        return repr_str

    @property
    def author(self) -> str:
        """Returns the string representation of the author.

        Returns
        ------
        str
            The string representation of the author.
        """

        locator = QuoteLocators.AUTHOR
        author_str = self.parent.find_element_by_css_selector(locator).text
        return author_str

    @property
    def content(self) -> str:
        """Returns the string representation of the content.

        Returns
        ------
        str
            The string representation of the content.
        """

        locator = QuoteLocators.CONTENT
        content_str = self.parent.find_element_by_css_selector(locator).text
        return content_str

    @property
    def tags(self) -> List[str]:
        """Returns the string representation of the tags.

        Returns
        ------
        List[str]
            The string representation of the tags.
        """

        locator = QuoteLocators.TAGS
        tags_str = [e.string for e in
                    self.parent.find_elements_by_css_selector(locator)]
        return tags_str
