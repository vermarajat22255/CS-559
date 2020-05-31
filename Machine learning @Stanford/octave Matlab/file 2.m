v = [1:10]
for i = 1:10
  v(i) = 2^i;
end

display(v)

i = 1;
while true,
  if v(i) < 500
    v(i) = 500;
  else
    break;
  end;
  i = i+1;
end;