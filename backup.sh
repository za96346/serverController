#!env -i /bin/bash --noprofile --norc
CONTAINER=workapp_mysql
DB_NAME=workApplication
FILENAME=~/backup/workApplication/"$(date "+%Y%m%d_%H%M%S")".sql
pwd=siou0722
which python

docker exec -i $CONTAINER bash -c "mysqldump -u root -p$pwd  $DB_NAME" > $FILENAME

python ./sendEmail/backupSuccess.py