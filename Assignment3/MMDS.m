clear all;
close all;
clc;
mun_data = load('input data/mun_data.dat');
mun_names = importdata('input data/mun_names.dat');
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
hold on
plot(dissimilarities,distances_mmds,'ro')%, ...
%[0 max(dissimilarities)],[0 max(dissimilarities)],'y.-');
xlabel('Dissimilarities'); ylabel('Distances')

distances_sammon = pdist(sammon);
plot(dissimilarities,distances_sammon,'go', ...
[0 max(dissimilarities)],[0 max(dissimilarities)],'k.-');
legend('MMDS','Sammon','location','best');
hold off
print('shepard_mmds_sammon_comparison','-dpng')






