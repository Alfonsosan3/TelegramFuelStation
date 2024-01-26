from typing import Final #de esta manera nos aseguramos que nuestros valores no cambiaran
from telegram.ext import CommandHandler, Application, filters, MessageHandler
from Modules.bot_commands import start_command,fuel_command,f95_command,diesel_command,error,handle_location



def main():

    
    app = Application.builder().token(TOKEN).build()

    print('Starting...')

    
    

    app.add_handler(MessageHandler(filters.LOCATION,handle_location))

    app.add_handler(CommandHandler('start',start_command))

    app.add_handler(CommandHandler('producto',fuel_command))
    
    app.add_handler(CommandHandler('gasolina95',f95_command))

    app.add_handler(CommandHandler('diesel',diesel_command))


    app.add_error_handler(error)

    

    app.run_polling(poll_interval = 1)






TOKEN : Final = '6818909843:AAGkbU8U7bn0rirPwUC73suKMDI40it713U'  # Token único para el bot de telegram

BOT_USERNAME : Final = '@gasolineras_balearesBot'









if __name__ == '__main__':

    main()
    
    
    

    