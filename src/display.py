import os

from formatters import splitter, highlighter

CHATWIDTH = os.get_terminal_size().columns - 8
COLOR_GUTTER = 238
COLOR_SYSTEM = 51
COLOR_USER = 48
COLOR_ASSISTANT = 209
COLOR_SYNTAX = 255


class Console:
    def print_header(self, system: str):
        pass

    def print_footer(self):
        pass

    def print_prompt(self, data):
        pass

    def print_response(self, data):
        lines = splitter([data])
        for ln in lines:
            if "```" not in ln:
                print(ln)


class NotePad:
    def __init__(self):
        self.line_idx = 0
        self.quote = False

    def print_header(self, system: str):
        self.__horizontal_line("\u2500", "┬")
        self.__horizontal_line(" ", "│", system, COLOR_SYSTEM)
        self.__horizontal_line("\u2500", "┼")

    def print_footer(self):
        self.__horizontal_line("─", "┴")

    def print_prompt(self, data):
        self.__printer(COLOR_USER, data)

    def print_response(self, data):
        self.__printer(COLOR_ASSISTANT, data)

    def prompt_user(self) -> str:
        self.line_idx += 1
        gutter = str(self.line_idx).rjust(4) + " " * 3
        gutter = colored(COLOR_GUTTER, f"{gutter}│ ")
        response = input(f"{gutter}\u001b[38;5;{COLOR_USER}m")
        print("\u001b[0m\r", end="")
        return response or None

    def __printer(self, color: int, data: str):
        lines = splitter([data], CHATWIDTH)
        lines = highlighter(lines)
        for ln in lines:
            self.__horizontal_line(None, "│", ln, color)

    def __horizontal_line(
        self,
        leader: str,
        separator: str,
        data: str = None,
        data_color: int = COLOR_GUTTER,
    ):
        separator = colored(COLOR_GUTTER, separator)

        if leader is None:
            self.line_idx += 1
            gutter = str(self.line_idx).rjust(4) + " " * 3
        else:
            gutter = leader * 7
        gutter = colored(COLOR_GUTTER, gutter)

        if data is None:
            data = colored(COLOR_GUTTER, leader * CHATWIDTH)
        else:
            padding = "\033[G\033[" + str(CHATWIDTH + 5) + "C"
            if "```" in data:
                if self.quote:
                    data = "\u2514" + "\u2500" * (CHATWIDTH - 4) + "\u2518"
                else:
                    data = "\u250C" + "\u2500" * (CHATWIDTH - 4) + "\u2510"
                self.quote = not self.quote
            else:
                if self.quote:
                    #                     pad = ' ' * (padding - printlen(data))
                    pad = padding
                    data = colored(COLOR_SYNTAX, data)
                    data = f"\u2502{data}{pad}\u2502"
                else:
                    data = colored(data_color, data)
                    data = f" {data}"

        print(f"{gutter}{separator}{data}")


def split_lines(data: str, length: int) -> list:
    if len(data) < length:
        return (data, None)

    (pre, post) = data[:length].rsplit(" ", 1)

    if len(pre) == 0:
        return (data, None)

    sz = len(pre)
    post = data[sz:].lstrip()

    return (pre, post)


def colored(code: int, data: str) -> str:
    return "\u001b[38;5;" + str(code) + "m" + data + "\u001b[0m"
