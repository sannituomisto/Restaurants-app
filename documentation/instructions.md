# Running the Application Locally

## 1. Clone the Repository
Clone this repository to your machine and navigate to its root directory.

## 2. Create the `.env` File
Create a `.env` file with the following content:

```
DATABASE_URL=<local-database-address>
SECRET_KEY=<secret-key>
```

## 3. Set Up the Virtual Environment
Activate the virtual environment and install the application's dependencies with the following commands:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```

## 4. Set Up the Database Schema
Run the following command to set up the database schema:

```sh
psql < schema.sql
```

## 5. Start the Application
Now, you can start the application with the command:

```sh
flask run
```