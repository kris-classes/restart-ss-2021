#!/bin/bash
#run this with the command :
# curl https://raw.githubusercontent.com/kris-classes/restart/main/install.sh | bash
echo "Starting restart install script"
echo "installing cowsay"
sudo yum install -y cowsay
echo "finished installing cowsay" | cowsay

echo "installing tmux"
sudo yum install -y tmux
echo "finished installing tmux"

echo "installing net-tools"
sudo yum install -y net-tools
echo "finished installing net-tools"