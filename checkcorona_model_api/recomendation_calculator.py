
def recomendations(risk, relatives_ages, relatives_existent_disease, relatives_habits):
    result = []

    if risk == "LOW":
        result.append("Aparentemente no esta infectad@, para obtener un diagnostico médico, te recomendamos comunicarte con tu medico o centro medico dado que este es un ejercicio de concentización social y NO es un diagnostico medico.")
        result.append("Ten en cuenta que el 15% a 20% de la población podría ser asintomatica y podrias estar infectado sin presentar sintomas. Es importante mantener la distancia con otros, especialmente con grupos de riesgo, para evitar contagios.")
#        result.append("It not seems that you are infected, but we strongly recommend to call the health case system hotline to be sure about that.")
#        result.append("Always have in mind, that 15 to 20% of people are asymptomaic and you can not have any simptom and already have the disease, so respecting the minimum distance with other, specially the ones who are part of a group of risk should be a priority.")
    elif risk == "MODERATE":
        result.append("Habiendo riesgo de infección, te recomendamos que estés aislad@ por al menos 14 días, y que te comuniques con un médico o el número telefónico de atención médica de tu país para obtener un diagnostico médico dado que este es un ejercicio de concientización social y no un diagnostico médico.")
#        result.append("It seems that there is a risk of infection, we strongly recommend to be as much isolated as you can for a period of at least 14 days, and call the helath care system hotline to be sure about the posibility to be infected.")
    elif risk == "HIGH":
        result.append("It seems that you have enough symptoms or a condition that should be threated very quickly, we ask you to call urgently the health care system hotline and get some attention with urgency, and be as much isolated as posible until the you see a doctor. ")
#        result.append("It seems that you have enough symptoms or a condition that should be threated very quickly, we ask you to call urgently the health care system hotline and get some attention with urgency, and be as much isolated as posible until the you see a doctor. ")
    else:
        result.append("")

    if relatives_ages == 1 and relatives_habits == 1:
        result.append("Pr favor, ten en cuenta que convives con una persona que fumo o fuma y con edad cercana al grupo de riesgo. La infección por gripe puede resultar leve para ti, pero riesgosa para quienes conviven con vos.")
#        result.append("Please, also take in care that you live with people that used to smoke and are close to the age of the risk group of elders. Perhaps an infection with coronavirus isn't more than a flu for you, but it can be a risk to your parents.")

    if relatives_ages == 2 or relatives_existent_disease == 1:
        result.append("Tambien ten en cuenta que convives con al menos una persona que esta dentro de un grupo de riesgo y es importante tener especial cuidado de respetar la distancia preventiva de 3 metros  con esta persona. \nSe que es difícil mantener distancia con seres queridos pero es importante demostrar ese afecto cuidando a nuestros convivientes respetando esa distancia y asegurando que no hay riesgo de contagio para ell@s.")
#        result.append("Please, take in care that almost one person who lives with you is part of the risk group and you should have speciall care with him. It is important to respect the distance and left him as much isolated as posible. If you get infected, that person should be in a high risk of infection and have health problems.")
    
    return result
