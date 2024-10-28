#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
-- Revoke all privileges from public
revoke all on database $POSTGRES_DB from public;
revoke create on schema public from public;

-- Create schema
create schema if not exists $POSTGRES_DB;

-- Set schema as default
revoke create on schema public from public;
alter database $POSTGRES_DB set search_path to $POSTGRES_DB;

-- Create roles
-- Migration role
create role migration;
grant connect on database $POSTGRES_DB to migration;
grant temporary on database $POSTGRES_DB to migration;
grant usage, create on schema $POSTGRES_DB to migration;

-- Read only role
create role read_only;
grant connect on database $POSTGRES_DB to read_only;
grant temporary on database $POSTGRES_DB to read_only;
grant usage on schema $POSTGRES_DB to read_only;
grant select on all sequences in schema $POSTGRES_DB to read_only;
grant select on all tables in schema $POSTGRES_DB to read_only;

-- Read write role
create role read_write;
grant connect on database $POSTGRES_DB to read_write;
grant temporary on database $POSTGRES_DB to read_write;
grant temporary on database $POSTGRES_DB to read_write;
grant usage on schema $POSTGRES_DB to read_write;
grant select, insert, update, delete on all tables in schema $POSTGRES_DB to read_write;
grant usage on all sequences in schema $POSTGRES_DB to read_write;
grant select on all sequences in schema $POSTGRES_DB to read_write;

-- Create users
-- Read only user
create user ${POSTGRES_USER}_ro with encrypted password '$POSTGRES_PASSWORD';
grant read_only to ${POSTGRES_USER}_ro;
grant select on all tables in schema $POSTGRES_DB to read_only;
grant select on all sequences in schema $POSTGRES_DB to read_only;

-- Read write user
grant read_write to $POSTGRES_DB;
grant select, insert, update, delete on all tables in schema $POSTGRES_DB to read_write;
grant usage on all sequences in schema $POSTGRES_DB to read_write;
grant select on all sequences in schema $POSTGRES_DB to read_write;

-- Migration user
create user ${POSTGRES_USER}_migration with encrypted password '$POSTGRES_PASSWORD';
grant migration to ${POSTGRES_USER}_migration;


-- Set default privileges
set role $POSTGRES_DB;
alter default privileges in schema $POSTGRES_DB
    grant select, insert, update, delete on tables to read_write;
alter default privileges in schema $POSTGRES_DB
    grant usage on sequences to read_write;
alter default privileges in schema $POSTGRES_DB
    grant select on sequences to read_write;
alter default privileges in schema $POSTGRES_DB
    grant select on tables to read_only;
alter default privileges in schema $POSTGRES_DB
    grant select on sequences to read_only;
EOSQL
