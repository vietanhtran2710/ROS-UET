# CÀI ĐẶT ROS 2 FOXY
## Giới thiệu
Hướng dẫn cài đặt sau đây được tổng hợp từ 2 đường dẫn:
- https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html (Cài đặt chính cho ROS 2 Foxy)
- https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup (Cài đặt các gói riêng biệt để thực hành TurtleBot 3)

Toàn bộ công việc cài đặt được thực hiện trên hệ điều hành **Ubuntu 20.04 LTS**, sinh viên cài hệ điều hành này trong máy để thực hành hoặc chạy máy ảo. Dung lượng ổ cứng tối thiểu nên là 30GB.
Link ISO cho Ubuntu 20.04 LTS:
- https://ubuntu.com/download/desktop

## Cài đặt ROS 2 FOXY qua Debian Packages
### 1. Cài đặt Locale
Locale là tập hợp các biến môi trường của hệ điều hành, định nghĩa ngôn ngữ và khu vực của người dùng. Để sử dụng ROS ta cần đảm bảo đã đặt ngôn ngữ là tiếng Anh hỗ trợ bảng mã UTF-8 bằng các lệnh sau:
```sh
locale  # kiểm tra xem đã đặt UTF-8 hay chưa
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
locale  # Xác nhận lại kết quả cài đặt 
```

### 2. Lấy mã nguồn
Ta cần có mã nguồn của ROS để thực hiện cài đặt. Lấy nơi lưu trữ mã nguồn từ Github về bằng **2 lệnh**  sau:
```sh
sudo apt update && sudo apt install curl gnupg2 lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
```
Sau đó thêm mã vào danh sách nguồn của hệ thống bằng **1 lệnh** sau:
```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### 3. Cài đặt các gói chính cho ROS 2
Cập nhật kho lưu trữ apt:
```sh
sudo apt update
```
Cài đặt phiên bản đầy đủ (Desktop) của ROS: chứa RVIz, demo và hướng dẫn:
```sh
sudo apt install ros-foxy-desktop
```

### 4. Cài đặt các gói độc lập của ROS 2 và Turtlebot3
```sh
sudo apt-get install ros-foxy-gazebo-* # Cài đặt Gazebo 11
sudo apt install ros-foxy-cartographer # Cài đặt Cartographer
sudo apt install ros-foxy-cartographer-ros
sudo apt install ros-foxy-navigation2 # Cài đặt Navigation2
sudo apt install ros-foxy-nav2-bringup
```
Sau đó ta cài đặt các gói của Turtlebot3 
```sh
source ~/.bashrc
sudo apt install ros-foxy-dynamixel-sdk
sudo apt install ros-foxy-turtlebot3-msgs
sudo apt install ros-foxy-turtlebot3
```

### 5. Thiết lập môi trường
Ta phải chạy lệnh sau trên mỗi một shell mới (1 cửa sổ terminal) để có thể truy cập vào những lệnh của ROS 2:
```sh
source /opt/ros/foxy/setup.bash
```
Để tiện hơn, ta sẽ thêm lệnh trên vào script **.bash.rc**, từ đó mỗi lần một shell mới được mở lệnh sẽ tự đông chạy, tiết kiệm thời gian hơn.
```sh
echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
```
Để tiện lợi di chuyển giữa các thư mục làm việc của nhiều dự án, ta thêm colcon_cd vào start up script như sau:
```sh
echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
echo "export _colcon_cd_root=~/ros2_workspace" >> ~/.bashrc # Lệnh có thể thay đổi
```
Lệnh thứ 2 có thể thay đổi tùy theo thư mục workspace của mỗi sinh viên sẽ tạo sau này, ta thay *~/ros2_workspace* bằng đường dẫn tới thư mục chứa các dự án.
Tiếp ta đặt **ROS_DOMAIN_ID** cho hệ thống. ROS sử dụng **ROS_DOMAIN_ID** để chia mạng cục bộ, các máy tính có cùng ROS_DOMAIN_ID sẽ có thể kết nối được với nhau qua ROS. Lớp có 2 robot Turtlebot3 mang 2 ID **30** và **31**. Tùy vào ID được phân, sinh viên gán đúng ID đó vào hệ thống bằng lệnh sau:
```sh
echo "export ROS_DOMAIN_ID=<ID được phân cho sinh viên>" >> ~/.bashrc # 30 hoặc 31 
```
Cuối cùng ta định nghĩa mẫu Turtlebot3 sẽ sử dụng để có thể chạy các gói, mẫu của 2 robot là **burger**
```sh
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
```
### 6. Kiểm tra
Sau khi đã thêm tất cả các lệnh trên vào file */.bashrc*, ta source lại file script:
```sh
source ~/.bashrc
```
Kiểm tra giá trị các biến môi trường:
```sh
printenv | grep -i ROS
```
Đầu ra của lệnh nên liêt kê các biến có giá trị như sau:
```
ROS_VERSION=2
ROS_PYTHON_VERSION=3
ROS_DISTRO=foxy
```
Cuối cùng ta chạy thử 2 node chứa publisher và subscriber liên lạc với nhau qua ROS. Mở 2 cửa sổ terminal và đặt 2 cửa sổ đó trên màn hình sao cho có thể tiện quan sát cả 2 cùng lúc. Tại cửa sổ đầu tiên, chạy:
```sh
ros2 run demo_nodes_cpp talker
```
Ở cửa sổ thứ 2 chạy: 
```sh
ros2 run demo_nodes_py listener
```
Nếu cải đặt đúng, cả 2 chương trình sẽ chạy ổn định và bên talker thông báo đang phát đi tin nhắn còn listener sẽ thông báo nghe được những tin nhắn đó. Đầu ra của 2 chương trình sẽ có định dạng như sau: 
```
[INFO] [1633924152.025729625] [talker]: Publishing: 'Hello World: 1'
[INFO] [1633924153.025731493] [talker]: Publishing: 'Hello World: 2'
[INFO] [1633924154.025732855] [talker]: Publishing: 'Hello World: 3'
[INFO] [1633924155.025839667] [talker]: Publishing: 'Hello World: 4'
[INFO] [1633924156.025780155] [talker]: Publishing: 'Hello World: 5'
```
```
[INFO] [1633924152.045882550] [listener]: I heard: [Hello World: 1]
[INFO] [1633924153.027236983] [listener]: I heard: [Hello World: 2]
[INFO] [1633924154.027201606] [listener]: I heard: [Hello World: 3]
[INFO] [1633924155.027304661] [listener]: I heard: [Hello World: 4]
[INFO] [1633924156.027329499] [listener]: I heard: [Hello World: 5]
```
Trên đây là một demo đầu tiên của ROS. 2 node liên lạc với nhau qua 1 topic, 1 node là publisher (phát tin nhắn) còn node còn lại là subscriber (lắng nghe tin nhắn). 2 node này đang chạy trong cùng 1 máy. Ở các bài sau node trên máy tính sẽ phát tin nhắn chứa mệnh lệnh cho node trên robot và robot sẽ hành động dựa vào nội dung những tin nhắn đó, đồng thời có thể gửi lại tin nhắn chứa dữ liệu thu thập được về máy tính.