import robinhood_api.helper as helper
import robinhood_api.urls as urls



def load_account_profile(login, info=None):
    """Gets the information associated with the accounts profile,including day
    trading information and cash being held by Robinhood.
    :param info: The name of the key whose value is to be returned from the function.
    :type info: Optional[str]
    :returns: The function returns a dictionary of key/value pairs. \
    If a string is passed in to the info parameter, then the function will return \
    a string corresponding to the value of the key whose name matches the info parameter.
    """
    url = urls.account_profile()
    data = helper.request_get(login, url, 'indexzero')
    return (helper.filter(data, info))


def load_basic_profile(login, info=None):
    """Gets the information associated with the personal profile,
    such as phone number, city, marital status, and date of birth.
    :param info: The name of the key whose value is to be returned from the function.
    :type info: Optional[str]
    :returns: The function returns a dictionary of key/value pairs. If a string \
    is passed in to the info parameter, then the function will return a string \
    corresponding to the value of the key whose name matches the info parameter.
    """
    url = urls.basic_profile()
    data = helper.request_get(login, url)
    return (helper.filter(data, info))


def load_investment_profile(login, info=None):
    """Gets the information associated with the investment profile.
    These are the answers to the questionaire you filled out when you made your profile.
    :param info: The name of the key whose value is to be returned from the function.
    :type info: Optional[str]
    :returns: The function returns a dictionary of key/value pairs. \
    If a string is passed in to the info parameter, then the function will return \
    a string corresponding to the value of the key whose name matches the info parameter.
    """
    url = urls.investment_profile()
    data = helper.request_get(login, url)
    return (helper.filter(data, info))


def load_portfolio_profile(login, info=None):
    """Gets the information associated with the portfolios profile,
    such as withdrawable amount, market value of account, and excess margin.
    :param info: The name of the key whose value is to be returned from the function.
    :type info: Optional[str]
    :returns: The function returns a dictionary of key/value pairs. \
    If a string is passed in to the info parameter, then the function will return \
    a string corresponding to the value of the key whose name matches the info parameter.
    """
    url = urls.portfolio_profile()
    data = helper.request_get(login, url, 'indexzero')
    return (helper.filter(data, info))


def load_security_profile(login, info=None):
    """Gets the information associated with the security profile.
    :param info: The name of the key whose value is to be returned from the function.
    :type info: Optional[str]
    :returns: The function returns a dictionary of key/value pairs. \
    If a string is passed in to the info parameter, then the function will return \
    a string corresponding to the value of the key whose name matches the info parameter.
    """
    url = urls.security_profile()
    data = helper.request_get(login, url)
    return (helper.filter(data, info))


def load_user_profile(login, info=None):
    """Gets the information associated with the user profile,
    such as username, email, and links to the urls for other profiles.
    :param info: The name of the key whose value is to be returned from the function.
    :type info: Optional[str]
    :returns: The function returns a dictionary of key/value pairs. \
    If a string is passed in to the info parameter, then the function will return \
    a string corresponding to the value of the key whose name matches the info parameter.
    """
    url = urls.user_profile()
    data = helper.request_get(login, url)
    return (helper.filter(data, info))
