# My new project

Hey, this is a template for Python projects, including a dev container for VSCode

# Features
Some features and plugins of this development environment:
- Uses black and flake8 for code formatting
- Uses isort for sorting python dependencies
- Some basic DS tools included in the requirements.txt file (pandas)
- Auto-formatting on save (cmd+s)
- PyLance for static code analysis 
- Automatic generation of Python docstrings following the Google format
- Git Blame
- Plugins for markdown files edition
  
# Structure

As Python does not enforce any project structure, use this just as a suggestion. Feel free to change it as it better suits your needs.

```
./
├── .devcontainer
├── myPythonModule
│   ├── main.py
│   ├── myPythonModule
│   ├── pytest.ini
│   ├── tests
│   ├── docs
├── requirements.txt
├── Dockerfile.dev
└── README.md
```
# Usage
To develop using the dev container:

1. You need to install [Docker](https://docs.docker.com/get-docker/) and [VSCode](https://code.visualstudio.com/download) in your computer.
2. Open VSCode and install the Dev Container extension (use the extensions tab in the left). 
3. Then simply open the project folder in VSCode. A pop-up window should ask you whether you want to open the project in the dev container. Hit yes. It will build the container for you - it may take some minutes. Then VSCode will open the project in the dev container and you are done. You will see in the bottom-left side of the screen a green bar "Dev Container: nameOfYourProject"
   > If the pop-up window doesn't show up: Open the command pallet (Shift + Command + P), type "Remote-Containers", click "Remote-Containers: Rebuild Container" in the drop down list. It will start building the container. You are done.

## SSH keys for git
Dev containers in VSCode can retrieve SSH keys from the host automatically. The SSH keys have to be added in the host machine to the SSH agent, e.g. running in a terminal:
```
ssh-add $HOME/.ssh/github_rsa
```
See this the VSCode documentation on sharing ssh keys [here](https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials).

# TO DOs
1. Add git hooks for formatting on commit
2. More detailed instructions