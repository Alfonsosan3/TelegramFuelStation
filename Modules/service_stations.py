#MY MODULES

from Utils.utils import getDistanceLatLong,url_google_maps
from Classes.fuel_station import Fuel_Station,Location

#EXTERNAL MODULES
from json import loads
from requests import get


##############################################################################################




def getServiceStationsByFuelId(fuelId,ccaaId):

    if ccaaId != 0:
        url = f"https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/FiltroCCAAProducto/"+ccaaId+f"/{fuelId}"
    else:
        url = f'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/FiltroProducto/{fuelId}' #Tarda más pero nos aseguramos que si no encuentra el codeCCAA por lo menos de un resultado
    try:
        response = get(url)

        response = loads(response.text)

        return response['ListaEESSPrecio']
    except:
        print('Ha habido un error')

def getFilteredFuelStations(response,Lat1,Long1):
    
    target = 2
    increment = 1.5 
    fuel_station_list = []
    
    while len(fuel_station_list) < 5:

        fuel_station_list = [] #Reiniciamos para que la lista no tenga valores iguales
        target = target*increment
        
        for index in range(len(response)):

            fuel_station = Fuel_Station(response[index])
        

            if getDistanceLatLong(Lat1,Long1,fuel_station.latitude,fuel_station.longitude) <= target: 
            
                fuel_station_list.append(fuel_station)

            

    return fuel_station_list



def cheapestFuelStation(fuel_station_list): 

    fuel_station_list_ordered = sorted(fuel_station_list, key=lambda row: float(row.price))
    
    text = ''

    
    for index in range(5):

        fuel_station = fuel_station_list_ordered[index]
            
        text += f'Gasolinera: {fuel_station.name}, Precio: {fuel_station.price}€ \nAquí tienes la ubicación: {url_google_maps(fuel_station.latitude,fuel_station.longitude)}\n'
   
    return text









