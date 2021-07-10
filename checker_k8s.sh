#!/bin/sh

FILE=/var/lib/jenkins/workspace/test_telebot/config_k8s.py

echo ${WORKSPACE}

if [ -f "$FILE" ]; then
    echo "secret file $FILE  exist."
    rm $FILE
    cat ${ConfigPy} >> $FILE
else
    echo "secret file $FILE does not exist."
    cat ${FILE}
    cat ${ConfigPy} >> $FILE
    echo "secret file has been copied"
fi
