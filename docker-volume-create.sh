read -p "Enter CS Lab username:" username
scp $username@10.9.6.102:/tmp/capsoul/capsoul-db.tar /tmp/capsoul/
docker volume create --name capsoul-db
docker create -v /code/db --name capsoul-db-restore busybox true
docker run --rm -v /tmp/capsoul:/backup --mount source=capsoul-db,target=/code/db busybox tar -xvf /backup/capsoul-db.tar
docker rm capsoul-db-restore
