import sys
import argparse

from assistant import Assistant
from display import NotePad, colored

COLOR_SYSTEM = 51
COLOR_USER = 118


def main(argv: list):

    parser = argparse.ArgumentParser(description="apollo - the terminal assistant")
    parser.add_argument("-i", "--id", type=str, help="chat id for history")
    parser.add_argument("prompt", nargs="*", help="initial chat prompt")

    opts = parser.parse_args()

    apollo = Assistant()
    history = False
    if opts.id is not None:
        history = apollo.loadHistory(opts.id)

    chat_id = apollo.chat_id
    if history:
        chat_id = colored(4, chat_id)

    display = NotePad()
    display.print_header(f"Apollo ({chat_id})")

    if len(opts.prompt) > 0:
        prompt = " ".join(opts.prompt)
        display.print_prompt(prompt)
    else:
        prompt = display.prompt_user()

    while prompt is not None:
        answer = apollo.chat(prompt)
        display.print_response(answer)
        prompt = display.prompt_user()

    display.print_footer()


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv[1:]))
