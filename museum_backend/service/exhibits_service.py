from dao.harvard_dao import getCurrentExhibits 

def getExhibitsByCity(city):
    if city == "Boston":
        output = getCurrentExhibits()
        return output
