#een programa om de pokemons folder te clearen zodat ik het niet manueel moet doen.
import shutil
import os  


shutil.rmtree('pokemons')

path = 'pokemons'

os.mkdir(path)