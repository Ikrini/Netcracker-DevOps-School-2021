#!/bin/sh

VERSION=/home/otherinion/test_telegram_bot/Netcracker-DevOps-school-2021/code/version.txt

echo ${BUILD_NUMBER}

if [ -f "$VERSION" ]; then
    echo "file  $VERSION  exist."
    rm $VERSION
    cat ${BUILD_NUMBER} >> $VERSION
else
    echo "file $VERSION does not exist."
    cat ${BUILD_NUMBER} >> $VERSION
    echo "version file has been copied"
fi


