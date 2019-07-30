from pygeocoder import Geocoder
import csv
from time import sleep

gmaps = Geocoder(api_key='GOOGLE_API_KEY') # Google Geocode API aanzetten en API Key invullen

input = open('C:/woningtransacties.csv','r') # csv bestand met latitude en longtitude 
output = open('C:/pythongeocode/addresses.csv','w', newline='') # pad aan passen voor output bestand en vooraf maken csv


try:
    reader = csv.reader(input, delimiter=';', quotechar='|') # selecter juiste delimiter van excel bestand
    next(reader, None)  # skip headers
    writer = csv.writer(output)
    
    counter = 0
    for row in reader:
        if counter == 2506: # aantal regels loop
            break
      
        print(row[23]) # kolom met latitude
        print(row[24]) # kolom met longtitude
        coordinates1 = row[23] # kolom met latitude
        coordinates2 = row[24] # kolom met longtitude
        counter += 1

        my_location = gmaps.reverse_geocode(float(coordinates1), 
        float(coordinates2))
        print(my_location)

        writer.writerow(my_location)
        sleep(0.08)    # wachten in seconden, voor maximale aantal 15 queries/sec API Google

finally:
    input.close()
    output.close()



