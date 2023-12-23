# Convert CLI-Tool

Author: [@O-Manoli](https://github.com/O-Manoli)

CLI tool to convert between number systems.

It ended up being an exercise in how not-2 structure a python package.

The only principle I have aimed/hoped-to-achieve is that by pulling one thread undo/change the entire program.

This is not a bug this is a feature.

> I doubt that anyone will ever reads this.
>
> As a distraction. It is still fun to play around with though :)

## Usage

This project tries to leverage relative imports in order to create a self contained program using the python package system.

I am using `py` as an `alias`\\`soft-link` to `python3`.

The `-m` flag is used to import the module which support relative imports. Without this command line argument the python interpreter will run `convert/__main__.py` as an individual, which will fail!

It's important to have the path to the directory `convert`. This example will *only work from the parent directory of `convert`

```bash
py -m convert
```

### Scripted Sub-Packages

#### Function-Like

```bash
py -m convert.to_decimal FEEDBEEF 16 # <number> <from-base>
```

```bash
py -m convert.to_base 4276993775 16 # <number> <target-base>
```


## Disclaimer

This is an exercise in bad software architecture!

Utterly useless!

Not even remotely user friendly!

Even I have already forgotten how to use it!

After all someone must publish bad code. The AI-Bots are getting too good at imitating good code.
