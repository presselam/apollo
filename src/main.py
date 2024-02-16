import sys

from assistant import Assistant
from display import NotePad

COLOR_SYSTEM = 51
COLOR_USER = 118

def main(argv: list):

    apollo = Assistant()
    display = NotePad()

    display.print_header('Apollo')

    if len(argv) > 0:
        prompt = ' '.join(argv)
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
