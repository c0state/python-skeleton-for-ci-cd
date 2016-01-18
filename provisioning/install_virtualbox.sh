set -ex

if ! grep --quiet "deb http://download.virtualbox.org/virtualbox/debian '$(lsb_release -cs)' contrib non-free" /etc/apt/sources.list.d/virtualbox.list; then
  sh -c "echo 'deb http://download.virtualbox.org/virtualbox/debian '$(lsb_release -cs)' contrib non-free' > /etc/apt/sources.list.d/virtualbox.list"
  wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- | sudo apt-key add -
  apt-get update && sudo apt-get install virtualbox-5.0
fi

echo "Successfully installed virtualbox"
