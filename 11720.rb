n = gets.chomp
str = gets.chomp.to_s
print str.split(//).inject(0){|sum,i|sum+=i.to_i}