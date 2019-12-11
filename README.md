# historia

Simple browsing history parsers. Currently, the ones for safari and opera are ready. 

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

## opera.py

Opera's browsing history parser, which reads and interprets History and generates the list of browsing history records in csv format.

One record consists of the following items;
* URL
* title
* visit time
* visit count
* visit from


### Usage

```
python3 opera.py -i <input file> -o <output file>
```

### Example

```
python3 opera.py -i History -o history.csv
```


## Requirements

The scripts are supposed to be run on python 3.
