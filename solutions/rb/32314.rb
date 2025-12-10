A = gets.chomp.to_i
W, V = gets.chomp.split.map(&:to_i)
puts W / V >= A ? 1 : 0
