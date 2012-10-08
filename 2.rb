fibs = [1, 1, 2]
sum = 0

while fibs.last < 4_000_000 do

  if fibs.last.even?
    sum += fibs.last
  end

  fibs << (fibs[-2] + fibs[-1])

  fibs.shift
end

puts sum
