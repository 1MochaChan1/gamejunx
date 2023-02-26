class Colors:
    default: str = '\33[0m'
    red: str = '\33[31m'
    green: str = '\33[32m'
    yellow: str = '\33[33m'
    blue: str = '\33[34m'
    error: str = '\033[91m'


class DebugPrint:
    def __init__(self, content, end:str=None, color: Colors = None,) -> None:
        if (color):
            print(f'{color}{content}{Colors.default}', end=end)
        else:
            print(f'{Colors.red}{content}{Colors.default}', end=end)
