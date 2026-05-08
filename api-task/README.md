
# Commands

## Login

```bash
  docker login
```

## Non-prod target images

```bash
docker build --target builder -t api-task:builder .
docker build --target development -t api-task:dev .
```

## Build image

```bash
docker build --target production --build-arg VERSION=0.3.0 -t api-task:0.3 -t api-task:latest .
```

## Run container

```bash
docker container run -d -p 2026:2026 --name api-task3 api-task:0.3
```

## Tag image

```bash
docker tag api-task:0.1 rayzki/api-task:0.1
docker tag api-task:0.1 rayzki/api-task:latest
```

## Pusgh image

```bash
docker push rayzki/api-task:0.3
docker push rayzki/api-task:latest
```

## Scripts

### Automating in prod.sh:

```bash
  #!/usr/bin/env bash
  REGISTRY="twoj-login"
  VERSION=$(grep '^version' pyproject.toml | cut -d'"' -f2)
```

### Docker call

Image build

```bash
  docker build --target production \
    --build-arg VERSION=$VERSION \
    -t $REGISTRY/api-task:$VERSION \
    -t $REGISTRY/api-task:latest \
    .
```

Image push

```bash
  docker push $REGISTRY/api-task:$VERSION
  docker push $REGISTRY/api-task:latest
```
