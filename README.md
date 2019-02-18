# Raefinder
The **Mnemonic major system** associates one or more consonants to a numeral in order to ease the memorization.

Therefore, I have written a simple script that given a number, it retrieves all words (from a dictionary) that match this mnemotechnic criteria.

*Note: It's a little bit adapted to the Spanish language, feel free to modify it as you wish.*

## Dependencies

- Python3
- Unidecode

## Installation

Open the terminal, go to the folder of this package and type:
```
python3 setup.py install --user
```

Then, to use it you can simply write:

```
$ raefinder 1261
-----------------------------
--        RAEFINDER        --
-----------------------------
atenazado
ateneísta
danzado
denuesto
dinasta
dinastía
tenazada
tenista

-------------------------------
- Words matched: 8
- Words analyzed: 80,383
- Elapsed time: 0.24041s
- Regex used: "^[aeiou]*([dt])[aeiou]*([nñy])[aeiou]*([sz])[aeiou]*([dt])[aeiou]*$"
```

Available options:

```
(number) (dictionary: optional) Shows all matched words in the dictionary
-h        To list all available options
-m        To see mnemotechnics used
```

## More about this mnemotechnic
These associations are not arbitrary, in fact, they follow a very simple pattern of remembering (e.g: *V* is the Roman numeral for *5*, *p* is a *9* flipped 180º,...). Anyway, just as an example:

```
Number to remember = 3.1415927
Sentence: "Meteor tail pink"
-----
meteor (314, /m/-/t/-/r/)
tail (15, /t/-/l/)
pink (927, /p/-/ŋ/-/k/, and taking /ŋ/ to be 2)
```

**Detailed explanation:** [https://en.wikipedia.org/wiki/Mnemonic_major_system](https://en.wikipedia.org/wiki/Mnemonic_major_system)
