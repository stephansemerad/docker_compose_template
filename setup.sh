
# Step 1.
# Set Up Enviroment
# ----------------------------------------------
cd flask_app
python -m venv venv      
venv\scripts\activate

python -m pip install --upgrade pip
python -m pip install flask
python -m pip install flask_sqlalchemy
python -m pip install psycopg2-binary
python -m pip install pytest
python -m pip freeze > requirements.txt

# Step 2.
# Create docker Image
# ----------------------------------------------
cd flask_app
docker image build -t flask_app .
docker run -p 8080:5000 flask_app
docker run -p 8080:5000 flask_app # Optional Run in Detached Mode

# Step 3.
# Create docker-compose.yaml
# ----------------------------------------------
docker-compose build
docker-compose up
curl http://localhost:8080/

# Expected result 
# '''
# {
#   "hello": "Welcome to the world of tommorow!"
# }
# '''