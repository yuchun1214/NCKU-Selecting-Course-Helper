# NCKU Selecting Course Helper

成大選課小幫手

## Execute Environment

python version : 3.6.5

I recommand you creat a virtualenv

```bash=
$ virtualenv --python=python3 venv
```

```bash=
$ source venv/bin/activate
```

### Install requirements

```bash=
$ pip install -r requirements.txt
```

## How to use

You need to modify `myCourse.json` to write  the course you already have.

### Execute

```bash=
$ python user.py <url>
```

**Default url is A9 general education.**
