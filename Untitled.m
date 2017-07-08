x=(-4:1:4);
y=(-4:1:4);
z=zeros(9);
for i=1:9
    for j=1:9
        xx=i-5
        xy=j-5
        z(i,j)=2*xx^2-xx^4+xx^6/6+xx*xy+xy^2/2
    end
end
surf(x,y,z)
hold on