__author__ = 'Alena_Laptseva'
import cmd
import git
# from git import Repo
from github import Github
import github

g = Github("pavelpantseleyeu", "")
g.get_api_status()


dir = git.cmd.Git("C:\Users\Pavel_Pantseleyeu\PycharmProjects\QAAutomation")
dir.pull()

for repo in g.get_user().get_repos():
    print repo.name
    repo.edit(has_wiki=False)

repo = Repo('https://github.com/ClarabridgeInc