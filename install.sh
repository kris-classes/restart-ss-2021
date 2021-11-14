#!/bin/bash
#run this with the command :
# curl https://raw.githubusercontent.com/kris-classes/restart/main/install.sh | bash
echo "Starting restart install script"
echo "============"

echo "installing cowsay"
sudo yum install -y cowsay
echo "finished installing cowsay" | cowsay

echo "installing tmux"
sudo yum install -y tmux
echo "finished installing tmux"

echo "installing net-tools"
sudo yum install -y net-tools
echo "finished installing net-tools"

echo "installing sl"
sudo yum install -y sl
echo "finished installing sl"

echo "installing micro text editor"
curl https://getmic.ro | bash
cd
mkdir bin
mv micro bin/
echo "finished installing micro text editor"


echo "Update .bashrc with /bin for our PATH"
echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
echo "Done updating PATH"


echo 'alias l="ls -alh"' >> "$HOME/.bashrc"

echo "Run the command 'source $HOME/.bashrc' to update your PATH"
