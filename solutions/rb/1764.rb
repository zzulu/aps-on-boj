require 'set'

N, M = gets.chomp.split.map(&:to_i)

a, b = Set.new, Set.new

N.times do
  a.add(gets.chomp)
end

M.times do
  b.add(gets.chomp)
end

i = a & b
puts i.count
i.sort.each do |name|
  puts name
end
