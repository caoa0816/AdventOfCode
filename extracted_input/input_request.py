import requests
import logging
import os 

def request_input(year: int, start_date:int, end_date:int):
    session_cookie = '53616c7465645f5fffa5641674233726254bebab13b77f68008b83730d9d40fdf724b2c6e455ade48a1f23ec57542c3595ff5b71b633d6d6e25d1e5022372ab6'
    header = {
        "Cookie": f"session={session_cookie}"
    }

    os.makedirs(os.path.join('~/advent-of-code/{year}'), exist_ok=True)
    if os.path.isdir(os.path.join('~/advent-of-code/{year}')):
        logging.info(f"Input directory successfully created")
    
    input_directory = f'~/advent-of-code/{year}/{year}_input'
    
    for i in range(start_date, end_date+1):   
        base_url = f"https://adventofcode.com/{year}/day/{i}/input"
        response = requests.get(base_url, headers=header)

        if response.status_code == 200:
            with open(f'{input_directory}/day{i}_input.txt', "w") as file:
                file.write(response.text)
                logging.info(f"Successfully extract input for year {year} day {i}")


# session_cookie = '53616c7465645f5fffa5641674233726254bebab13b77f68008b83730d9d40fdf724b2c6e455ade48a1f23ec57542c3595ff5b71b633d6d6e25d1e5022372ab6'
# header = {
#          "Cookie": f"session={session_cookie}"
#      }
# for i in range(1, 26):
#     base_url = f"https://adventofcode.com/2023/day/{i}/input"
#     response = requests.get(base_url, headers=header)
#     if response.status_code == 200:
#         with open(f"./day{i}_input.txt", "w") as file:
#             file.write(response.text)