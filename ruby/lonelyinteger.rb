#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a)
    # Write your code here
    mapped = Hash.new(0)
    a.each do |x|
        mapped[x] = mapped[x]+1
    end

    mapped.select{|k,v| v.eql? 1}.keys
    
end

n = gets.strip.to_i

a = gets.rstrip.split.map(&:to_i)

puts lonelyinteger a

