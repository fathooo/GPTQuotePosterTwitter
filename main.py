# -*- coding: utf-8 -*-

import schedule
import time
from app import main
from datetime import datetime
import pytz

# Define la zona horaria de Chile
chile_timezone = pytz.timezone('Chile/Continental')

def run_main():
    # Obtén la hora actual en la zona horaria de Chile
    current_time = datetime.now(chile_timezone)
    print(f'Ejecutando: {current_time.strftime("%d-%m-%Y %H:%M:%S")}')
    main()

if __name__ == "__main__":
    # Define la tarea cron
    print(f'Iniciando dia {datetime.now(chile_timezone).strftime("%d-%m-%Y %H:%M:%S")}')
    run_main()
    schedule.every().day.at("20:00").do(run_main)
    # Ejecuta el ciclo para verificar si hay tareas pendientes
    while True:
        schedule.run_pending()
        time.sleep(1)  # Pausa para evitar consumo excesivo de CPU
