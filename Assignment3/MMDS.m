clear all;
close all;
clc;
mun_data = load('mun_data.dat');
mun_names = importdata('mun_names.dat');
dissimilarities = pdist(mun_data);
[metric_mds,~,disparities_mmds] = mdscale(dissimilarities,2,'Criterion','metricstress');
[sammon,~,disparities_sammon] = mdscale(dissimilarities,2,'Criterion','sammon');

figure()
hold on
plot(metric_mds(:,1),metric_mds(:,2),'bo');
plot(sammon(:,1),sammon(:,2),'r*');
N = 5;
text(metric_mds(1:N:length(metric_mds),1),metric_mds(1:N:length(metric_mds),2),mun_names(1:N:length(metric_mds)));
text(sammon(1:N:length(sammon),1),sammon(1:N:length(sammon),2),mun_names(1:N:length(sammon)));
legend('mmds','sammon')
hold off
print('mmds_sammon','-dpng')

distances_mmds = pdist(metric_mds);
figure()
plot(dissimilarities,distances_mmds,'bo', ...
[0 max(dissimilarities)],[0 max(dissimilarities)],'r.-');
xlabel('Dissimilarities'); ylabel('Distances')
title('Shepard plot using Metric MDS')
print('shepard_mmds','-dpng')

distances_sammon = pdist(sammon);
figure()
plot(dissimilarities,distances_sammon,'bo', ...
[0 max(dissimilarities)],[0 max(dissimilarities)],'r.-');
xlabel('Dissimilarities'); ylabel('Distances')
title('Shepard plot using Sammon mapping')
print('shepard_sammon','-dpng')





