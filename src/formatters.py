from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name

def splitter(data: list, length: int) -> list:
    retval = []
    for text in data:
        for ln in text.split("\n"):
            remainder = ln
            while remainder is not None:
                parts = _split_lines(remainder, length)
                retval.append(parts[0])
                remainder = parts[1]

    return retval

def highlighter(data: list) -> list:
    retval = []

    language = None
    buffer = None
    for text in data:
        if language is None:
            if "```" in text:
                language = text[3:]
                buffer = []
            retval.append(text)
        else:
            if "```" == text:
                language = None
                retval.append(text)
            else:
                lexer  = get_lexer_by_name(language)
                formatter = get_formatter_by_name('256')
                hl = highlight(text, lexer, formatter)
                retval.append(hl.rstrip("\n"))


    return retval


def _split_lines(data: str, length: int) -> list:
    if len(data) < length:
        return (data, None)

    (pre, post) = data[:length].rsplit(' ', 1)

    if len(pre) == 0:
        return (data, None)

    sz = len(pre)
    post = data[sz:].lstrip()

    return (pre, post)
