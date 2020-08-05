class QuotesPageLocators:
    """A class that contains the quotes page CSS locators.

    Parameters
    ----------
    QUOTE : str
        The CSS locator that selects the div of class quote.
    AUTHOR_DROPDOWN : str
        The CSS locator that selects the author drop down menu.
    TAG_DROPDOWN : str
        The CSS locator that selects the tag drop down menu.
    TAG_DROPDOWN_VALUE_OPTION : str
        The CSS locator that selects a tag option that has a value.
    SEARCH_BUTTON : str
        The CSS locator that selects the search button.
    """

    QUOTE = "div.quote"
    AUTHOR_DROPDOWN = "select#author"
    TAG_DROPDOWN = "select#tag"
    # no match if option doesn't have a value
    TAG_DROPDOWN_VALUE_OPTION = "select#tag option[value]"
    SEARCH_BUTTON = "input[name=\"submit_button\"]"
