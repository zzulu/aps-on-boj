class String
  def numeric?
    Float(self) != nil rescue false
  end
end


N, M = gets.chomp.split.map(&:to_i)

dex_no_to_poke = {}
dex_poke_to_no = {}

(1..N).each do |i|
  pokemon = gets.chomp

  dex_no_to_poke[i] = pokemon
  dex_poke_to_no[pokemon] = i
end

M.times do
  input = gets.chomp
  if input.numeric?
    puts dex_no_to_poke[input.to_i]
  else
    puts dex_poke_to_no[input]
  end
end
