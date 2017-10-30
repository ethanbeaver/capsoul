docker volume create --name capsoul-db
docker create -v /code/db --name capsoul-db-restore busybox true
docker run --rm -v /tmp/capsoul:/backup --mount source=capsoul-db,target=/code/db busybox tar -xvf /backup/backup.tar
docker rm capsoul-db-restore
