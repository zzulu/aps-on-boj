N=10000;a=(1..N).to_a;1.upto(N).each{|n|a[n+n.to_s.split(//).map(&:to_i).inject(:+)-1]=nil};a.compact.each{|n|p n}
