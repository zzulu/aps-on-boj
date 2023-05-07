def get_next(y, x, n)
  d = [[1, 0],[0, 1],[-1, 0],[0, -1]]
  return d.filter_map do |dy, dx|
    next_y, next_x = y + dy, x + dx
    next unless next_y.between?(0, n-1) && next_x.between?(0, n-1)
    [next_y, next_x]
  end
end


N = gets.chomp.to_i

draw = []

N.times do
  row = gets.chomp.split('')  
  draw.push(row)
end

normal_count, weak_count = 0, 0
normal_visited = Array.new(N) { Array.new(N, false) }
weak_visited = Array.new(N) { Array.new(N, false) }

(0...N).each do |y|
  (0...N).each do |x|
    # Normal
    if !normal_visited[y][x]
      color = draw[y][x]

      stack = [[y, x]]
      until stack.empty?
        sy, sx = stack.pop

        normal_visited[sy][sx] = true
        get_next(sy, sx, N).each do |ny, nx|
          if !normal_visited[ny][nx] && color == draw[ny][nx]
            stack.push([ny, nx])
          end
        end
      end

      normal_count += 1
    end

    # Weak
    if !weak_visited[y][x]
      colors = draw[y][x] == 'B' ? ['B'] : ['R', 'G']

      stack = [[y, x]]
      until stack.empty?
        sy, sx = stack.pop

        weak_visited[sy][sx] = true
        get_next(sy, sx, N).each do |ny, nx|
          if !weak_visited[ny][nx] && colors.include?(draw[ny][nx])
            stack.push([ny, nx])
          end
        end
      end

      weak_count += 1
    end
  end
end

puts "#{normal_count} #{weak_count}"
