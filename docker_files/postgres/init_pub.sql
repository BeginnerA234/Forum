CREATE DATABASE myforum_db;
CREATE USER postgres_user WITH  PASSWORD 'postgres_password';
GRANT ALL PRIVILEGES ON DATABASE myforum_db TO postgres_user;