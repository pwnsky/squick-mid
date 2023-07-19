# Squick中台

The middleground of squick project
Squick 中台，嵌入了游戏GM和Grafana

采用Go的Gin框架来开发

集成了Mysql、Redis、Mongo



Grafana搭建

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