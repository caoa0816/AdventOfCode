import requests



session_cookie = '53616c7465645f5fffa5641674233726254bebab13b77f68008b83730d9d40fdf724b2c6e455ade48a1f23ec57542c3595ff5b71b633d6d6e25d1e5022372ab6'
header = {
         "Cookie": f"session={session_cookie}"
     }
for i in range(1, 26):
    base_url = f"https://adventofcode.com/2022/day/{i}/input"
    response = requests.get(base_url, headers=header)
    if response.status_code == 200:
        with open(f"./2022/day{i}_input.txt", "w") as file:
            file.write(response.text)