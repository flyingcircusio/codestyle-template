This repository maintains our generally recommended code style / pre-commit validation settings.

# Usage

* Install `pre-commit` utilities on your system (`pkgs.pre-commit` on nixpkgs)

* Start own project or clone your existing project

* Ensure you have a clean working directory

* Run `codestyle-template/update` to apply the settings to your project, record the resulting changes as a single commit.

  * This may result in undesired changes, check for exclude rules that may be needed for your specific project.

  * Add exclude rules to a separate file `.pre-commit-config-local.yaml`, e.g.
    ```yaml
    exclude: ^myfile.txt$
    ```

    Note: the global exclude will be merged via rexep `|`. Other elements will be merged using dict and list merge. This file needs to be commited first.

* Enable black and isort on your editor

* Run manually using `pre-commit run` if you want to check your changes before committing.

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
