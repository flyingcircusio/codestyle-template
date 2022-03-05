This repository maintains our generally recommended code style / pre-commit validation settings.

# Usage

* Install `pre-commit` utilities on your system (`pkgs.pre-commit` on nixpkgs)

* Start own project or clone your existing project

* Ensure you have a clean working directory

* Run `codestyle-template/update` to apply the settings to your project, record the resulting changes as a single commit.

* Enable black and isort on your editor

* Enable Github action or Gitlab pipeline to verify changes automatically.

Example:

```console 
$ git clone myproject
$ cd myproject
$ ../codestyle-template/update
$ git status
# review output
$ git commit -m "Update coding style."
```
