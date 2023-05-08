def get_next(y, x, n, m)
  d = [[1, 0],[0, 1],[-1, 0],[0, -1]]
  return d.filter_map do |dy, dx|
    next_y, next_x = y + dy, x + dx
    next unless next_y.between?(0, n-1) && next_x.between?(0, m-1)
    [next_y, next_x]
  end
end

N, M = gets.chomp.split.map(&:to_i)

board = []

N.times do
  board.push(gets.chomp.split.map(&:to_i))
end

def dfs(start_y, start_x, depth, parent_y, parent_x, board) # return sum of numbers
  if depth <= 1
    return board[start_y][start_x]
  else
    sum_list = get_next(start_y, start_x, N, M).filter_map do |ny, nx|
      next if parent_y == ny && parent_x == nx
      dfs(ny, nx, depth-1, start_y, start_x, board)
    end

    if depth == 3
      next_list = get_next(start_y, start_x, N, M).filter { |ny, nx| parent_y != ny || parent_x != nx }
      
      next_list.combination(2).each do |a, b|
        sum = board[a[0]][a[1]] + board[b[0]][b[1]]
        sum_list.push(sum)
      end
    end

    return board[start_y][start_x] + sum_list.max
  end
end


max_sum = 0

(0...N).each do |y|
  (0...M).each do |x|
    sum = dfs(y, x, 4, nil, nil, board)
    if sum > max_sum
      max_sum = sum
    end
  end
end

puts max_sum
