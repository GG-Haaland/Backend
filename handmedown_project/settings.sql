-- settings.sql
CREATE DATABASE handmedown;
CREATE USER hmduser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE handmedown TO hmduser;