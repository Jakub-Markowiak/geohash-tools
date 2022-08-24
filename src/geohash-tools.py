# Author
# Package description
# etc.

# remember: del, __

_base32ghs = '0123456789bcdefghjkmnpqrstuvwxyz'
_decimal = range(0,32)
# pair base32 characters and decimal characters
_converter_decimal = dict(zip(_decimal, _base32ghs))
_converter_base32ghs = dict(zip(_base32ghs, _decimal))
# convert characters between systems
_decimal_to_base32ghs = lambda x: _converter_decimal[x]
_base32ghs_to_decimal = lambda x: _converter_base32ghs[x]
def _base32ghs_to_base2(x): return(format(_base32ghs_to_decimal(x), '05b'))
_decode_map_base2 = {char: _base32ghs_to_base2(char) for char in _base32ghs}


def encode(lat, lon, precision):
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
    new = [geohash[i:i+5] for i in range(0, len(geohash), 5)]
    geohash = ''.join([_decimal_to_base32ghs(int(i,base=2)) for i in new])

    return(geohash)


def decode(geohash):
    '''
    Decode geohash string as geographical coordinates.
    Returns a (latitude, longitude) tuple.
    '''
    # convert from base32ghs to base2
    geohash_base2 = [int(_decode_map_base2[char]) for char in geohash]

    lat_interval, lon_interval = (-90.0, 90.0), (-180.0, 180.0)
    is_odd = True
    for i in geohash_base2:
        if is_odd:
            if i:
                lon_interval = ((lon_interval[1] + lon_interval[0]) / 2, lon_interval[1])             
            else:
                lon_interval = (lon_interval[0], (lon_interval[1] + lon_interval[0]) / 2)  
        else:
            if i:
                lat_interval = ((lat_interval[1] + lat_interval[0]) / 2, lat_interval[1])    
            else:
                lat_interval = (lat_interval[0], (lat_interval[1] + lat_interval[0]) / 2)

        is_odd = not is_odd

    lat, lon = (lat_interval[1] + lat_interval[0]) / 2, (lon_interval[1] + lon_interval[0]) / 2
    return(lat,lon)


# def neighbours(geohash):
#     return(neighbours_list)

# def distance(geohash_1, geohash_2):
#     return(dist)