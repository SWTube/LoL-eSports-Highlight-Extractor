"""
#   File Name: cut_not_inGame.py
#        Team: standardization
#  Programmer: tjswodud
#  Start Date: 07/07/20
# Last Update: September 28, 2020
#     Purpose: Full video of LCK will be given in this program.
#              And compare frame and compare_image (minimap, pause, upperleft banner) per frame, using sift_algorithm.
#              (if it success for compare, that frame is ingame, if not, that frame is not ingame.)
#              Finally, this program will return edited video, except for frame that is not ingame.
"""

import cognition_inGame as ingame
import cv2 as cv
import os
import searching_upperleft_banner as upperleft
import time

start_time = time.time()

# in Windows OS
# resource_path = "E:/video/resources"
# output_path = "E:/video/outputs"

# in Ubuntu OS
resource_path = "/media/cogongnam/f8447e77-84e5-43a2-a0f0-e1b1977f1322/video/resources"
output_path = "/media/cogongnam/f8447e77-84e5-43a2-a0f0-e1b1977f1322/video/outputs"
replay_banner_path = "../resources/replay_banner.png"
replay_banner = upperleft.resource(replay_banner_path)
highlight_banner_path = "../resources/highlight.png"
highlight_banner = upperleft.resource(highlight_banner_path)
pro_view_banner_path = "../resources/pro view.png"
pro_view_banner = upperleft.resource(pro_view_banner_path)

video_list = os.listdir(resource_path)
template_image = cv.imread("../resources/minimap_templ.png", cv.COLOR_BGR2GRAY)
pause_image = cv.imread("../resources/pause_image.png", cv.COLOR_BGR2GRAY)

compare_images = []
compare_images.append(replay_banner)
compare_images.append(highlight_banner)
compare_images.append(pro_view_banner)

video_num = 1
for video_file in video_list:
    new_video_path = resource_path + '/' + video_file
    video_capture = ingame.create_capture(new_video_path)
    print('[No.{} video is editing...]'.format(video_num))
    ingame.match_template(video_capture, template_image, pause_image, compare_images, video_file, output_path)
    video_num += 1

end_time = time.time()
exe_time = round((end_time - start_time), 1)
print('time : {} s.'.format(exe_time))