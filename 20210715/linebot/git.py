from github import Github
from github import Github

g = Github(base_url="https://github.com/api/v3", login_or_token="XXX")
r = g.get_repo("ORG/REPO")
i = r.get_issues(state='open')
c = i.get_comments()

for issue in c:
    print(issue)
try:
    username="abel108714"
    password="aa461192"
    g = Github(username, password)

    # repo = g.get_user().get_repo(GITHUB_REPO)
    repo = g.get_user().get_repos()
    all_files = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

    with open('/tmp/file.txt', 'r') as file:
        content = file.read()

    # Upload to github
    git_prefix = 'folder1/'
    git_file = git_prefix + 'file.txt'
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
        print(git_file + ' UPDATED')
    else:
        repo.create_file(git_file, "committing files", content, branch="master")
        print(git_file + ' CREATED')
except Exception as e:
    print(e)