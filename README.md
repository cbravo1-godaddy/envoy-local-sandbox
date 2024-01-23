# Envoy local sandbox


## Dependencies

- python
- Envoy

## MacOS installations

- install Envoy: 

```zsh
brew tap tetratelabs/getenvoy
brew install envoy

```

- Install Python & FastAPI:


```zsh
brew install python
pip3 install fastapi
pip3 install "uvicorn[standard]"

```

## Get Started

### Init python apps

App 1
```zsh
cd apps/app1
uvicorn main:app --reload --port 1111

```

App 2
```zsh
cd apps/app2
uvicorn main:app --reload --port 2222

```

App 3
```zsh
cd apps/app3
uvicorn main:app --reload --port 3333

```

App 4
```zsh
cd apps/app4
uvicorn main:app --reload --port 4444

```

### Init Envoy

envoy --config-path <config file>
```zsh
envoy --config-path assets-experiment.yaml

```