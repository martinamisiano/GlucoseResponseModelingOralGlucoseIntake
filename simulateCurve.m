function [t_sim, gluc_sim] = simulateCurve(params, baseline)

model = @(p,t) p(1)*(exp(-p(2)*t) - exp(-p(3)*t));

t_sim = linspace(0,5,100);

BGP_sim = model(params, t_sim);
gluc_sim = baseline + BGP_sim;

end
