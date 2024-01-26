

class Fuel_Station(object):


    def __init__(self,json):
        self.name = json['Rótulo']
        self.latitude = json['Latitud'].replace(',','.')
        self.longitude = json['Longitud (WGS84)'].replace(',','.')
        self.price = json['PrecioProducto'].replace(',','.')



class Location(object):

    def __init__(self,location):
        self.latitude = location[0]
        self.longitude = location[1]
    
    

