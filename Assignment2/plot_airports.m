% Colors for airports; values must be between 0 and 1
n = 255;
colors(1, :) = [0, 0, 0] / n;
colors(2, :) = [100.7301107362861, 62.40505837223183, 0] / n;
colors(3, :) = [200.9271221602317, 129.13902239980374, 0] / n;
colors(4, :) = [255, 202.96975332400476, 0] / n;

% Load files
load airports_loc.txt;
% Textread is buggy on some MATLAB versions, use textscan instead
fid = fopen('airports_names.txt');
C = textscan(fid, '%f%f%s');
fclose(fid);
nx = C{1};
ny = C{2};
names = C{3};

% Open new figure
figure;
hold on;

for i = 1:266
    line([nx(i), airports_loc(i, 2)], [ny(i), airports_loc(i, 3)], 'color', colors(airports_loc(i, 1), :));
    % Draw a white rectangle of size of the label
    text(nx(i), ny(i), names{i}, 'HorizontalAlignment', 'center', 'Margin', 0.1, 'BackgroundColor', 'white', 'Color', 'white');
end

colormap(colors);
scatter(airports_loc(:, 2), airports_loc(:, 3), 20, airports_loc(:, 1), 'filled');


for i = 1:266
    text(nx(i), ny(i), names{i}, 'HorizontalAlignment', 'center', 'color', colors(airports_loc(i, 1), :));
end
