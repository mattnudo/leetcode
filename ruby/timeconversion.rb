#!/bin/ruby

require 'json'
require 'stringio'
require 'time'

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s)
    # Write your code here
    puts Time.parse(s).strftime("%H:%M:%S")
end

s = gets.chomp

timeConversion s

