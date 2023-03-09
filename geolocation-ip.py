import pygeoip

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def print_record(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    region = rec['region_name']
    country = rec['country_name']
    longitude = rec['longitude']
    latitude = rec['latitude']
    print('[*] Target: {} Geo-located.'.format(tgt))
    print('[+] {}, {}, {}'.format(city, region, country))
    print('[+] Latitude: {}, Longitude: {}'.format(latitude, longitude))

tgt = 'X.X.X.X'
print_record(tgt)

// This is only for educational purpose.
