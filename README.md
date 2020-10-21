# DepopFollowers

This is a tiny Python script to retrieve the follower count of a profile as shown on the website.

In it's current form it will output the following:

``` bash
$ python main.py
emrata has 63K followers!
```

If you want it to output just the follower count to use in other programs etc. then change the last line to:

``` python
print(followers)
```

This will then output:

``` bash
$ python main.py
63K
```

## Usage

Update the username variable on line 4 to the desired 

## Requirements

The only dependencies (apart from Python) are the `requests` and `bs4` modules.

As this is pretty basic you should be able to get away with any version of each module (`pip install requests bs4`), but I have included a requrements.txt in case you want exact versions.

Install with `pip install -r requirements.txt`.
