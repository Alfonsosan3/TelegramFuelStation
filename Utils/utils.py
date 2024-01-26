from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from datetime import datetime
from Classes.fuel_station import Location





def getDistanceLatLong(Lat1,Long1,Lat2,Long2):

    coords1 = (Lat1,Long1)
    coords2 = (Lat2,Long2)

    return geodesic(coords1,coords2).km       

def url_google_maps(latitude:str,longitude:str):
    
    url = "https://www.google.com/maps/search/?api=1&query="

    
    quote_address = f'{latitude},{longitude}' 
    total_url = url + quote_address

    return total_url





def getState(latitude, longitude):

    geolocator = Nominatim(user_agent="telegrambotgasolineras")
    

    ubicacion = geolocator.reverse((latitude, longitude), language='es')
    
    
    state = ubicacion.raw.get('address', {}).get('state', '')

    if state == '':
        state = ubicacion.raw.get('address', {}).get('city', '')
    else:
        pass 
    return state

def getCCAA(CCAA):

    if  CCAA == 'Andalucía':
        set_codeNumber = '01'
    elif CCAA == 'Aragón':        
        set_codeNumber = '02'
    elif CCAA == 'Asturias':        
        set_codeNumber = '03'
    elif CCAA == 'Islas Baleares':        
        set_codeNumber = '04'
    elif CCAA == 'Canarias':       
        set_codeNumber = '05'
    elif CCAA == 'Cantabria':        
        set_codeNumber = '06'
    elif CCAA == 'Castilla-La Mancha':        
        set_codeNumber = '07'
    elif CCAA == 'Castilla y León':        
        set_codeNumber = '08'
    elif CCAA == 'Cataluña':        
        set_codeNumber = '09'                        
    elif CCAA == 'Comunidad Valenciana':   
        set_codeNumber = '10'
    elif CCAA == 'Extremadura':        
        set_codeNumber = '11'    
    elif CCAA == 'Galicia':        
        set_codeNumber = '12'
    elif CCAA == 'Comunidad de Madrid':        
        set_codeNumber = '13'
    elif CCAA == 'Región de Murcia':        
        set_codeNumber = '14'
    elif CCAA == 'Pamplona':        
        set_codeNumber = '15'
    elif CCAA == 'País Vasco':        
        set_codeNumber = '16'
    elif CCAA == 'La Rioja':        
        set_codeNumber = '17'
    elif CCAA == 'Ceuta':        
        set_codeNumber = '18'
    elif CCAA =='Melilla':
        set_codeNumber = '19'
    else:
        set_codeNumber = '0'  #Por si no se encuentra la ubicación                  
    return set_codeNumber


def time_now():
    
    now = datetime.now()
    format = now.strftime('%Y-%m-%d %H:%M:%S')
    return format
