def char_limit(s: str, n_limit: int, name: str):
    """ limits string characters amount

    :param s: string to limit
    :type s: str
    :param n_limit: number of chars to limit
    :type n_limit: int
    :param name: name of string
    :type name: str

    :rtype: str
    """
    if len(s) > n_limit:
        return f"{name} is too large (it has more than {n_limit} characters). "
    return ""
