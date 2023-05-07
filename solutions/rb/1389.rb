N, M = gets.chomp.split.map(&:to_i)

graph = Array.new(N+1) { [] }
distance_sum = Array.new(N+1, 0)
distance_sum[0] = Float::INFINITY

M.times do
  u, v = gets.chomp.split.map(&:to_i)
  graph[u].push(v)
  graph[v].push(u)
end

(1..N).each do |n|
  visited = Array.new(N+1, false)
  distance = Array.new(N+1, Float::INFINITY)
  distance[0], distance[n] = 0, 0
  queue = [n]

  until queue.empty?
    vertex = queue.shift

    graph[vertex].each do |v|
      if !visited[v]
        distance[v] = distance[vertex] + 1
        queue.push(v)
      end
    end

    visited[vertex] = true
  end

  distance_sum[n] = distance.sum
end

puts distance_sum.each_with_index.min.last
