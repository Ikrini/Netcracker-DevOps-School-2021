#!/bin/sh

FILEK=/var/lib/jenkins/workspace/test_telebot/config_k8s.py

echo ${WORKSPACE}

if [ -f "$FILEK" ]; then
    echo "secret file $FILE  exist."
    rm $FILEK
    cat ${Config_k8sPy} >> $FILEK
else
    echo "secret file $FILE does not exist."
    cat ${FILEK}
    cat ${Config_k8sPy} >> $FILEK
    echo "secret file has been copied"
fi
