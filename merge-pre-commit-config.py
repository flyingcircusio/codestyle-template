import copy
import os.path
import sys

import yaml

LOCAL_FILE = ".pre-commit-config-local.yaml"


def merge(base, overlay):
    if not isinstance(overlay, dict):
        return overlay
    result = copy.deepcopy(base)
    for k, v in overlay.items():
        if k in result and isinstance(result[k], dict):
            result[k] = merge(result[k], v)
        elif k in result and isinstance(result[k], list):
            result[k] = result[k][:]
            result[k].extend(v)
        elif k in result and k == "exclude" and isinstance(result[k], str):
            # Regex merge for "exclude". There may be more, but we don't know
            # that , yet.
            result[k] += f"|{v}"
        else:
            result[k] = copy.deepcopy(v)
    return result


def main():
    with open(sys.argv[1], "r") as f:
        source = yaml.safe_load(f)

    if os.path.exists(LOCAL_FILE):
        with open(LOCAL_FILE, "r") as f:
            local = yaml.safe_load(f)
        merged = merge(source, local)

    else:
        merged = source

    with open(sys.argv[2], "w") as f:
        f.write(yaml.dump(merged))


if __name__ == "__main__":
    main()
