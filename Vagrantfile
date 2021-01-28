# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  # config.vm.box = "ubuntu/bionic64"
  # config.vm.box_version = "20201006.0.0"
  config.vm.box = "ubuntu/xenial64"
  config.vm.box_version = "~> 20191204.0.0"
  # config.vm.box = "ubuntu/trusty64"
  # config.vm.box_version = "~> 20150420.1.2"

  # config.vm.box_version = "~> 20200304.0.0"

  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provision "shell", inline: <<-SHELL
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer
    sudo apt-get install software-properties-common
    sudo apt-add-repository universe
    sudo apt-get update
    sudo apt-get install python3
    sudo apt-get install python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
    sudo apt-get install python-setuptools
    sudo apt-get install python-virtualenv
    sudo apt-get install python3-pip
    sudo apt-get install python-django
    sudo apt-get install python-djangorestframework
    sudo apt-get install -y python3-venv

    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
 SHELL

end
