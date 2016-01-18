if ! which vagrant; then
  wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
  dpkg -i vagrant_1.8.1_x86_64.deb
fi
