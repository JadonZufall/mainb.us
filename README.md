# [mainb.us](http://mainb.us)
Mainbus is a website powered by Django and serves as a personal multipurpose hosting website for myself and possibly some close friends to host projects and other content on.


## NGinX
In order to support video sized uploading you need to increase the maximum file upload size for the client, this is done in the main config for the site.  Currently I have this set to 100MB.
```
mainb.us {
    # Other configuration settings...

    client_max_body_size 100M;  # Increase this value as needed (e.g., 100MB)
}
```

## Setup
TODO

### Development
TODO

### Production
TODO