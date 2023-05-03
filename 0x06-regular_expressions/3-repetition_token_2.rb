#!/usr/bin/env ruby
regex = /hbt+n/
input = ARGV[0]
matches = input.scan(regex)
puts matches.join
