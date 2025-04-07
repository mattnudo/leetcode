#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr)
    # Write your code here
    # for 3x3, want to add 
    #prim = [0][0] + [1][1] + [2][2]
    # secondary = [2][0] + [1][1] + [0][2]
    #Math.abs(prim+secondary)
    primary = 0
    secondary = 0
    arr.size.times do |x|
        primary += arr[x][x]
        secondary += arr[x][arr.size-x-1]
    end
    
    absolute_difference(primary, secondary)
    
end

def absolute_difference(primary, secondary)
    (primary - secondary).abs
end


n = gets.strip.to_i

arr = Array.new(n)

n.times do |i|
    arr[i] = gets.rstrip.split.map(&:to_i)
end

puts diagonalDifference arr


