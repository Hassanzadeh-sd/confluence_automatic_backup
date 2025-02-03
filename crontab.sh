0 0 * * * /opt/confluence/automatic_backups/.venv/bin/python /opt/confluence/automatic_backups/automatic_backups.py >> /var/log/scripts/confluence-automatic_backup.log 2>&1
@weekly /opt/confluence/automatic_backups/purge_backups.sh >> /var/log/scripts/purge_backups.log 2>&1
