<!-- https://realpython.com/pipenv-guide/ -->

<!--  Install pipenv
pip install pipenv -->

<!-- Once you’ve done that, you can effectively forget about pip since Pipenv essentially acts as a replacement. It also introduces two new files, the Pipfile (which is meant to replace requirements.txt) and the Pipfile.lock (which enables deterministic builds).

Pipenv uses pip and virtualenv under the hood but simplifies their usage with a single command line interface. -->



<!-- https://www.pythontutorial.net/python-basics/install-pipenv-windows/ -->
<!-- https://pipenv-fork.readthedocs.io/en/latest/basics.html -->
<!-- Example Pipenv Workflow
Clone / create project repository:

$ cd myproject
Install from Pipfile, if there is one:

$ pipenv install
Or, add a package to your new project:

$ pipenv install <package>
This will create a Pipfile if one doesn’t exist. If one does exist, it will automatically be edited with the new package you provided.

Next, activate the Pipenv shell:

$ pipenv shell
$ python --version
This will spawn a new shell subprocess, which can be deactivated by using exit. -->

<!-- https://pipenv-fork.readthedocs.io/en/latest/basics.html -->
<!-- Example Pipenv Upgrade Workflow¶
Find out what’s changed upstream: $ pipenv update --outdated.
Upgrade packages, two options:
Want to upgrade everything? Just do $ pipenv update.
Want to upgrade packages one-at-a-time? $ pipenv update <pkg> for each outdated package.
☤ Importing from requirements.txt
If you only have a requirements.txt file available when running pipenv install, pipenv will automatically import the contents of this file and create a Pipfile for you.

You can also specify $ pipenv install -r path/to/requirements.txt to import a requirements file.

If your requirements file has version numbers pinned, you’ll likely want to edit the new Pipfile to remove those, and let pipenv keep track of pinning. If you want to keep the pinned versions in your Pipfile.lock for now, run pipenv lock --keep-outdated. Make sure to upgrade soon! -->


<!-- Fifth, use the following command to activate the new virtual environment:

pipenv shell -->