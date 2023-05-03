#!/usr/bin/env ruby
regex = /^h.n$/
input = ARGV[0]
matches = input.scan(regex)
puts matches.join
