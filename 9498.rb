s=gets.chomp.to_i
r = case s
when 90..100 then 'A'
when 80..89 then 'B'
when 70..79 then 'C'
when 60..69 then 'D'
else 'F' end
puts r
