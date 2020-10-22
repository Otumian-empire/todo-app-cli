# Todo-App-Cli

This is todo app but works on the commandline.

## TOOLS

git text editor (vscode, sublime, ...)

## FILES

- `app.py` - interfaces the front end to the backend
- `model.py` - interface the backend to the front end
- `todo.sql` - has the structure of the database table
- `README.md` - has information on how to install/download and run app
- `todo-app-doc.md` - has information on app design

## DEPENDENCIES

- pipenv - track the dependencies that the todo-app depends on and also to separate the todo apps dependencies from the system dependencies (separate sytem environments)
- git - track the files
- mysql-connector-python - as a wrapper around mysql for the database
- xammp (mysql) - for the database

## ACTIVITY MODEL

- todo_cli_db - database name
- todos - table name
- id - uniquely identifies an activity
- task - description of the activity
- created_at - when the activity was added

## CRUD

- create an activity
- read an activity
- read all activities
- update an activity
- delete an activity
- delete all activities

## NAVIGATIONS

- option 1

  - 1 - add an activity
  - 2 - read an activity
  - 3 - read all activities
  - 4 - update an activity
  - 5 - delete an activity
  - 6 - delete all activities
  - 7 - exit

- option 2 (command based)

  - add, activity

    - example:

      - add, eat food
      - add, sleep at 2pm
      - add, call john doe, feed the mouse

  - read, activity_id

    - example:

      - read, 1
      - read, 10

  - read, *

  - read, all

  - update, activity_id, new_task

    - example:

      - update, 1, go to the gym

  - delete, activity_id

    - example:

      - delete, 1
      - delete, 3

  - delete, *

  - delete, all

- exit

## Other notes

- All create, update and delete queries returns a boolean.
- All select queries return a list or an empty list.
- Update, delete and read a single activity by id

## SOME RESOURCES

- [clear-screen]
- [python-mysql]
- [realpython-pipenv-guide]
- [pypa-io-pipenv]
- [xampp]
- [cmd-import-sql-file]

#

[clear-screen]: https://stackoverflow.com/a/2084628/10051170
[pypa-io-pipenv]: https://pipenv.pypa.io/en/latest/basics/
[python-mysql]: https://www.w3schools.com/python/python_mysql_getstarted.asp
[realpython-pipenv-guide]: https://realpython.com/pipenv-guide/
[xampp]: https://www.apachefriends.org/download.html
[cmd-import-sql-file]:https://stackoverflow.com/a/17666279/10051170