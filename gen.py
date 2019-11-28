#!/usr/bin/env python3

import os
import subprocess
import datetime
import time
import shutil

def main():
    this_directory = os.path.dirname(os.path.realpath(__file__))
    legend_of_swarkland_dir = os.path.join(this_directory, "deps/legend-of-swarkland")
    public_dir = os.path.join(this_directory, "public")

    subprocess.check_call(["git", "submodule", "update", "--init", "--recursive"], cwd=this_directory)

    sha1 = subprocess.check_output(
        ["git", "rev-parse", "--short", "--verify", "HEAD"],
        cwd=legend_of_swarkland_dir,
    ).decode("utf8").strip()

    version = subprocess.check_output(
        ["git", "describe", "--tags"],
        cwd=legend_of_swarkland_dir,
    ).decode("utf8").strip()

    build_cmd = ["zig", "build", "-Dtarget=x86_64-windows-gnu", "-Drelease-safe"]
    print("building for windows...")
    subprocess.check_call(build_cmd, cwd=legend_of_swarkland_dir)
    print("done")

    exe_path = os.path.join(public_dir, "legend-of-swarkland_{version}.exe".format(version=version))
    shutil.copy(
        os.path.join(legend_of_swarkland_dir, "zig-cache/bin/legend-of-swarkland.exe"),
        exe_path,
    )
    exe_size = sizeof_fmt(os.stat(exe_path).st_size)

    context = dict(
        css=open(os.path.join(this_directory, "css.css")).read(),
        date=datetime.datetime.now().isoformat(sep=" ", timespec="minutes"),
        date_unix=int(time.time() / 60) * 60,
        sha1=sha1,
        version=version,
        exe_size=exe_size,
    )

    template = open(os.path.join(this_directory, "index-template.html")).read()
    with open(os.path.join(this_directory, "public/index.html"), 'w') as f:
        f.write(template.format(**context))

def sizeof_fmt(num, suffix="B"):
    for prefix in ["","Ki","Mi","Gi","Ti","Pi","Ei","Zi"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, prefix, suffix)
        num /= 1024.0
    prefix = "Yi"
    return "%.1f%s%s" % (num, prefix, suffix)

if __name__ == "__main__":
    main()
