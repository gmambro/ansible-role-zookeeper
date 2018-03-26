# -*- mode: ruby -*-
# vim: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos/7"

  config.vm.provider "virtualbox" do |vb|
    config.vm.synced_folder ".", "/home/vagrant/roles/gmambro.zookeeper", type: "virtualbox"
  end

  $script = <<-SCRIPT
     sudo yum install -y epel-release
     sudo yum install -y java-1.7.0-openjdk-devel ansible
  SCRIPT


  config.vm.provision "shell", inline: $script
end
