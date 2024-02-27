import sys
import argparse

from assistant import Assistant
from display import NotePad

def main(argv: list):

    parser = argparse.ArgumentParser(description = 'apollo chat bot')
    parser.add_argument('-c', '--code', action='store_true', dest='code', help='only respond in code snippets')
    parser.add_argument('prompt', nargs='*', help='an initial prompt')
    opts = parser.parse_args(args=argv)

    system = 'you are a helpful assistant'
    if opts.code:
        system = 'only respond in code snippets'

    apollo = Assistant(system=system)
    display = NotePad()

    display.print_header('Apollo')

    if len(opts.prompt) > 0:
        prompt = ' '.join(opts.prompt)
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
