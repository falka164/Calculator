# Calculator
Basic calculator app which demonstrate of using Continuous Integration with CircleCI as a integration service.

On branch dockerImage are Dockerfile and upgraded circleCI config file, which should allow to create docker image throug CircleCI pipline.  But at this point my current circleci plan doesn't include Docker Layer Caching, so I'm not sure if it works :)


On branch onlyDocker are files necessary to build docker image without ussing CircleCI. Built image is avalible on https://hub.docker.com/repository/docker/falka164/calc-repo
