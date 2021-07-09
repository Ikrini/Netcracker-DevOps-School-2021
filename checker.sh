#!/bin/sh

FILE=/var/lib/jenkins/workspace/test_telebot/config.py

echo ${WORKSPACE}

if [ -f "$FILE" ]; then
    echo "secret file $FILE  exist."
    sudo rm $FILE
    cp ${ConfigPy} /var/lib/jenkins/workspace/test_telebot
else
    echo "secret file $FILE does not exist."
    cat ${ConfigPy}
    cp ${ConfigPy} /var/lib/jenkins/workspace/test_telebot
    echo "secret file has been copied"
fi
