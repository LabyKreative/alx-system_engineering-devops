#!/usr/bin/env ruby
regex = /[A-Z]*/
input = ARGV[0]
matches = input.scan(regex)
puts matches.join
