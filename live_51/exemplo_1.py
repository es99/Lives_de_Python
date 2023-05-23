"""
Primeira etapa do problema.

Fazer download das imagens dos 100 primeiros pokemons da pokeapi
"""

from datetime import datetime
from time import sleep

start_time = datetime.now()

sleep(2)

time_elapsed = datetime.now() - start_time

print(f"Tempo total (hh:mm:ss.ms) {time_elapsed}")