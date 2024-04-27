to generate a migration run 
cd test_task_be
alembic revision --autogenerate -m "<YOUR_MESSAGE>"

to apply a migration run
alembic upgrade <MIGRATION_ID>

to revert a migration run
alembic downgrade <MIGRATION_ID>
