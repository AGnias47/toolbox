#!/bin/bash

: '
Installs commonly used utilities for Ubuntu. This is mainly for me so it may 
contain excessive installs for someone elses preferences
'

sudo apt update
sudo apt install -y wget

# Install aliasfile and .vimrc
wget https://raw.githubusercontent.com/AGnias47/toolbox/main/bash/aliasfile
mv aliasfile ~/.bash_aliases
wget https://raw.githubusercontent.com/AGnias47/toolbox/main/bash/vimrc
mv vimrc ~/.vimrc

# Create bash profile
echo 'export PATH=$PATH:/usr/local/bin:/home/$USER/.local/bin' >> ~/.bash_profile
echo 'source ~/.bash_profile || true' >> ~/.bashrc
source ~/.bashrc

# Install packages via apt
sudo apt install -y \
build-essential \
vim \
curl \
python3-{dev,venv,pip} \
openjdk-17-jdk-headless \
ruby-full \
uidmap \
jq \
cmatrix

# Install pyenv
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Common Python dependencies; taken from https://github.com/asdf-vm/asdf/issues/570#issuecomment-531187568
sudo apt install -y \
libssl-dev \
zlib1g-dev \
libbz2-dev \
libreadline-dev \
libsqlite3-dev \
llvm \
libncurses5-dev \
xz-utils \
tk-dev \
libxml2-dev \
libxmlsec1-dev \
libffi-dev \
liblzma-dev

# Configure git
git config --global init.defaultBranch main

# Install packages via snap
sudo snap install spotify
sudo snap install pycharm-community --classic
sudo snap install brave
sudo snap install gimp

# Install rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Install node via nvm
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.bashrc
nvm install node

# Install vscode
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
sudo apt install -y apt-transport-https
sudo apt update
sudo apt install -y code

# Install and run aptupdate script
sudo wget -P /usr/local/bin https://raw.githubusercontent.com/AGnias47/toolbox/main/utilities/aptupdate
sudo chmod 755 /usr/local/bin/aptupdate
sudo aptupdate

echo "Manual Steps to take"
echo "- Setup ssh keys (ssh-keygen -t ed25519 -C <email>)"
echo "- Install Dropbox"
echo "- Confirm rootless Docker install"
