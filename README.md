# [mainb.us](http://mainb.us)
Mainbus is a website powered by Django and serves as a personal multipurpose hosting website for myself and possibly some close friends to host projects and other content on.

## File Structure
```
📂./
 ┣ 📂/apps
 ┃ ┣ 📂/api
 ┃ ┃ ┗ ...
 ┃ ┣ 📂/authentication
 ┃ ┃ ┗ ...
 ┃ ┣ 📂/base
 ┃ ┃ ┗ ...
 ┃ ┗ ...
 ┣ 📂/mainbus
 ┃ ┗ ...
 ┣ 📂/media
 ┃ ┗ ...
 ┣ 📂/static
 ┃ ┗ ...
 ┣ 📂/temp
 ┃ ┗ ...
 ┣ 📂/tools
 ┃ ┗ ...
 ┣ 📜.DEBUG
 ┣ 📜mainbus.log
 ┣ 📜README.md
 ┣ 📜manage.py
 ┗ 📜db.sqlite3
```

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

## SSH
The ssh port for the server has been changed from `22` to `22022` to avoid crawlers that kept attempting to login.



## Tool Documentation
TODO

## Application Descriptions
TODO

## Models
TODO

## Views
TODO