a,b,c=gets.chomp.split(" ").map{|n|n.to_i}
puts (a+b)%c
puts ((a%c)+(b%c))%c
puts (a*b)%c
puts ((a%c)*(b%c))%c
