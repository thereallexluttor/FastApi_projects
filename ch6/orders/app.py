from fastapi import FastAPI
import yaml
from pathlib import Path
#instance of FastAPI class. this represents our API application

app = FastAPI(debug=True, openapi_url="/openapi/orders.json", docs_url="/docs/orders")

oas_doc = yaml.safe_load(
 (Path(__file__).parent / 'oas.yaml').read_text()
) 

app.openapi = lambda: oas_doc

#importing our api module to register in load time our view functions
from orders.api import api