import argparse

def read_user_cli_args():
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste a disponibilidade de uma URL"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="insira um ou mais URLs",
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="URLs File",
        nargs=1,
        type=str,
        default=[],
        help="insira um path de um arquivo .csv",
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    status = f'O status da "{url}" é:'
    print(status, end=" ")
    if result:
        result_print = '"Online!" 👍'
        print(result_print)
    else:
        result_print = f'"Offline?" 👎 \n  Erro: "{error}"'
        print(result_print)

    log = status+" "+result_print
    return log