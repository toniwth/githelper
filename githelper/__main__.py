"""
**************************************
        Entrypoint of githelper
**************************************
"""
from src import githelper_logic
from src import githelper_view
def main():
    # TODO: Change directory to current directory where we are
    # repo = githelper_logic.get_git_info('..', 10)
    print(githelper_view.title_echo())


if __name__ ==  '__main__':
    main()
