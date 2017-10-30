sudo docker create -v /code/db --name capsoul-db-restore busybox true
sudo docker run --rm -v /tmp:/backup --volumes-from capsoul-db busybox tar -xvf /backup/backup.tar /code/db
