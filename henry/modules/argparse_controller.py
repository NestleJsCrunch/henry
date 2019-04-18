import argparse


def limit_type(limit):
    """Check that limit argument is greater than 0

    Arguments:
        limit {int} -- The limit passed to argparse through the --limit flag

    Raises:
        argparse.ArgumentTypeError -- Raised if limit is not greater than 0

    Returns:
        int -- The limit passed
    """

    l = int(limit)
    if l <= 0:
        raise argparse.ArgumentTypeError('Must be greater than 0.')
    return l
