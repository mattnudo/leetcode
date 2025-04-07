#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k)
    # Write your code here

    if n.to_i < 10
        n
    else
        sum = n.chars.map{|x| x.to_i}.reduce(0,:+)
        superDigit(sum.to_s, k)
    end
end


first_multiple_input = gets.rstrip.split

n = first_multiple_input[0]

k = first_multiple_input[1].to_i

puts superDigit n, k

