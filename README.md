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

1. starting all the apps with a single command

```zsh
cd apps

python3 init_multiple.py
```


2. Just curiosity: init every app manually

```zsh
cd apps

# App1
python3 app --appNumber 1 --port 1111

# App2
python3 app --appNumber 2 --port 2222

#App3
python3 app --appNumber 3 --port 3333

#App4
python3 app --appNumber 4 --port 4444
```


### Init Envoy

Run: envoy --config-path <config file>

```zsh
cd envoy

envoy --config-path assets-experiment.yaml

```

### Init Haproxy

Look doc at haproxy/README.md