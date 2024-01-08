import requests
import unittest

class TestEndpoints(unittest.TestCase):
    base_url = 'http://localhost:8000/api/'  # Reemplaza con tu URL base
    token = '60223ca07830a10a5d5dab1de8918cf03ed56d33'  # Replace with the token you received


    def test_authenticated_request(self):
        headers = {'Authorization': f'Token {self.token}'}
        response = requests.get(self.base_url + 'InstitucionEducativa/', headers=headers)
        
        self.assertEqual(response.status_code, 200)  # Adjust as per your expectations     
        

        read_only_fields = ('created_at',) 
        data = {'nombreInstitucionEducativa': 'Escuela 14', 'activo': True}  # Datos a enviar en la solicitud POST        
        response = requests.post(self.base_url + 'InstitucionEducativa/', headers=headers, json=data)        
        self.assertEqual(response.status_code, 201)  # Ajusta según el código esperado (201: Created)

 
        data = {'nombreInstitucionEducativa': 'Escuela 15', 'activo': True}  # Datos a enviar en la solicitud POST        
        response = requests.post(self.base_url + 'InstitucionEducativa/', headers=headers, json=data)        
        self.assertEqual(response.status_code, 201)  # Ajusta según el código esperado (201: Created)

        data = {'nombreInstitucionEducativa': 'Escuela 16', 'activo': True}  # Datos a enviar en la solicitud POST        
        response = requests.post(self.base_url + 'InstitucionEducativa/', headers=headers, json=data)        
        self.assertEqual(response.status_code, 201)  # Ajusta según el código esperado (201: Created)

        data = {'nombreInstitucionEducativa': 'Escuela 17', 'activo': True}  # Datos a enviar en la solicitud POST        
        response = requests.post(self.base_url + 'InstitucionEducativa/', headers=headers, json=data)        
        self.assertEqual(response.status_code, 201)  # Ajusta según el código esperado (201: Created)


        # Additional assertions and validations...

    # Agrega más métodos de prueba para otros tipos de solicitudes (POST, PUT, DELETE, etc.)

if __name__ == '__main__':
    unittest.main()