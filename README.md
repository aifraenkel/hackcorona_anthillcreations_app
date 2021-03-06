# Hackcorona, anthillcreations team

Our goal is provide the community a simple to use tool that enables people to get an insight about a the possibility of a Covid19 infection and educate about how to take care of themselves and their relatives.

At the momento, it is a Facebook Messenger Chatbot. The architecture is ready to scale to most used social networks, including WhatsApp. The demostration is implemented for latin america, spanish language.

## Who we are?
 - Claire-Isabelle Carlier (Canada), Data Science (Python, a bit of SQL), Azure, Business Analytics, Data Modeling & Visualization, Web Scraping
 - Souradeep Paul (India), Product Management, Project Management, Design
 - Jessie Hsieh (Germany), Python, SQL, AWS and GCP. Web Scraping and flask web application
 - Sean Zhang (US), Software Development (Fullstack), React.js, iOS backend: AWS Serverless
 - Alejandro Fraenkel (Argentina), Software architecture and development. AWS, Azure and GCP, Java and .net backend and testing automation
 - Deepshikha Jain (Canada), Business Analytics & Research (Healthcare experience)

# Documentation
## MVP - Design Decisions - a.k.a. Why?
 - [x] We choose python for the models api, because python was the most suitable language to do an experiment of risk calculation model, and it also simplifies the evolution  of that model to a Machine Learning model. 
 - [x] We priorize productivity and time to market, instead of priorizing code quality and coverage because the whole MVP was developed in a two days hackathon.
 - [x] Chatbot was developed using DialogFlow, because that platform is good enough for scale the bot and have lot of options of integration.
 - [x] To simplify costs management, and because it was natural too, we use GCP for every component.

## Requirements
 - Python 3.7
 - GCP command line tools
 - GCP project deployment user permission

## Installation and usage
We recommend installing and runnig api into a virtual environment context.  
1. Start virtual environment
```
py -m venv env
env\Scripts\activate
```
2. Install dependencie and run the api
```
pip install -r requirements.txt
py main.py
```
3. Stop virtual env
```
deactivate
```

## Deployment
Being on api folder, the folder where app.yaml is located
```
gcloud login
gcloud app deploy
```
