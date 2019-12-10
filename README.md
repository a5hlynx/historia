# historia

Simple browsing history parser(s). Currently, only the one for safari is ready. 

## safari.py

Safari's browsing history parser, which reads and interprets History.db and generates the list of browsing history records in csv format.

One record consists of the following items;
* URL
* title
* visit time
* visit count
* visit from


### Usage

```
python3 safari.py -i <input file> -o <output file>
```

### Example

```
python3 safari.py -i History.db -o history.csv
```

### Requirements

The script is supposed to be run on python 3.
