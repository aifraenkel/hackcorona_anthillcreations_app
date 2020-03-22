from web_scrapping import brazil_local_cases, argentina_local_cases, chile_local_cases

def risk(age_brackets, existing_disorder, smoking_history, country, state, exposed_to_virus, exposed_to_risk_country,
         fever, other_symptons):

    result = {}

    if country == "Brazil":
        cases = int(brazil_local_cases(state))
    elif country == "Argentina":
        cases = int(argentina_local_cases(state))
    elif country == "Chile":
        cases = int(chile_local_cases(state))
    else:
        cases = "not available"

    risk_score = risk_score = age_brackets+existing_disorder+smoking_history+exposed_to_virus+exposed_to_risk_country+other_symptons

    if cases > 100:
        risk_score = risk_score+2
    elif cases > 10 & cases <=100:
        risk_score = risk_score+1
    else:
        risk_score = risk_score

    if fever == 1:
        risk_score = risk_score*1.5
    else:
        risk_score = risk_score

    if risk_score > 12:
        result["risk"] = "HIGH"
    elif risk_score < 6:
        result["risk"] = "LOW"
    else:
        result["risk"] = "MODERATE"

    result["extended_results"] = "Your risk level is "+result["risk"] + ". Number of cases in your state: "+str(cases)
    return result
