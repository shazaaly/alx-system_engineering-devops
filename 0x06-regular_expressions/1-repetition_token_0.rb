#!/usr/bin/env ruby
# a Ruby script that accepts one argument and pass it
# to a regular expression matching using  repetition topens

puts ARGV[0].scan(/h?b?t{2,5}n?/).join