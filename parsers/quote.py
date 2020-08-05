from locators.quote_locators import QuoteLocators


class QuoteParser:
    """
    Given one of the specific quote divs, found out the data about the quote
    (quote content, author, tags).
    """

    def __init__(self, parent):
        """
        Parameters
        ----------
        parent : bytes
            The html content to be parsed.
        """
        self.parent = parent

    def __repr__(self):
        """Returns the string representation of a QuoteParser object.

        Returns
        ------
        str
            A string representing the QuoteParser object.
        """
        return f"<Quote {self.content}, by {self.author}>"

    @property
    def author(self):
        """Returns the string representation of the author.

        Returns
        ------
        str
            The string representation of the author.
        """
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def content(self):
        """Returns the string representation of the content.

        Returns
        ------
        str
            The string representation of the content.
        """
        locator = QuoteLocators.CONTENT
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tags(self):
        """Returns the string representation of the tags.

        Returns
        ------
        str
            The string representation of the tags.
        """
        locator = QuoteLocators.TAGS
        return [e.string for e in
                self.parent.find_elements_by_css_selector(locator)]
