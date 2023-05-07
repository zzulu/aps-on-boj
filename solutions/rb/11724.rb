N, M = gets.chomp.split.map(&:to_i)

graph = Array.new(N+1) { [] }
visited = Array.new(N+1, false)
visited[0] = true

(1..M).each do
  u, v = gets.chomp.split.map(&:to_i)
  graph[u].push(v)
  graph[v].push(u)
end

count = 0
current = 1
until visited.all?
  count += 1
  while visited[current]
    current += 1
  end

  stack = [current]

  until stack.empty?
    vertex = stack.pop
    visited[vertex] = true
    graph[vertex].each do |v|
      if !visited[v]
        stack.push(v)
      end
    end
  end
end

puts count
