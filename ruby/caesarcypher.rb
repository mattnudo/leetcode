#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k)
    # Write your code here
    arr = s.chars
    encoded = arr
    arr.each_with_index do |x,y|
        if arr[y].to_s =~ /[a-zA-Z]/
            shifted = arr[y].ord + k
            if shifted > 122
                shifted = shifted - 26
            end
            encoded[y] = (shifted).chr.to_s
        end
            
    end
    encoded.join('')
end

n = gets.strip.to_i

s = gets.chomp

k = gets.strip.to_i

puts caesarCipher s, k


