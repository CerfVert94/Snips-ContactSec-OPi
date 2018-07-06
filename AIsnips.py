import io
import json
import requests

from snips_nlu import SnipsNLUEngine, load_resources
from snips_nlu.default_configs import CONFIG_FR

with io.open("dataset.json") as f:
    sample_dataset = json.load(f)

load_resources("fr") #indinque la langue
nlu_engine = SnipsNLUEngine(config=CONFIG_FR)#configuration supplémentaire pour la langue
nlu_engine.fit(sample_dataset)

while(True):
    x = input("tapez votre question sur le temps? ")
    #parsing = engine.parse(u""+x)
    #res = json.dumps(parsing, indent=2)
    #city=extract city name
    
    print(x)
