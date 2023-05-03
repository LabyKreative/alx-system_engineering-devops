#!/usr/bin/env ruby
regex = /hb?t?n/
input = ARGV[0]
matches = input.scan(regex)
puts matches.join
