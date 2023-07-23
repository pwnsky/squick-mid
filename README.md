# Squick中台



## 介绍

squick-mid是Squick项目的中台项目，中台在网络游戏中充当很重要的角色，它可以让我们知道该游戏背后的运营数据，能够实时的掌握该游戏的数据情况。

本次项目采用Vue3来开发后台前端，Go的Gin框架来开发后端，定时向squick游戏服务器获取游戏数据，采用后台实时监控游戏各个服务器节点状态玩家数据，通过Grafana实时的将数据展示出来。





## 项目进展

管理Squick服务状态 【进行中】

集成 Mysql、Redis、MongoDB 【进行中】

集成 Grafana 【进行中】

集成GM 【进行中】





## 搭建





### 数据库搭建





### 后端编译





### Grafana搭建

```bash
#!/bin/bash
docker run -d \
    --restart=always \
    --name grafana_1 \
    -p 3600:3000 \
    -v $(pwd)/data:/var/lib/grafana/ \
    -v $(pwd)/conf:/etc/grafana/ \
    grafana/grafana
```





### 前端渲染

