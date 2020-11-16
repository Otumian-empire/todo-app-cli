# Todo-App-Cli

This is todo app that runs on the commandline connected to an actual database.

## How to set up

A brief guide to how to clone, create database, install modules, run and test app. Feel free to let me know if you need any assistance.

## clone app

- Open the terminal and navigate to where you want to put the app.
- The clone the app with, `git clone https://github.com/Otumian-empire/todo-app-cli.git`.

## create database

- create a file, `.env.local` in the root directory of you app. That is, In `todo-app-cli`.
- copy and paste the content of `.env.remote` into `.env.local`.
- set the database name to `todo_cli_db` and populate the others as necessary.
- Start the local xammp server and mysql.
- create a database with the specified name in phpmyadmin.
- import `todo.sql` into the database opened in phpmyadmin.

## install modules

- Run `pipenv install` on the terminal

## run app

- run `python app.py` for `Option1Parser`
- run `python app.py command [id] [task]` for `Option2Parser`
- read on these parsers from `todo-app-doc.md`

## run tests

- run `python -m unittest discover test`
