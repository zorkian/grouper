# grouper

[![Build Status](https://travis-ci.org/dropbox/grouper.png?branch=master)](https://travis-ci.org/dropbox/grouper)

### Description

Grouper is an application to allow users to create and manage memberships
to their own groups.

##### Warning

This project is still very much in flux and likely to have database changes
migration support for the time being.

### Installation

New versions will be updated to PyPI pretty regularly so it should be as easy
as:

```bash
pip install grouper
```

Next you need to configure grouper to find a SQL-style backing database and
stand up processes to serve the read-write web UI and read-only programmatic
API.

Running a Test instance
==========================

Grouper runs behind a reverse proxy that handles Authentication and so expects
a valid, authenticated, user account. I've included a test proxy for running
on development instances.

Creating a development instance:

```bash

# Setup the database.
PYTHONPATH=. bin/grouper-ctl -vvvc config/dev.yaml sync_db

# Run the development reverse proxy
PYTHONPATH=. bin/grouper-ctl -vvc config/dev.yaml user_proxy $USER

# Run the frontend server
PYTHONPATH=. bin/grouper-fe --config=config/dev.yaml -vv

# Run the graph/api server
PYTHONPATH=. bin/grouper-api --config=config/dev.yaml  -vv

```

Setting up the first groups and permissions
===========================================

There are three administrative flags, corresponding to full authority to
administer groups, users, and permissions. These flags can be set for any
account and grant powers independent of the usual way and are given out manually
via the following commands:

```bash

# Allow user to set up groups and group-membership.
PYTHONPATH=. bin/grouper-ctl -c config/dev.yaml -vv \
    capabilities add user@example.com group_admin

# Allow someone to enable/disable user accounts.
PYTHONPATH=. bin/grouper-ctl -c config/dev.yaml -vv \
    capabilities add user@example.com user_admin

# Allow someone to create permissions.
PYTHONPATH=. bin/grouper-ctl -c config/dev.yaml -vv \
    capabilities add user@example.com permission_admin

```
