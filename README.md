# XML Editor Tool

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Build Status](https://github.com/AndrewDarnall/XML-Editing-Tool/actions/workflows/lint.yml/badge.svg)


---

This is a simple tool for the domain specific editing of an XML document.
<br>
<br>
The tool takes as input a directory with `.xml` files, and iteratively edits each file
searching for specific nodes within the tree representation of the tags and replaces
and add to the hard-coded target nodes.
<br>
<br>
The tool is meant to automate some time-consuming tasks which could be error-prone
and can be (and should be) handled by a machine.

---

## Requirements

| Software  | Version |
|-----------|---------|
| Python    |`3.10.14`|
| Pip       | `23.3.1`|
| pre-commit| `2.10.1`|

You can install `pre-commit` to apply the git hooks defined in the `.pre-commit-config.yaml` by either installing it via:

1) `pip` via the command

```bash
python -m pip install pre-commit==2.10.1
```

2) package manager such as `apt` for `Debian-based` distributions:

```bash
apt-get install pre-commit
```

---

## Usage

1) Clone the repository into a directory of choice

```bash
git clone https://github.com/AndrewDarnall/XML-Editing-Tool.git
```

2) Change into the repo's `target-dir` directory

```bash
cd XML-Editing-Tool/target-dir
```

3) Move all the target `.xml` files into the `target-dir` directory


4) Run the script

```bash
python ../main.py .
```

---
