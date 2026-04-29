function params = fitModel(t, BGP)

model = @(p,t) p(1)*(exp(-p(2)*t) - exp(-p(3)*t));

p0 = [100 1 0.1];
lb = [0 0 0];
ub = [1000 10 10];

options = optimoptions('lsqcurvefit','Display','off');

params = lsqcurvefit(model, p0, t, BGP, lb, ub, options);

end
