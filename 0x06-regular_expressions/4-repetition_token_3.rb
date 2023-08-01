#!/usr/bin/env ruby
# a Ruby script that accepts one argument and pass it
# to a regular expression matching using  repetition topens

puts ARGV[0].scan(/hbt{0,4}n/).join