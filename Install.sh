#!/bin/bash

echo "Starting restart install script"
echo "installing cowsay"
sudo yum install -y cowsay
echo "finished" | cowsay
