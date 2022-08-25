# Author: Jakub Markowiak (jamarkowiak@gmail.com)
# Sources:
# https://en.wikipedia.org/wiki/Geohash
# https://github.com/masuidrive/pr_geohash

from math import asin as _asin 
from math import sin as _sin
from math import cos as _cos
from math import sqrt as _sqrt

_base32ghs = '0123456789bcdefghjkmnpqrstuvwxyz'
_decimal = range(0,32)

# zip base32ghs characters and decimal characters
_converter_decimal = dict(zip(_decimal, _base32ghs))
_converter_base32ghs = dict(zip(_base32ghs, _decimal))

# convert characters between systems
_decimal_to_base32ghs = lambda x: _converter_decimal[x]
_base32ghs_to_base2 = lambda x: format(_converter_base32ghs[x], '05b')
_decode_map_base2 = {char: _base32ghs_to_base2(char) for char in _base32ghs}

def encode(lat, lon, precision=6):
    '''
    Encode coordinates as geohash with specified precision (number of characters).
    Returns a string object containing geohash.
    '''
    assert abs(lat) <= 90, 'Invalid latitude'
    assert abs(lon) <= 180, 'Invalid longitude'

    geohash = str()
    lat_interval, lon_interval = (-90.0, 90.0), (-180.0, 180.0)
    is_odd = True

    while len(geohash) < precision * 5:
        if is_odd:
            mid = (lon_interval[0] + lon_interval[1]) / 2
            if lon > mid:
                geohash += '1'
                lon_interval = (mid, lon_interval[1])
            else:
                geohash += '0'
                lon_interval = (lon_interval[0], mid)
        else:
            mid = (lat_interval[0] + lat_interval[1]) / 2
            if lat > mid:
                geohash += '1'
                lat_interval = (mid, lat_interval[1])
            else:
                geohash += '0'
                lat_interval = (lat_interval[0], mid)
        is_odd = not is_odd

    geohash = ''.join([_decimal_to_base32ghs(int(i,base=2)) for i in [geohash[j:j+5] for j in range(0, len(geohash), 5)]])

    return(geohash)

def decode(geohash):
    '''
    Decode geohash string as geographical coordinates.
    Returns a (latitude, longitude) tuple.
    '''
    geohash_base2 = ''.join([_decode_map_base2[char] for char in geohash])

    lat_interval, lon_interval = (-90.0, 90.0), (-180.0, 180.0)
    is_odd = True
    for i in geohash_base2:
        if is_odd:
            if int(i):
                lon_interval = ((lon_interval[1] + lon_interval[0]) / 2, lon_interval[1])             
            else:
                lon_interval = (lon_interval[0], (lon_interval[1] + lon_interval[0]) / 2)  
        else:
            if int(i):
                lat_interval = ((lat_interval[1] + lat_interval[0]) / 2, lat_interval[1])    
            else:
                lat_interval = (lat_interval[0], (lat_interval[1] + lat_interval[0]) / 2)

        is_odd = not is_odd

    lat, lon = (lat_interval[1] + lat_interval[0]) / 2, (lon_interval[1] + lon_interval[0]) / 2
    return(lat,lon)


_neighbours = {
'top': { 'even': "p0r21436x8zb9dcf5h7kjnmqesgutwvy", 'odd': "bc01fg45238967deuvhjyznpkmstqrwx" },
'right': { 'even': "bc01fg45238967deuvhjyznpkmstqrwx", 'odd': "p0r21436x8zb9dcf5h7kjnmqesgutwvy" },
'bottom': { 'even': "14365h7k9dcfesgujnmqp0r2twvyx8zb", 'odd': "238967debc01fg45kmstqrwxuvhjyznp" },
'left': { 'even': "238967debc01fg45kmstqrwxuvhjyznp", 'odd': "14365h7k9dcfesgujnmqp0r2twvyx8zb" }
}

_borders = {
'top': { 'even': "prxz", 'odd': "bcfguvyz" },
'right': { 'even': "bcfguvyz", 'odd': "prxz" },
'bottom': { 'even': "028b", 'odd': "0145hjnp" },
'left': { 'even': "0145hjnp", 'odd': "028b" }
}

def adjacent(geohash, direction):
    '''
    Calculate geohash adjacent to input geohash in specific direction.
    Acceptable directions are 'top', 'right', 'bottom', 'left'.
    Returns adjacent geohash string.
    '''
    base, lastChr = geohash, geohash[-1]
    geohash_type = 'odd' if bool(len(geohash) % 2) else 'even'
    base = base[:-1] 
    if lastChr in _borders[direction][geohash_type]:
        base = adjacent(base, direction)

    return(base + _base32ghs[_neighbours[direction][geohash_type].index(lastChr)])


def neighbours(geohash, include_self = True, show=False):
    '''
    Find all geohashes adjacent to input geohash.
    If argument 'show' is set to True, function prints map of neighbouring geohashes.
    Returns list of neighbours (including input geohash, can be disabled using 'include_self' argument).
    '''
    top, right, bottom, left = (adjacent(geohash, direction) for direction in _borders.keys())
    top_left, top_right, bottom_left, bottom_right = adjacent(top, 'left'), adjacent(top, 'right'), adjacent(bottom, 'left'), adjacent(bottom, 'right')

    if show:
        # print results
        sep = ('-' * len(geohash) + '|') * 2 + '-' * len(geohash)
        print(
            f'''
            {top_left}|{top}|{top_right}
            {sep}
            {left}|\033[1m\033[92m{geohash}\033[0m|{right}
            {sep}
            {bottom_left}|{bottom}|{bottom_right}
            '''
        )

    if include_self:
        return([top_left, top, top_right, left, geohash, right, bottom_left, bottom, bottom_right])
    else:
        return([top_left, top, top_right, left, right, bottom_left, bottom, bottom_right])

_earth_radius = 6371000 # in meters 
def distance(geohash_1, geohash_2):
    '''
    Calculate exact distance between two geohashes.
    Returns distance between input geohashes in meters.
    '''
    (geohash_1_lat, geohash_1_lon), (geohash_2_lat, geohash_2_lon) = decode(geohash_1), decode(geohash_2)

    # calculate distance using haversine formula 
    d = 2 * _earth_radius * _asin(
        _sqrt(
            (_sin((geohash_2_lon - geohash_1_lon) / 2)) ** 2 +
            _cos(geohash_1_lon) * _cos(geohash_2_lon) * _sin((geohash_2_lat - geohash_1_lat) / 2) ** 2
        )
    )

    return(d)

