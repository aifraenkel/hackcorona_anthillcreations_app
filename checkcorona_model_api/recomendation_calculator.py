
def recomendations(risk, relatives_ages, relatives_existent_disease, relatives_habits):
    result = []

    if risk == "LOW":
        result.append("It not seems that you are infected, but we strongly recommend to call the health case system hotline to be sure about that.")
        result.append("Always have in mind, that 15 to 20% of people are asymptomaic and you can not have any simptom and already have the disease, so respecting the minimum distance with other, specially the ones who are part of a group of risk should be a priority.")
    elif risk == "MODERATE":
        result.append("It seems that there is a risk of infection, we strongly recommend to be as much isolated as you can for a period of at least 14 days, and call the helath care system hotline to be sure about the posibility to be infected.")
    elif risk == "HIGH":
        result.append("It seems that you have enough symptoms or a condition that should be threated very quickly, we ask you to call urgently the health care system hotline and get some attention with urgency, and be as much isolated as posible until the you see a doctor. ")
    else:
        result.append("")

    if relatives_ages == 1 and relatives_habits == 1:
        result.append("Please, also take in care that you live with people that used to smoke and are close to the age of the risk group of elders. Perhaps an infection with coronavirus isn't more than a flu for you, but it can be a risk to your parents.")

    if relatives_ages == 2 or relatives_existent_disease == 1:
        result.append("Please, take in care that almost one person who lives with you is part of the risk group and you should have speciall care with him. It is important to respect the distance and left him as much isolated as posible. If you get infected, that person should be in a high risk of infection and have health problems.")
    
    return result
