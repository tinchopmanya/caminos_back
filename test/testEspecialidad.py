import requests
import unittest

class TestEndpoints(unittest.TestCase):
    base_url = 'http://localhost:8000/api/'  # Reemplaza con tu URL base
    token = '60223ca07830a10a5d5dab1de8918cf03ed56d33'  # Replace with the token you received


    def test_authenticated_request(self):
        headers = {'Authorization': f'Token {self.token}'}
        response = requests.get(self.base_url + 'Especialidad/', headers=headers)
        
        self.assertEqual(response.status_code, 200)  # Adjust as per your expectations     
        
        
        data = {'nombreEspecialidad': 'Fonoaudiologa', 'activo': True}  # Datos a enviar en la solicitud POST        
        response = requests.post(self.base_url + 'Especialidad/', headers=headers, json=data)        
        self.assertEqual(response.status_code, 201)  # Ajusta según el código esperado (201: Created)

 
        data = {'nombreEspecialidad': 'Maesta', 'activo': True}  # Datos a enviar en la solicitud POST        
        response = requests.post(self.base_url + 'Especialidad/', headers=headers, json=data)        
        self.assertEqual(response.status_code, 201)  # Ajusta según el código esperado (201: Created)

        data = {'nombreEspecialidad': 'Psicomotricista', 'activo': True}  # Datos a enviar en la solicitud POST        
        response = requests.post(self.base_url + 'Especialidad/', headers=headers, json=data)        
        self.assertEqual(response.status_code, 201)  # Ajusta según el código esperado (201: Created)

        data = {'nombreEspecialidad': 'Fonoaudiologa', 'activo': True}  # Datos a enviar en la solicitud POST        
        response = requests.post(self.base_url + 'Especialidad/', headers=headers, json=data)        
        self.assertEqual(response.status_code, 201)  # Ajusta según el código esperado (201: Created)


        # Additional assertions and validations...

    # Agrega más métodos de prueba para otros tipos de solicitudes (POST, PUT, DELETE, etc.)

if __name__ == '__main__':
    unittest.main()