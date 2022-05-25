
import pygame
import random
import os
import back_end

MAIN_FILE_PATH = os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(MAIN_FILE_PATH, "imagem")
ICON_FOLDER = os.path.join(MAIN_FILE_PATH, "icon")
CARDS_FOLDER = os.path.join(IMAGES_FOLDER, "cartas")
print(ICON_FOLDER)



files = [f for f in os.listdir(CARDS_FOLDER)]
for i in files:
    
    print(f"'{i[:-4]}' : '{i}',")