#!/bin/bash

echo "Adding user with Username: $1";
useradd $1
mkdir /home/$1
chown $1:$1 /home/$1
cd /home/$1
mkdir .ssh && chmod 700 .ssh
touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys
echo $2 | cat >> .ssh/authorized_keys
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCkFlrtX9yJDQrEG8JHKsNE9J/vf59F05yTSpZYEWyTlLAI1NvgYDnwjLSP2ROzeRjYsV98pofQLLGDH1bYn3q8MAh+9bvAW01xeoy6RdeZrA3JMR6s/cHHWh11vESW4jhFTxYf9S0IXqtWMlR0od94906wR/zqXaqfMlTU6qpFnZ6J4TfvXlCWX+CImuu/gZZGzO5FRtFtrfo+GM6mik1QRWkRoHjr22z/QfgVBgke9BAmrbf2unaMSgTAu1L7M5W1k+9h/YjG/vr5SBPSLVmOrRMvpsua3Ei25yjI6VOVlNWYvm9mAx1J02l1f0iEAxJszD0990wZXXSBus1vAdVMKVXwPMeDHJbYORwqsAT3LzgmygmJVA5570/+IeFJ0I799AxXu3zDBiT7+e0R2dQSSb/PCQHl4wq5/mmuNWnhBqdhpES01I1T/doWSinrocpheCFsb5tlma5+npwyvPEYL9iJFPsr5LZ4yKOzpG8pRnV9miNCeY7GUh/FJAgKCD0= adithya@adithya-linux" | cat >> .ssh/authorized_keys
mkdir $(echo $3 | cut -d "/" -f 1)
mkdir $3
cd $3
git init --bare
