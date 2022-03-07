This repository maintains our generally recommended code style / pre-commit validation settings.

# Usage

* Install `pre-commit` utilities on your system (`pkgs.pre-commit` on nixpkgs)

* Start own project or clone your existing project

* Ensure you have a clean working directory

* Run `codestyle-template/update` to apply the settings to your project, record the resulting changes as a single commit.

  * This may result in undesired changes, check for exclude rules that may be needed for your specific project.

* Enable black and isort on your editor

* CI/CD

  * A Github action is installed automatically. 

  * Gitlab pipelines need to be added manually.

Example:

```console 
$ git clone myproject
$ cd myproject
$ ../codestyle-template/update
$ git status
# review output
$ git commit -m "Update coding style."
```
