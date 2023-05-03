#!/usr/bin/env ruby
regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
input = ARGV[0]
matches = input.scan(regex)
puts matches.join(",")
