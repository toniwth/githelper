from git import Repo
from time import asctime

# shown all information for a repository
# TODO check for problem with get bare repo or normal repo
def get_git_info(working_dir, commit_length):
    repo = Repo(working_dir)
    head_commit_list = list(repo.iter_commits('HEAD', max_count=commit_length))
    return head_commit_list[0].tree
