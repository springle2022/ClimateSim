from library_files import trendline
import os
path_to_here = os.path.dirname(__file__)


year, levels = trendline.get_data(path_to_here+"\data\Carbon_Dioxide_Post_Industrial.txt") 
print(year, levels)