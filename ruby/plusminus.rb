#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr)
    # Write your code here
    
    negatives = []
    positives = []
    zeroes = []

    arr.each do |x|
        if x.positive?
            positives << x
        elsif x.negative?
            negatives << x
        else
            zeroes << x
        end
    end
    
    puts positives.size.to_f / arr.size
    puts negatives.size.to_f / arr.size
    puts zeroes.size.to_f / arr.size
    
    #puts arr.select{|element| element.positive?}.size.to_f / arr.size
    #puts arr.select{|element| element.negative?}.size.to_f / arr.size
    #puts arr.select{|element| element.zero?}.size.to_f / arr.size
    
end

n = gets.strip.to_i

arr = gets.rstrip.split.map(&:to_i)

plusMinus arr
