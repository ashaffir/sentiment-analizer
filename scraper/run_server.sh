#! /bin/sh
echo "Checking mongoDB..."
mongod=`pgrep mongod`
if [ $mongod -gt 0 ]; then
    echo "Starting uvicorn server..."
    uvicorn main:app --reload --port 8222 --log-config ./log.ini
else
    echo "***********************************"
    echo "***** MongoDB is not running! *****"
    echo " Run:"
    echo "sudo mongod --dbpath ~/data/db"
    echo "***********************************"
fi
