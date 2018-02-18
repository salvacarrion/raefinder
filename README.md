# Raefinder
The **Mnemonic major system** associates one or more consonants to a numeral in other to ease the memorization.

Therefore, I have written a simple script that given a number, it retrieves all words (from a dictionary) that match this mnemotecnic criteria.

*Note: It's a little bit adapted to the Spanish language, feel free to modify it as you wish.*

## Dependencies

- Python3

## How to use it

Just type on the terminal and get the results:

```
$ python3 raefinder.py 123

==>
adenoma
adinamia
dinamia
dinamo
tonema

-------------------------------
Total results: 5
```

Available options:

```
(number)	To retrive matching words from DRAE
-h		To list all available options
-m		To see mnemotecnics used
```

## More about this mnemotecnic
These associations are not arbitrary, in fact, they follow a very simple pattern of remembering (e.g: *V* is the Roman numeral for *5*, *b* is a *9* turned 180º,...). Anyway, just as an example:

```
Number to remember = 3.1415927
Sentence: "Meteor tail pink"
-----
meteor (314, /m/-/t/-/r/)
tail (15, /t/-/l/)
pink (927, /p/-/ŋ/-/k/, and taking /ŋ/ to be 2)
```

**Detail explanation:** [https://en.wikipedia.org/wiki/Mnemonic_major_system](https://en.wikipedia.org/wiki/Mnemonic_major_system)
