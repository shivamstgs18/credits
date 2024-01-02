Project Setup:

Create a virtual environment:
python3 -m venv .venv

Activate the virtual environment:
source .venv/bin/activate

Install project dependencies from requirements.txt:
pip install -r requirements.txt

Run the FastAPI Application:
Start the FastAPI application using UVicorn:
uvicorn main:app --reload

Access the application at http://127.0.0.1:8000 in your web browser.


Swagger UI : http://127.0.0.1:8000/docs

API Flow:
  POST '/token' - Get JWT for a specific user
  GET '/credits' - Get all credit information from all users
  GET '/credits/{user_id}' - Get all credits for a specific user
  GET 'my_credits' - Get all credits of the current logged-in user
  POST '/credits' - Add new credit to the current logged in user
  PUT '/credits' - Update a specific credit for the current logged in user
  DELETE '/credits/{id}' - Delete the specific credit for the current logged in user

Try the above API flow with any of these users:
Username: admin
password: admin
OR
Username: shivam
password: 1234


