將final_project_1100915與my_robot_1100915_description資料夾放到/catkin_ws/src

開啟終端機1並輸入 #切至catkin_ws
            
    cd ~/catkin_ws
終端機1輸入 #建置套件
    
    catkin_make
終端機1輸入
    
    roslaunch final_project_1100915 ros_1100915.launch 
等待gazebo完全啟動

開啟終端機2輸入

    roslaunch final_project_1100915 navigation.launch
就能夠看見gazebo上機器人移動由原點依序到A B C點
