import os
import urllib
import subprocess
from getpass import getpass


class GitManager:

    def __init__(self, user: str, repo: str):
        self.user = user
        self.repo = repo

    def clone(self, clone_path: str = ''):
        password = getpass('Password: ')
        password = urllib.parse.quote(password)
        command = [
            'git', 'clone',
            'https://{0}:{1}@github.com/{0}/{2}.git'.format(
                self.user, password, self.repo
            )
        ]
        if clone_path != '':
            command += [clone_path]
        subprocess.run(command)
        repo_path = '/content/{}'.format(self.repo)\
            if clone_path == '' else os.path.join('/content/', clone_path)
        assert os.path.exists(repo_path), 'Unable to clone repository'
        os.chdir(repo_path)
