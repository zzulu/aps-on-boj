sugar = gets.chomp.to_i
f_q, f_r = sugar.divmod(5)
f_q.downto(0).to_a.each do |q|
  t_q, t_r = (sugar-(q*5)).divmod(3)
  if t_r == 0
    puts q + t_q
    sugar = nil
    break
  end
end
puts -1 unless sugar.nil?
