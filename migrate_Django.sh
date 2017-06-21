#!/bin/bash
rm db.sqlite3; #deletes the database file.
rm -rf task/migrations; #deletes the migrations folder.
python manage.py migrate; #run the initial django migration to create all the initial tables. need this step because we are killing the database just above
python manage.py makemigrations task; #creates the migration.
python manage.py migrate task; #runs the migration.  This will delete all of the data in your database.