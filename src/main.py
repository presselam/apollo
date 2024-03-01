import sys
import argparse

from assistant import Assistant
from display import NotePad, Console


def main(argv: list):

    parser = argparse.ArgumentParser(description="apollo chat bot")
    parser.add_argument(
        "-c",
        "--codeonly",
        action="store_true",
        dest="code",
        help="only respond in code snippets",
    )
    parser.add_argument(
        "-v", "--vim", dest="vim", help="indicate what response vim wants"
    )
    parser.add_argument(
        "--canned", action="store_true", dest="canned", help="dont waste credits"
    )
    parser.add_argument("prompt", nargs="*", help="an initial prompt")
    opts = parser.parse_args(args=argv)

    system = "you are a helpful assistant"
    if opts.code:
        system = "only respond in code snippets without usage example"

    apollo = Assistant(system=system)
    display = NotePad()
    if opts.code:
        display = Console()

    display.print_header("Apollo")

    if len(opts.prompt) > 0:
        prompt = " ".join(opts.prompt)
        display.print_prompt(prompt)
    else:
        prompt = display.prompt_user()

    while prompt is not None:
        answer = apollo.chat(prompt, not opts.canned)
        display.print_response(answer)
        prompt = None
        if not opts.code:
            prompt = display.prompt_user()

    display.print_footer()


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv[1:]))
