import pandas as pd
import numpy as np
import requests


def brazil_local_cases(state):
    brazil_coronavirus_page = requests.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Brazil").text
    brazil = pd.read_html(brazil_coronavirus_page, header=0)[3]

    for column in brazil.columns:
        brazil[column] = brazil[column].str.replace(r"\[.*\]", "")

    brazil = brazil.fillna(0)

    new_header = brazil.iloc[0]
    brazil = brazil[1:]
    brazil.columns = new_header  # set the header row as the df header

    brazil = brazil.rename(
        {"AC": "Acre", "AL": "Alagoas", "AM": "Amazonas", "AP": "Amapá", "BA": "Bahia", "CE": "Ceará",
         "DF": "Distrito Federal", "ES": "Espírito Santo", "GO": "Goiás", "MA": "Maranhão", "MG": "Minas Gerais",
         "MS": "Mato Grosso do Sul", "MT": "Mato Grosso", "PA": "Pará", "PB": "Paraíba", "PE": "Pernambuco",
         "PI": "Piauí", "PR": "Paraná", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte", "RO": "Rondônia",
         "RR": "Roraima", "RS": "Rio Grande do Sul", "SC": "Santa Catarina", "SE": "Sergipe", "SP": "São Paulo",
         "TO": "Tocantins"}, axis='columns')

    state_total_case = brazil[state].iloc[-1].strip()
    return state_total_case


def chile_local_cases(region):
    chile_coronavirus_page = requests.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Chile").text
    chile=pd.read_html(chile_coronavirus_page, header=0)[2]

    chile.set_index('Regions', inplace=True)
    region_total_case= chile.loc[region]['Confirmed cases'].strip()
    return region_total_case


def argentina_local_cases(province):
    argentina_coronavirus_page = requests.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Argentina").text
    argentina=pd.read_html(argentina_coronavirus_page, header=0)[3]
    argentina.set_index('Province', inplace=True)
    argentina_cases = argentina.iloc[:,-1].str.replace(r"[\(\[].*?[\)\]]","").fillna(0)

    province_total_case = argentina_cases.loc[province].strip()
    return province_total_case