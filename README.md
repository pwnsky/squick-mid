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





### 监控搭建

InfluxDB





influxDB

```
docker run -d --name influxdb -p 8086:8086 influxdb
```

访问: http://127.0.0.1:8086/ 设置密码和创建数据库



grafana

```
docker run -d --name grafana -p 3000:3000 grafana/grafana
```

访问 http://127.0.0.1:3000 输入admin和admin，然后设置密码



statsd

```
docker run -d --name statsd -p 3000:3000 statsd/statsd
```

客户端: https://github.com/alexcesaro/statsd











### 前端渲染





## 参考

[Statsd+Graphite+Grafana：搭建web监控系统](https://www.cnblogs.com/-wenli/p/13661292.html)

[使用 StatsD + Grafana + InfluxDB 搭建 Node.js 监控系统](https://juejin.cn/post/6844903457422327816)

https://blog.csdn.net/hogwarts_ziqi/article/details/128472305

https://zhuanlan.zhihu.com/p/80062750
