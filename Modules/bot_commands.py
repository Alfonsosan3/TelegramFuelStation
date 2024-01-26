



from telegram import Update,ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import  ContextTypes
from Modules.service_stations import cheapestFuelStation,getFilteredFuelStations,getServiceStationsByFuelId
from Utils.utils import getState,getCCAA,time_now
from db_mysql.connection import log_register,ccaa_register



async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global latitude1,longitude1
    user_location = update.message.location
    latitude1 = user_location.latitude
    longitude1 = user_location.longitude


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    log_register('start',time_now())
    await update.message.reply_text(
    'Para que haga una búsqueda de las gasolineras más cercanas a tu ubicación, por favor comparta la ubicación (selecciona el recuadro que aparece en el teclado: Compartir Ubicación).\nPara seleccionar el tipo de producto: \n/diesel95\n/gasolina95',
    reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Compartir ubicación", request_location=True)]]))
    

async def fuel_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text('¿Que tipo de producto te interesa consultar? \n /gasolina95 \n /diesel')


async def f95_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        
        state = getState(latitude1,longitude1)
        code_CCAA = getCCAA(state)
        fuelId = 1 #Gasolina 95
        service_stations = getServiceStationsByFuelId(fuelId,code_CCAA)
        stations_by_user_location = getFilteredFuelStations(service_stations,latitude1,longitude1)   

        await update.message.reply_text(f'{cheapestFuelStation(stations_by_user_location)}')

        log_register('f95',time_now())
        ccaa_register(code_CCAA,time_now())

        
    except NameError:

        log_register('error location',time_now())
        await update.message.reply_text('Por favor comparta su ubicación.')
        

async def diesel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        
        state = getState(latitude1,longitude1)
        code_CCAA = getCCAA(state)
        fuelId = 4 #Diesel
        service_stations = getServiceStationsByFuelId(fuelId,code_CCAA)
        stations_by_user_location = getFilteredFuelStations(service_stations,latitude1,longitude1)   

        await update.message.reply_text(f'{cheapestFuelStation(stations_by_user_location)}')

        log_register('diesel',time_now()) 
        ccaa_register(code_CCAA,time_now())    
        
    except NameError:

        log_register('error location',time_now())
        await update.message.reply_text('Por favor comparta su ubicación.')
        

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text('Se ha producido un error, inténtalo de nuevo.')
    print(context.error)
    log_register('error location',time_now())