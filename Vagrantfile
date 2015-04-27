# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision "shell", inline <<-SHELL
    cd /vagrant
    sudo apt-get update
    sudo apt-get install -y python python-pip
    sudo pip install -r requirements.txt
  SHELL
end
