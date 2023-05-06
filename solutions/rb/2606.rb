v = gets.chomp.to_i
e = gets.chomp.to_i

graph = Array.new(v+1) { [] }

(0...e).each do
  s, e = gets.chomp.split(' ').map(&:to_i)
  graph[s].push(e)
  graph[e].push(s)
end

stack = [1]
visited = Array.new(v+1, false)

until stack.empty?
  vertex = stack.pop

  visited[vertex] = true
  graph[vertex].each do |v|
    if !visited[v]
      stack.push(v)
    end
  end
end

puts visited[2..].count(true)
