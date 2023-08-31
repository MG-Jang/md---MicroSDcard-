#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
import numpy as np
import math

from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from geometry_msgs.msg import PoseArray, Pose

# import matplotlib.pyplot as plt
# import matplotlib as mpl
from sklearn.cluster import DBSCAN

# lidar_velodyne_cluster 는 LiDAR의 Point들을 물체 단위로 구분하는 Clustering 예제입니다.
# PointCloud Data를 입력받아 DBSCAN Algorithm을 활용하여 Clustering을 수행합니다.
# 교육생분들은 DBSCAN의 Parameter를 조절하여 적절한 Clustering 결과를 얻어내야 합니다.

# 노드 실행 순서
# 1. DBSCAN Parameter 입력
# 2. 각 Cluster를 대표하는 위치 값 계산
# 3. PointCloud Data로부터 Distance, Angle 값 계산


class SCANCluster:
    def __init__(self):

        self.scan_sub = rospy.Subscriber("/lidar3D", PointCloud2, self.callback)

        self.cluster_pub = rospy.Publisher("/clusters", PoseArray, queue_size=10)

        self.pc_np = None

        # TODO: (1) DBSCAN Parameter 입력
        '''
        # DBSCAN의 Parameter를 결정하는 영역입니다.
        # sklearn.cluster의 DBSCAN에 대해 조사하여 적절한 Parameter를 입력하기 바랍니다.

        self.dbscan = DBSCAN( , , ...)
        '''
        '''
        dbscan(density-based spatial clustering of applicaition with noise)
        밀도 기반 데이터 클러스터링 알고리즘
        min_samples : 핵심 포인트를 중심점으로 간주하는 주변 지역의 표본 수
        eps : 핵심 포인트를 중심으로 측정되는 유클리디언 거리값
        dense region : 특정 공간에서 데이터가 붐비는 지역
        핵심 샘플 : eps 거리 안에 데이터가 지정한 min_samples 개수를 만족 시키는 밀집 지역에 있는 데이터 포인트
        noise : eps 거리 안에 들어오는 포인트 수가 지정한 min_sample 보다 적을 경우 잡음으로 레이블
        '''
        self.dbscan = DBSCAN(eps=0.8, min_samples=30)
        '''
        1. 특성 공간에서 데이터가 붐비는 밀집 지역을 찾고 그 범위 안에서 핵심 샘플이 될 포인트를 지정한다
        2. 어느 데이터 포인트에서 eps 거리 안에 데이터가 min_samples 개수 만큼 들어 있으면
        이 데이터 포인트를 핵심 샘플로 지정한다.
        이 경우 해당 데이터 포인트는 새로운 클러스터 레이블로 할당된다.(개수 만족 못하면 잡음)
        3. 새롭게 할당된 핵심 샘플로부터 eps 거리 안의 포인트가 만약 어떤 클러스터에도 포함되지 않으면
        해달 클러스터 레이블로 할당시킨다. (만약 핵심 샘플이면 그 포인트의 이웃을 차례로 방문)
        4. 1~3을 반복하며 eps 거리 안에 더 이상 핵심 샘플이 없을 때까지 자란다. 
        '''

    def callback(self, msg):
        self.pc_np = self.pointcloud2_to_xyz(msg)
        
        if len(self.pc_np) == 0:

            cluster_msg = PoseArray()

        else:
            pc_xy = self.pc_np[:,:2]
            # print(pc_xy)
            db = self.dbscan.fit_predict(pc_xy)
            # print(db)
            n_cluster = np.max(db) + 1
            # print(n_cluster)
            cluster_msg = PoseArray()

            # cluster_list = []
            # cluster_list.append(db)
            # print(cluster_list)
            for cluster in range(n_cluster):
                # print(np.where(db==cluster))
                idx = np.where(db==cluster)[0][0]                
                # TODO: (2) 각 Cluster를 대표하는 위치 값 계산
                '''
                # DBSCAN으로 Clustering 된 각 Cluster의 위치 값을 계산하는 영역입니다.
                # Cluster에 해당하는 Point들을 활용하여 Cluster를 대표할 수 있는 위치 값을 계산합니다.
                # 계산된 위치 값을 ROS geometry_msgs/Pose type으로 입력합니다.
                # Input : cluster
                # Output : cluster position x,y   

                tmp_pose=Pose()
                #tmp_pose.position.x = 
                #tmp_pose.position.y = 
                '''
                # print(cluster)
                tmp_pose = Pose()
                tmp_pose.position.x = pc_xy[idx][0]  # 대표하는 좌표
                tmp_pose.position.y = pc_xy[idx][1]
                # print(tmp_pose)
                cluster_msg.poses.append(tmp_pose)

        self.cluster_pub.publish(cluster_msg)

    def pointcloud2_to_xyz(self, cloud_msg):

        point_list = []

        for point in pc2.read_points(cloud_msg, skip_nans=True):
            # TODO: (3) PointCloud Data로부터 Distance, Angle 값 계산
            '''
            # LiDAR의 PointCloud Data로부터 Distance와 Angle 값을 계산하는 영역입니다.
            # 각 Point의 XYZ 값을 활용하여 Distance와 Yaw Angle을 계산합니다.
            # Input : point (X, Y, Z, Intensity)            

            dist = 
            angle = 
            '''
            # print(point)
            # print(point)
            pt_x = point[0]
            pt_y = point[1]
            pt_z = point[2]

            dist = math.sqrt(pt_x**2+pt_y**2+pt_z**2)  # 거리
            angle = math.atan2(pt_y,pt_x)  # yaw angle

            if pt_x > 2.7 and pt_y > -10 and pt_y < 10 and dist < 60 and dist > 1:
                point_list.append((pt_x, pt_y, pt_z, point[3], dist, angle))

        point_np = np.array(point_list, np.float32)
        # print(point_np)
        return point_np


if __name__ == '__main__':

    rospy.init_node('velodyne_clustering', anonymous=True)

    scan_cluster = SCANCluster()

    rospy.spin()
