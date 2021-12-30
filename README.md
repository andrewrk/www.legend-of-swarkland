Website for [legend-of-swarkland](https://github.com/thejoshwolfe/legend-of-swarkland).

https://wolfesoftware.com/legend-of-swarkland/

## Usage

```
./gen.py
```

And then the `public/` directory contains the site's static assests.

## Build and Publish Command for NixOS

```
(ZIG_PATH=~/tmp/zig-linux-x86_64-0.9.0/; nix-shell --pure -p python3 -p git -p clang -p cacert -p s3cmd --command "./gen.py --zig=$ZIG_PATH/zig && s3cmd sync -P --no-preserve --add-header='Cache-Control: max-age=0, must-revalidate' public/ s3://wolfesoftware.com/legend-of-swarkland/")
```
