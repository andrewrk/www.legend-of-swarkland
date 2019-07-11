#!/usr/bin/env python3

import os
import subprocess
import datetime

def main():
    this_directory = os.path.dirname(os.path.realpath(__file__))

    subprocess.check_call(["git", "submodule", "update", "--init"], cwd=this_directory)
    sha1 = subprocess.check_output(
        ["git", "rev-parse", "--short", "--verify", "HEAD"],
        cwd=os.path.join(this_directory, "deps/legend-of-swarkland"),
    ).decode("utf8").strip()

    context = dict(
        css=open(os.path.join(this_directory, "css.css")).read(),
        date=datetime.datetime.today().strftime("%Y-%m-%d %H:%M"),
        sha1=sha1,
    )

    template = open(os.path.join(this_directory, "index-template.html")).read()
    with open(os.path.join(this_directory, "public/index.html"), 'w') as f:
        f.write(template.format(**context))

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)

if __name__ == "__main__":
    main()
