FROM ros:jazzy

ARG USERNAME=USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Delete existing user with the same UID if present (e.g. "ubuntu" on noble)
RUN if id -u $USER_UID >/dev/null 2>&1; then userdel $(id -un $USER_UID); fi

# Create the user and add sudo support
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install common system utilities and ROS 2 Jazzy dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    lsb-release \
    build-essential \
    cmake \
    git \
    wget \
    locales \
    python3-pip \
    python3-colcon-common-extensions \
    && apt-get clean

# Add ROS 2 repository and GPG key for Jazzy
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - \
    && echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list \
    && apt-get update

# Install ROS 2 Jazzy packages and development tools
RUN apt-get install -y \
    ros-jazzy-ros-base \
    ros-jazzy-demo-nodes-cpp \
    ros-jazzy-rqt-graph \
    ros-dev-tools \
    ros-jazzy-rviz2 \
    && apt-get clean

# Add ROS setup to the user's bashrc
RUN echo "source /opt/ros/jazzy/setup.bash" >> /home/$USERNAME/.bashrc
RUN echo "source install/setup.bash" >> /home/$USERNAME/.bashrc

# Set bash as the default shell
ENV SHELL=/bin/bash

# Set user to the created user
USER $USERNAME

# Default command to run when the container starts
CMD ["/bin/bash"]