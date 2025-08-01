def fact(n)
  (1..n).reduce(1, :*)
end

def ncr(n, r)
  fact(n) / (fact(r) * fact(n - r))
end

print "Enter number of rows: "
n = gets.to_i

(0...n).each do |i|
  print " " * (n - i)
  (0..i).each do |j|
    print "#{ncr(i, j)} "
  end
  puts
end
