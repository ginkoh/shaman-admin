# Delete all migrations files, except the __init__py.
find $1*/migrations/*.py ! -name "__init__.py" -type f -delete

# Delete the whole database.
rm $1db.sqlite3

# Execute the migrations.
python3 $1manage.py makemigrations
python3 $1manage.py migrate

# Run the command to create a new super user, since the last one was deleted.
python3 $1manage.py createsuperuser

# How to use it:
# sh delete_migrations.sh ~PATH_TO_YOUR_PROJECT_ROOT/
