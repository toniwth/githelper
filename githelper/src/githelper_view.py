"""
********************************************
             githelper views
     echo data through the terminal
********************************************
"""
from src.githelper_classes import TextStyle
# ---------- functions -------------

# display a nice title for githelper-tool
def title_echo():
    text = TextStyle.STARS + "\n"\
           + TextStyle.BLUE \
           + TextStyle.BOLD \
           + "        githelper\n" \
           + TextStyle.RESET \
           + TextStyle.STARS + "\n"
    return text

# output the commit from head
def info_echo(commit_list):
    for commit in commit_list:
        commit