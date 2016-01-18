# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 80, host: 5000

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end

  config.vm.provision "shell", privileged: true, inline: <<-SHELL
    set -ex

    apt-get update
    apt-get upgrade -y

    if ! which pip; then
      bash -c "(curl https://bootstrap.pypa.io/get-pip.py | python)"
    fi
    pip install -r /vagrant/app/requirements.txt
    pip install -r /vagrant/app/requirements-dev.txt

    if ! which node; then
      curl -sL https://deb.nodesource.com/setup_5.x | bash -
      apt-get install -y nodejs
    fi
    npm install phantomjs -g
  SHELL

  config.vm.provision "shell", privileged: true, inline: <<-BROWSERS
    set -ex

    if ! grep --quiet "deb http://dl.google.com/linux/chrome/deb/ stable main" /etc/apt/sources.list.d/google-chrome.list; then
      bash -c "(wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key   add -)"
      bash -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
      apt-get update
      apt-get install google-chrome-stable -y
    fi
  BROWSERS
end
