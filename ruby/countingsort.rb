#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr)
    # Write your code here

    counting = Array.new(100,0)
    
    arr.each do |x|

        counting[x] = counting[x].to_i  + 1
    end
    
    puts counting.join(' ')

end

n = gets.strip.to_i

arr = gets.rstrip.split.map(&:to_i)

puts countingSort arr


