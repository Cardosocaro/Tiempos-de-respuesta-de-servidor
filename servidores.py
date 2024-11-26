import requests
import time
from concurrent.futures import ThreadPoolExecutor

# Función para realizar una solicitud
def make_request(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return str(e)

# Función para medir tiempos de múltiples solicitudes
def test_requests(url, num_requests):
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        results = list(executor.map(make_request, [url] * num_requests))
    end_time = time.time()

    successful_requests = results.count(200)
    print(f"\n--- Test: {num_requests} Requests ---")
    print(f"Successful Requests: {successful_requests}/{num_requests}")
    print(f"Time Taken: {end_time - start_time:.2f} seconds")

# Configuración de la prueba
url = "https://www.wikipedia.org"
test_cases = [ 1 , 5, 9, 12, 10,15, 20,25,30,35, 40,50,55, 60,65,70,80,90, 100,200]  # Número de solicitudes por prueba

for test_case in test_cases:
    test_requests(url, test_case)