BACKUP_DIR="/var/lib/docker/volumes/confluence_home_data/_data/restore/site/"
DAYS_TO_RETAIN=30

if [ $(ls $BACKUP_DIR | wc -l) > 2 ]
then
  find $BACKUP_DIR -maxdepth 1 -type f -ctime +$DAYS_TO_RETAIN -name full-backup*zip -delete
fi
