"""
********************************************
             githelper classes
********************************************
"""

# Class with constants to style output for terminal due to ans
# ansi escape code
class TextStyle(self):
    # Text decoration
    self.BOLD = '\001b[1m'
    self.UNDERLINE = '\u001b[4m0'
    self.REVERSED = '\u001b[7m'
    # Font colors
    self.BLACK = '\u001b[30m'
    self.RED = '\u001b[31m'
    self.GREEN = '\u001b[32m'
    self.YELLOW = '\u001b[33m'
    self.BLUE = '\u001b[34m'
    self.MAGENTA = '\u001b[35m'
    self.CYAN = '\u001b[36m'
    self.WHITE = '\u001b[37m'
    self.RESET = '\u001b[0m'
    # Background colors
    self.BG_BlACK = '\u001b[40m'
    self.BG_RED = '\u001b[41m'
    self.BG_GREEN = '\u001b[42m'
