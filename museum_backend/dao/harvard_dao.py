import requests
from model.exhibit import Exhibit

def getCurrentExhibits():
    url = 'https://api.harvardartmuseums.org/exhibition'
    params = {
        "apikey": "0ab310c3-a1e2-4d38-9941-748c59b6f91a",
        "status": "current"
    }

    response = requests.get(url = url, params = params)
    data = response.json()

    exhibits = []

    for record in data["records"]:
        name = record["title"]
        startDate = record["begindate"]
        endDate = record["enddate"]
        website = record["url"]
        imageUrl = record["id"]
        exhibit = Exhibit(name, startDate, endDate, website, imageUrl)

        exhibits.append(exhibit)

    print(exhibits)
    return exhibits
