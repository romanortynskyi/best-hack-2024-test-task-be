SECRET_NAME="best-hack-2024-test-task-be/sqlalchemy-database-uri"

# Retrieve the secret value
SECRET_VALUE=$(aws secretsmanager get-secret-value --secret-id $SECRET_NAME --query SecretString --output text)

# Export the secret value as an environment variable
export SQKALCHEMY_DATABASE_URI=$SECRET_VALUE

echo "Secret retrieved and stored in \$SECRET environment variable"
