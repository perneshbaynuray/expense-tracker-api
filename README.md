# Expense Tracker API

## Description
Expense Tracker API service.

## How to run it
./scripts/run.sh

## How to test it
./scripts/test.sh

## Port configuration
Listens on PORT from environment or 8080.

## Rollback

Argo CD deploys what is on the `main` branch, from the `k8s/` folder.

To roll back a deployment, find the commit that introduced
the unwanted image version:

    git log --oneline -- k8s/deployment.yaml

Revert that commit:

    git revert <commit>

Push the revert commit:

    git push origin main

Argo CD automatically syncs the previous version from Git.

Do not use `kubectl rollout undo`, because Argo CD self-heal
would restore the version currently defined in Git.
