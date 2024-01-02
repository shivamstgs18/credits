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
