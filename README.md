to install dependencies run
poetry install

to generate a migration run 
cd test_task_be
alembic revision --autogenerate -m "<YOUR_MESSAGE>"

to run all migrations run
alembic upgrade head

to apply a migration run
alembic upgrade <MIGRATION_ID>

to revert a migration run
alembic downgrade <MIGRATION_ID>

to run the app locally
cd test_task_be
flask run

to open the app locally go to http://localhost:5000
