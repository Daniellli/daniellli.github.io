
###
 # @Author: daniel
 # @Date: 2025-02-19 15:27:11
 # @LastEditTime: 2025-02-19 15:29:24
 # @LastEditors: daniel
 # @Description: 
 # @FilePath: /daniellli.github.io/run_resize.sh
 # have a nice day
### 

set -e 
set -x 


img_path=assets/resized/prof_pic-chongqing-4.jpg
ratio=0.15



python resize.py --src ${img_path} --resize-ratio ${ratio}

