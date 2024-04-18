Star Wars API Project (0x06-starwars_api)
Welcome to the Star Wars API project! This project aims to provide a simple and easy-to-use API for accessing various information about the Star Wars universe.

Overview
The Star Wars API project is built with Python and Flask, providing a RESTful API for accessing information such as characters, planets, starships, vehicles, species, and films from the Star Wars universe.

Features
Retrieve information about Star Wars characters
Get details about planets, starships, vehicles, species, and films
Search functionality to find specific characters or items
Authentication support for secure access
Installation
To run the Star Wars API locally, follow these steps:

Clone this repository:
bash
Copy code
git clone https://github.com/Edwinogechi/0x06-starwars_api.git
Navigate to the project directory:
bash
Copy code
cd 0x06-starwars_api
Install dependencies:
Copy code
pip install -r requirements.txt
Set up environment variables:
arduino
Copy code
export API_HOST=0.0.0.0
export API_PORT=5000
export AUTH_TYPE=basic_auth
Run the application:
Copy code
python3 -m api.v1.app
Usage
Once the application is running, you can interact with the API using HTTP requests. Here are some example endpoints:

Get a list of all Star Wars characters:
bash
Copy code
GET /api/v1/characters
Get details about a specific character by ID:
bash
Copy code
GET /api/v1/characters/{character_id}
Search for characters by name:
bash
Copy code
GET /api/v1/characters/search?name={character_name}
For more details on available endpoints and usage examples, refer to the API documentation.

API Documentation
Detailed API documentation can be found in the docs directory. Open the index.html file in your web browser to view the documentation.

Contributing
Contributions to the Star Wars API project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Tasks
0. Star Wars Characters
mandatory
Write a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module
