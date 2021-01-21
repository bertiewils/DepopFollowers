# DepopFollowers

This is a tiny Python script to retrieve the follower count of a profile **as shown on the website**.


## Usage

In it's current form it will output the following:

```sh
$ ./main.py emrata
emrata has 63K followers!
```

If you want it to output just the follower count you can run it with the `-s` or `--short` flag;

```sh
$ ./main.py -s emrata
63K
```

If in doubt, check the `--help` output:

```sh
$ ./main.py --help
usage: main.py [-h] [-s] username

Retrieve follower count for a user on Depop

positional arguments:
  username     username of the user

optional arguments:
  -h, --help   show this help message and exit
  -s, --short  print just the follower count
```

## Requirements

The only dependencies (apart from Python) are the `requests` and `bs4` modules.

As this is pretty basic you should be able to get away with any version of each module (`pip install requests bs4`), but I have included a requrements.txt in case you want exact versions.

Install with `pip install -r requirements.txt`.
