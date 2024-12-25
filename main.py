from fastapi import FastAPI
from api.v1.endpoints.shorten import *
import uvicorn

app = FastAPI()

# List of route inclusion functions
route_functions = [
    include_shorten_routes
]

# Dynamically call each function
for include_route in route_functions:
    include_route(app)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}

# Run the app using uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
