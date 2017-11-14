#!/usr/bin/env bash
docker build . --tag capsoul-backend
docker run -P --mount source=capsoul-db,target=/code/db --name capsoul_backend -p 42000:8000 -d capsoul-backend
