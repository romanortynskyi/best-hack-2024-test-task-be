SECRET_ARN="arn:aws:secretsmanager:us-east-1:891377136147:secret:best-hack-2024-test-task-be/sqlalchemy-database-uri-mdOYL2"

# Retrieve the secret value
SECRET_VALUE=$(aws secretsmanager get-secret-value --secret-id $SECRET_ARN --query SecretString --output text)

# Export the secret value as an environment variable
export SQKALCHEMY_DATABASE_URI=$SECRET_VALUE

echo "Secret retrieved and stored in \$SECRET environment variable"
