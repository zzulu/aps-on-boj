a,b,c=gets.chomp.split.map(&:to_i)
p a > b ? (b > c ? b : (a > c ? c : a)) : (a > c ? a : (b > c ? c : b))
