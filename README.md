# [mainb.us](http://mainb.us)
Mainbus is a website powered by Django and serves as a personal multipurpose hosting website for myself and possibly some close friends to host projects and other content on.

## File Structure
|   `apps`

|   |   *Contains all Django applications for the website*

|   |   `api`

|   |   `authentication`

|   |   `base`

|   |   `...`

|   `mainbus`

|   |   *The main/core directory for the website*

|   `*media`

|   |   *Not managed by github but its where the media uploaded to filestore is stored*

|   `*static`

|   |   *Where Django puts the collected static content.*

|   `temp`

|   |   *Contains temporary content that needs to go elsewhere later*

|   `tools`

|   |   *Contains various tools for both production and development*

|   <`.Debug`>

|   |   *If this file is present Django runs in DEBUG mode*

|   <`mainbus.log`>

|   |   *Where logging information is currently stored*

|   <`README.md`>

|   |   *This file*

|   <`manage.py`>

|   |   *Django manage.py used for development and commands on the webserver*

|   <`db.sqlite3`>

|   |   *SQLite3 database file, should probably switch off of that in prod*


## Setup
TODO

### Development
TODO

### Production
## NGinX
In order to support video sized uploading you need to increase the maximum file upload size for the client, this is done in the main config for the site.  Currently I have this set to 100MB.
```
mainb.us {
    # Other configuration settings...

    client_max_body_size 100M;  # Increase this value as needed (e.g., 100MB)
}
```
