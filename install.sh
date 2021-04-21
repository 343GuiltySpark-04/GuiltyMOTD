#!/bin/bash

sudo mkdir -p -v /usr/local/games/guiltyMOTD/db/
sudo mkdir -p -v /usr/local/games/guiltyMOTD/bin

sudo cp -v ./* /usr/local/games/guiltyMOTD/bin

sudo cp -v ./data/motd_db.yaml /usr/local/games/guiltyMOTD/db/

sudo chown -v -R root:wheel /usr/local/games/guiltyMOTD

sudo chmod -v -R g+w /usr/local/games/guiltyMOTD

sudo chmod -v -R +x /usr/local/games/guiltyMOTD/bin/main.py

sudo ln -v -s /usr/local/games/guiltyMOTD/bin/main.py /usr/bin/guiltyMOTD
