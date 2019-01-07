N=10000;a=Array.new(N,1);1.upto(N).each{|n|a[n+n.to_s.split(//).map(&:to_i).inject(:+)-1]=0};a.each_with_index{|f,i|p i+1 if f==1}
