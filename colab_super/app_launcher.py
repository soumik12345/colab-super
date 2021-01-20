import subprocess
from pyngrok import ngrok
from .git_manager import GitManager


class AppLauncher:

    def __init__(self, user_name: str, repository_name: str, clone_path: str = './'):
        self.git_manager = GitManager(user=user_name, repo=repository_name)
        self.git_manager.clone(clone_path=clone_path)
        self.public_url = None

    def launch_app(self, port: int = 80):
        self.public_url = ngrok.connect(port=str(port))
        print(self.public_url)
        subprocess.run([
            'streamlit', 'run', '--server.port', str(port), 'app.py', '>/dev/null'
        ])
