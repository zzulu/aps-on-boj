T = gets.chomp.to_i

T.times do
  n = gets.chomp.to_i
  dp = Array.new(3+n+1, 0)
  dp[1], dp[2], dp[3] = 1, 2, 4
  (4..n).each do |i|
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  end
  puts dp[n]
end
