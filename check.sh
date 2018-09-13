#!/bin/bash
URL="http://django-psql-example-gxytest-jenkins.swgz.tae.ctyun.cn/health"
CODE=`curl -I -m 10 -o /dev/null -s -w %{http_code} ${URL}`
if  [ $CODE -eq 200 ]
 then
  echo "SUCCESS"
 else
  echo "FAILED"
  return 1
fi
