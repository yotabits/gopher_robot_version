from sys_packages import get_system_packages
from ros_packages import  get_ros_packages
import writer


def prepare_string():
    system_dict = get_system_packages()
    result = ""
    ros_dict_devel = get_ros_packages("/opt/yujin/amd64/indigo-devel")
    ros_dict_stable = get_ros_packages("/opt/yujin/amd64/indigo-stable")
    ros_dict_base = get_ros_packages("/opt/ros")
    result += writer.dict_to_str(system_dict,"SYSTEM PACAKGES")
    result += writer.dict_to_str(ros_dict_devel,"YUJIN_DEVEL")
    result += writer.dict_to_str(ros_dict_stable,"YUJIN STABLE")
    result += writer.dict_to_str(ros_dict_base, "ROS INTERNAL")
    print result


prepare_string()