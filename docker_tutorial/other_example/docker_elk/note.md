curl -XPOST -D- "http://localhost:5601/api/saved_objects/index-pattern" \
    -H "Content-Type: application/json" \
    -H "kbn-version: 6.1.0" \
    -d '{"attributes":{"title":"logstash-*","timeFieldName":"@timestamp"}}'
