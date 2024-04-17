# Tour of Heroes API using FastAPI

This is a simple API for the Tour of Heroes tutorial using FastAPI.

## Installation

1. Clone the repository
2. Install the dependencies using `pip install -r requirements.txt`
3. Run the server using `uvicorn main:app --reload --port 7000`

## Usage

The API has the following endpoints:

1. `/heroes` - GET: Get all heroes
2. `/heroes/{hero_id}` - GET: Get a hero by ID
3. `/heroes` - POST: Create a new hero
4. `/heroes/{hero_id}` - PUT: Update a hero by ID