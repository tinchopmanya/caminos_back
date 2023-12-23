import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'centrocaminos.settings')


import django
django.setup()

from faker import Faker
from ccapp.models import Especialidad  # Reemplaza 'TuModelo' con el nombre de tu modelo

fake = Faker()

Especialidad.objects.all().delete()

# Función para poblar datos
def populate_data(num_entries):
    for _ in range(num_entries):
        # Crear instancias de TuModelo con datos aleatorios
        tu_objeto = Especialidad(
            nombreEspecialidad=fake.name(),
            # Añade más campos y métodos faker según tu modelo
        )
        tu_objeto.save()

if __name__ == '__main__':
    num_entries = 150  # Cambia esto al número deseado de entradas a crear
    populate_data(num_entries)
    print(f'{num_entries} datos han sido creados exitosamente.')
