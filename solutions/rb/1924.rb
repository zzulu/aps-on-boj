x,y = gets.chomp.split.map(&:to_i)
w = ["SUN", "MON","TUE","WED","THU","FRI","SAT"]
x_to_y = 1.upto(x-1).inject(0) do |sum, m|
  case m
  when 1, 3, 5, 7, 8, 10, 12
    sum += 31
  when 4, 6, 9, 11
    sum += 30
  when 2
    sum += 28
  end
end
print w[(x_to_y+y)%7]
