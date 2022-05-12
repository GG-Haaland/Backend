-- settings.sql
CREATE DATABASE handmedown_with_auth;
CREATE USER handuser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE handmedown_with_auth TO handuser;