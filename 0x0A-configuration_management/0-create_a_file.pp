# Puppet Manifest to Create and Configure a File

file{ '/tmp/school':
ensure => 'file',
permission => 0744,
owner => 'www-data'
group => 'www-data'
content => 'I love Puppet'

}