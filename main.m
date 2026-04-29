clear; clc;

% Carica dati
data = readtable('../data/glucose_data.txt');

patients = unique(data.paziente);
nPaz = length(patients);

results = [];

for i = 1:nPaz
    
    idx = data.paziente == patients(i);
    
    t = data{idx,2}; % tempo
    gluc = data{idx,3}; % glucosio
    
    baseline = gluc(1);
    BGP = gluc - baseline;
    
    % FIT PARAMETRI
    params = fitModel(t, BGP);
    
    % SIMULAZIONE
    [t_sim, gluc_sim] = simulateCurve(params, baseline);
    
    % METRICHE
    metrics = computeMetrics(t_sim, gluc_sim, baseline);
    
    % SALVA RISULTATI
    results = [results; patients(i), params, metrics];
    
    % PLOT (solo primi 3)
    if i <= 3
        figure;
        scatter(t, gluc, 'filled'); hold on;
        plot(t_sim, gluc_sim, 'LineWidth',2);
        xlabel('Time (h)');
        ylabel('Glucose (mg/dL)');
        title(['Patient ', num2str(patients(i))]);
        legend('Data','Model');
    end
    
end
% Tabella finale
results_table = array2table(results, ...
    'VariableNames', {'Patient','A','a','b','AUC','Cmax','Tmax','Treturn'});

writetable(results_table, '../results/results.csv');

disp(results_table);
