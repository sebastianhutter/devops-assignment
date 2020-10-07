# kubernetes - setup

The python script `setup.py` spins up a kubernetes cluster at digitalocean
and downloads a kubeconfig file with a token validy of around 30 days.

You need to specify the digitalocean access token to execute the script.

## Preparation

To execute the scripts you need to setup a local virtualenv

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Spin up cluster

```bash
DIGITALOCEAN_ACCESS_TOKEN=mycoolaccesstoken ./setup.py
```

Encrypt the kubeconfig filw with the candidates public gpg key and send it to her.
```bash
# load public key to gpg keychain
# https://www.gnupg.org/gph/en/manual/x56.html
# https://www.gnupg.org/gph/en/manual/x110.html
gpg --import key.asc
gpg --output kubeconfig.gpg --encrypt --recipient <candidatesgpgkeyid> kubeconfig
```

## Cleanup

After the assingment is complete destroy the kubernetes cluster

```bash
DIGITALOCEAN_ACCESS_TOKEN=mycoolaccesstoken ./destroy.py
```