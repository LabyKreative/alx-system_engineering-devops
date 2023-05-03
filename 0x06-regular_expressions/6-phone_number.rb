#!/usr/bin/env ruby
regex = /^\d{10,10}$/
input = ARGV[0]
matches = input.scan(regex)
puts matches.join
