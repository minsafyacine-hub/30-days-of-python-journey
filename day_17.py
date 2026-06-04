# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. 
# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names


student_data = [4201, 15.5, 12.0, 18.5, 14.0, 16.0, 'Orléans']
student_ID, *grades, city = student_data

raw_sensor_data = [
    [101, 22.5, 23.0, 21.8],         # Données parfaites
    [102, 19.0, "ERREUR", 20.5],     # Bug : une chaîne de caractères au milieu
    [103, 15.2, 16.1],               # Données parfaites (mais moins de mesures)
    [104]                            # Bug : aucune mesure prise aujourd'hui
]

def clean_weather_data(data_list):
    try : 
        for list in raw_sensor_data:
            ID, *temperatures = list
        print(list)
        print(temperatures / len(temperatures))
    except TypeError:
        for error in enumerate(list):
            d = error.index  
        print(f"Capteur {ID} à l'index {d} : Donnée corrompue détectée.")
    except ZeroDivisionError:
        for error in enumerate(list):
            d = error.index 
        print(f"Capteur {ID} à l'index {d} : Aucune mesure enregistrée.")
    