def ellipsize(text, length=80):
    if text and len(text) > length:
        return text[:length] + '...'
    else:
        return text
