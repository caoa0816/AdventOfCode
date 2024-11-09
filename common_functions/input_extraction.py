import requests
import os

def extract_input(year: int, day: int):
    
    input_destination = f"./{year}/{year}_input"
    os.makedirs(input_destination, exist_ok=True)
    
    session_cookie = '53616c7465645f5fffa5641674233726254bebab13b77f68008b83730d9d40fdf724b2c6e455ade48a1f23ec57542c3595ff5b71b633d6d6e25d1e5022372ab6'
    header = {
             "Cookie": f"session={session_cookie}"
         }
   
    base_url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(base_url, headers=header)
    if response.status_code == 200:
        with open(f"{input_destination}/day{day}_input.txt", "w") as file:
                file.write(response.text)


if __name__ == "__main__":
    extract_input(2022, 1)
    

