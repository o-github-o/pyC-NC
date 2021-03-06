from nltk.tag.simplify import simplify_wsj_tag
from textblob import TextBlob


def pos_tag(text, simple=False):
    """ Tokenizes a given text and determines the pos-tags. Lowercases
        the text.

     Params:
        text: string to be tokenized
        simple: boolean indicating weather to simplify the pos tags

    Returns:
        list of tuples of form (token, pos-tag)
    """

    blob = TextBlob(text.lower())
    pos = blob.tags

    # simplify tags if requested
    if simple:
        simple_pos = []
        for word, tag in pos:
            new_tag = simplify_wsj_tag(tag)
            # simplification removes some tags
            # not allowed to use empty tag so use initial one
            if not new_tag:
                new_tag = tag
            simple_pos.append((word, new_tag))
        pos = simple_pos

    return pos
