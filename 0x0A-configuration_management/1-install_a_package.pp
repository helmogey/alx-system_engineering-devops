#!/usr/bin/pup
# Using Puppet, install flask from pip3.

class { 'python3::pip': }

package { 'python3-flask':
  ensure => '2.1.0',
  provider => 'pip3',
  require => Class['python3::pip'],
}

