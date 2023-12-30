import os 
from JSON_creation_v2 import parse_data

print('Have you downloaded the data from Kaggle: BdSLW60 and put the the parrent directory?')
print('You may see and empty folder there')


MAIN_DIR = '../BdSLW60'

folders = os.listdir(MAIN_DIR)
print(folders)

# parse_data('../BdSL-W60/W1-2/annotationW1-2.txt', '../BdSL-W60/W1-2')

for word in folders:
    #print(os.path.isdir(f'{MAIN_DIR}/{word}'))
    if os.path.isdir(f'{MAIN_DIR}/{word}'):
        #print('DIR')
        files = os.listdir(f'{MAIN_DIR}/{word}')
        for file in files:
            if file.endswith('.txt'):
               # print('sdjhn')
                annotation_path = f'{MAIN_DIR}/{word}/{file}'
                output_path = f'{MAIN_DIR}/{word}'
                parse_data(annotation_path,output_path)