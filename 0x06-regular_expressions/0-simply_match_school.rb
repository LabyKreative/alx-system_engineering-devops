#!/usr/bin/env ruby
regex = /School/
input = ARGV[0]
matches = input.scan(regex)
puts matches.join
