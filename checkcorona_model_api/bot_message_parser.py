
def isCountryRisky(country):
    if country in ['China','Spain','Germany','Italy','Iran']:
        return 1
    else:
        return 0

def parseAgeBrackets(value):
    values_dict = {
         "ageGroup1": 1,
         "ageGroup2": 2,
         "ageGroup3": 3,
         "ageGroup4": 4
    }
    return values_dict.get(value)

def parseExistingDisorder(value):
    values_dict = {
         "noPreexistConditions" : 0,
         "hasPreexistConditions": 1
    }
    return values_dict.get(value)

def parseSmokingHistory(value):
    values_dict = {
         "neverSmoke": 1,
         "pastSmoke": 2,
         "currentSmoke": 3
    }
    return values_dict.get(value)

def parseExposureToVirus(value):
    values_dict = {
         "exposure1" : 1,
         "exposure2" : 2,
         "exposure3" : 3
    }
    return values_dict.get(value)

def parseHasFever(value):
    values_dict = {
         "noFever" : 0,
         "hasFever" : 1
    }
    return values_dict.get(value)    

def parseHasRelatedDiseases(value):
    values_dict = {
         "noSymptoms" : 0,
         "hasSymptoms" : 1
    }
    return values_dict.get(value)    