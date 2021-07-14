#!/bin/sh

VERSION=/var/lib/jenkins/workspace/test_telebot/code/version.txt

echo ${BUILD_NUMBER}

if [ -f "$VERSION" ]; then
    echo "file  $VERSION  exist."
    rm $VERSION
    echo ${BUILD_NUMBER} >> $VERSION
else
    echo "file $VERSION does not exist."
    echo ${BUILD_NUMBER} >> $VERSION
    echo "version file has been copied"
fi


