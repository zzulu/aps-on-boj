N,x=gets.chomp.split.map(&:to_i)
num=gets.chomp.split.map(&:to_i)
puts num.map{|n| n if n < x}.compact.join(' ')
