# to start working on the project
- clone this repository using git
```bash
git clone <repository-link>
```

- start a new branch using
```bash
git checkout -b <branch-name>
```

- initialize the environment
if using gitbash
```bash
py -m venv venv
. venv/Scripts/activate
```

if using cmd
```bash
py -m venv venv
venv/Scripts/activate.bat
```

you should see (venv) at the start of the command line

- install the dependencies
```bash
pip install -r requirements.txt
```

- always commit to <your-branch> and start a pull request