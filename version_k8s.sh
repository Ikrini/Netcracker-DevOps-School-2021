#!/bin/sh

VERSIONK=/var/lib/jenkins/workspace/test_telebot/code-kuber/version_k8s.txt

echo ${BUILD_NUMBER}

if [ -f "$VERSIONK" ]; then
    echo "file  $VERSIONK  exist."
    rm $VERSIONK
    echo ${BUILD_NUMBER} >> $VERSIONK
else
    echo "file $VERSION does not exist."
    echo ${BUILD_NUMBER} >> $VERSIONK
    echo "version file has been copied"
fi
