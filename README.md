# Geohash tools
Python module which supports geohash geocode system based on space-filling curves, announced in 2008 by Gustavo Niemeyer. System allows to encode 2-dimensional data as sequence of characters, where number of characters determines accuracy of decoded information. 

### More detailed information about mathematics behind Geohash can be found here:<br>
Wikipedia: https://en.wikipedia.org/wiki/Geohash<br>
### Important links:<br>
Package is inspired by its Ruby equivalent: https://github.com/masuidrive/pr_geohash<br> 
Github: https://github.com/Jakub-Markowiak/geohash-tools<br>
PyPI repository: https://pypi.org/project/geohash-tools/

## Quick start

Install directly from PyPI repository:

        pip install geohash-tools

Import `geohash tools` to your python module using following command:

        import geohash_tools as gh

## Features

Module provides tools that allows user to perform basic geohash-related operations:
### Coding:
* `encode(lat,lon,precision)` &ndash; encode geographical coordinates as geohash with demanded precision (number of characters),
* `decode(geohash)` &ndash; decode geographical coordinates as (latitude,longitude) tuple.
### Neighbours:
* `adjacent(geohash, direction)` &ndash; find geohash adjacent to geohash specified in input in chosen direction. Returns adjacent geohash with same precision. Allowed directions are `top`, `right`, `bottom`, `left`,
* `neighbours(geohash, include_self=True, show=False)` &ndash; find adjacent geohashes in all 8 directions. If `show` argument is set to `True`, simple ascii map will be printed.
### Measurements:
* `distance(geohash_1, geohash_2)` &ndash; calculate exact distance between pair of geohashes using haversine formula.
  
## Examples
There are presented some simple examples which purpose is to make user more familiar with functions presented in Features section.

### Encoding geohash
    >>> import geohash_tools as gh
    # Default precision is set to 6 characters
    >>> gh.encode(52.41419458448101, 16.899256413657202)
    'u3k40t'
    >>> gh.encode(52.41419458448101, 16.899256413657202, precision=9)
    'u3k40t9wv'
### Decoding geohash
    >>> gh.decode('u3k40t')
    (52.41302490234375, 16.9024658203125)

    >>> gh.decode('u3k40t9wv')
    (52.4142050743103, 16.899268627166748)
### Find adjacent geohash
    >>> gh.adjacent('u3k40t', 'top')
    'u3k40w'

    >>> gh.adjacent('u3k40t9wv', 'left')
    'u3k40t9wu'
### Find geohash neighbours
    >>> gh.neighbours('u3k40w')
    ['u3k40r', 'u3k40x', 'u3k40z', 'u3k40q', 'u3k40w', 'u3k40y', 'u3k40m', 'u3k40t', 'u3k40v']

    >>> gh.neighbours('u3k40t9wv', show=True)

    u3k40t9xh|u3k40t9xj|u3k40t9xn
    ---------|---------|---------
    u3k40t9wu|u3k40t9wv|u3k40t9wy
    ---------|---------|---------
    u3k40t9ws|u3k40t9wt|u3k40t9ww

    ['u3k40t9xh', 'u3k40t9xj', 'u3k40t9xn', 'u3k40t9wu', 'u3k40t9wv', 'u3k40t9wy', 'u3k40t9ws', 'u3k40t9wt', 'u3k40t9ww']        

    >>> gh.neighbours('u3k40w', include_self=False)
    ['u3k40r', 'u3k40x', 'u3k40z', 'u3k40q', 'u3k40y', 'u3k40m', 'u3k40t', 'u3k40v']

### Calculate distance between 2 geohashes
    >>> gh.distance('u3k40t9wv', 'u3k40')
    26666.04332847212

## License
>MIT License
>
>Copyright (c) 2022 Jakub Markowiak
>
>Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
>
>The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


### Contact<br>
Jakub Markowiak: jamarkowiak@gmail.com