#!/bin/bash
# ------ Uncomment if you don't have Python installed
#sudo apt-get install software-properties-common
#sudo add-apt-repository ppa:deadsnakes/ppa
#sudo apt-get update
#sudo apt-get install python10.8
# -------

sudo apt-get install git python3-pip make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl
sudo pip install virtualenvwrapper

git clone https://github.com/yyuu/pyenv.git ~/.pyenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

exec $SHELL
echo "Check $ pyenv install --list"

# ----
# sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
# git clone https://github.com/pyenv/pyenv.git ~/.pyenv
#echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
#echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
#echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
#exec bash
#
#pyenv versions
#
#git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
#echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
#exec bash
# pyenv virtualenv --version