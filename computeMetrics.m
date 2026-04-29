function metrics = computeMetrics(t, gluc, baseline)

% AUC
AUC = trapz(t, gluc);

% Cmax e Tmax
[Cmax, idx] = max(gluc);
Tmax = t(idx);

% Tempo ritorno entro +5%
threshold = baseline * 1.05;

idx_return = find(gluc <= threshold & t > Tmax, 1);

if isempty(idx_return)
    Treturn = NaN;
else
    Treturn = t(idx_return);
end

metrics = [AUC, Cmax, Tmax, Treturn];

end
