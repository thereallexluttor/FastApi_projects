from fastapi import FastAPI

#instance of FastAPI class. this represents our API application
app = FastAPI(debug=True)

#importing our api module to register in load time our view functions
from orders.api import api