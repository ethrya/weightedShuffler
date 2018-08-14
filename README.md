# weightedShuffler
Weighted Shuffler for Spotify

Python code which utilises the spotipy module to add a random selection to songs to the queue based on user defined weightings.

## Prerequisites
The following prerequisites can all be imported using pip.
1. Python 3.4 or higher
2. spotipy
3. pandas 
4. numpy
5. json

## Installation and setup
1. Clone the repository

```
git clone https://github.com/ethrya/weightedShuffler.git
```
2. Create an app and get a client ID and secret from 

3. Complete the config.py file.
## Usage
1. Create the spreadsheet of songs using
```python
python sheetMaker.py
```
2. Update the weightings for each song by changing the relevant value in the 'weightnings.xlsx' spreadsheet. Weightings reflect the relative 'rate' at which songs are chosen.

3. Play songs with weightings by running

```python
python shuffler.py
```