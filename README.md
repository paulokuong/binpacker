[![Build Status](https://travis-ci.org/paulokuong/binpacker.svg?branch=master)](https://travis-ci.org/paulokuong/binpacker)
binpacker
======

Generic Bin Packing Problem Solver.

> Given a set of items with weight information and capacity of a bin,
> Binpacker determines which items can fit in the bin with that capacity
> and continues to pack all items in new bins in a way that it will utilize
> the space of each bin. In the other word, Binpacker can be used to
> determine what is the minimum number of bins we can use to pack all items
> with different weights.

Requirements
------------

* Python 3.4 (tested)

Goal
----

The ultimate goal of this library is to provide a generic interface
for solving the Bin Packing problem for variety of applications.

Code sample
-----------

Lets say, given the capacity (11) of a bin and a list of packages
with different weights, we would like to load and unload the
packages in a way that it utilizes the space of each bin.

```python
import time
from binpacker.binpacker import Binpacker
from binpacker.binpacker import Item
packer = Binpacker(11)
packer.items = [
    Item('A',4), Item('B',1), Item('C',2),
    Item('D',6), Item('E',9), Item('F',3),
    Item('G',7), Item('H',2), Item('I',5)
]
j=0
while True:
  packer.pack_items()
  for i, x in enumerate(packer.bins):
      print('Bin ({}%) {}: {}'.format(x.utilization, i,[i.name for i in x.get_items()]))

  print('----------------------------------')
  packer._items.append(Item('Z{}'.format(i),2))
  j += 1
  time.sleep(3)

output:
    Bin (100.0%) 0: ['H', 'C', 'F', 'A']
    Bin (100.0%) 1: ['I', 'D']
    Bin (90.91%) 2: ['B', 'E']
    Bin (63.64%) 3: ['G']
    ----------------------------------
    Bin (100.0%) 0: ['H', 'C', 'F', 'A']
    Bin (100.0%) 1: ['I', 'D']
    Bin (90.91%) 2: ['B', 'E']
    Bin (81.82%) 3: ['Z0', 'G']
    ----------------------------------
    Bin (100.0%) 0: ['H', 'C', 'F', 'A']
    Bin (100.0%) 1: ['I', 'D']
    Bin (90.91%) 2: ['B', 'E']
    Bin (100.0%) 3: ['Z0', 'G', 'Z1']
    ----------------------------------
    Bin (100.0%) 0: ['H', 'C', 'F', 'A']
    Bin (100.0%) 1: ['I', 'D']
    Bin (90.91%) 2: ['B', 'E']
    Bin (100.0%) 3: ['Z0', 'G', 'Z1']
    Bin (18.18%) 4: ['Z2']
    ----------------------------------
    Bin (100.0%) 0: ['H', 'C', 'F', 'A']
    Bin (100.0%) 1: ['I', 'D']
    Bin (90.91%) 2: ['B', 'E']
    Bin (100.0%) 3: ['Z0', 'G', 'Z1']
    Bin (36.36%) 4: ['Z2', 'Z3']
    ----------------------------------
    Bin (100.0%) 0: ['H', 'C', 'F', 'A']
    Bin (100.0%) 1: ['I', 'D']
    Bin (90.91%) 2: ['B', 'E']
    Bin (100.0%) 3: ['Z0', 'G', 'Z1']
    Bin (54.55%) 4: ['Z2', 'Z3', 'Z4']

```
* Note that (xxx%) is the percentage of fullness

Contributors
------------

* Paulo Kuong ([@pkuong](https://github.com/paulokuong))
