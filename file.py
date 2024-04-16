from git import Repo
new_repo = Repo.init(r'C:\Users\dell\OneDrive\Desktop\Automating_Github_Commands')

import git 
repo_url = "https://github.com/prarthanaagrawal/Youtube-Video-Transcriber"
local_path = r"C:\Users\dell\OneDrive\Desktop\Automating_Github_Commands"
repo = git.Repo.clone_from(repo_url, local_path) 
print(f'Repository Cloned at location: {local_path}')