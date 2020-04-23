"""
********************************************
             githelper classes
********************************************
"""

# Class with constants to style output for terminal due to ans
# ansi escape code
class TextStyle:
    def __init__(self):
        pass
    # Style elements
    LINE = "==========================="
    STARS = "***************************"
    # Text decoration
    BOLD = '\u001b[1m'
    UNDERLINE = '\u001b[4m'
    REVERSED = '\u001b[7m'
    # Font colors
    BLACK = '\u001b[30m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    BLUE = '\u001b[34m'
    MAGENTA = '\u001b[35m'
    CYAN = '\u001b[36m'
    WHITE = '\u001b[37m'
    RESET = '\u001b[0m'
    # Background colors
    BG_BlACK = '\u001b[40m'
    BG_RED = '\u001b[41m'
    BG_GREEN = '\u001b[42m'
    BG_YELLOW = '\u001b[43m'
    BG_BLUE = '\u001b[44m'
    BG_MAGENTA = '\u001b[45m'
    BG_CYAN = '\u001b[46m'
    BG_WHITE = '\u001b[47m'
