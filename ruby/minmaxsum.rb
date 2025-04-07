#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr)
    # Write your code here
    sum = arr.sum
    puts "#{sum - arr.max} #{sum-arr.min}"
end

arr = gets.rstrip.split.map(&:to_i)

miniMaxSum arr
