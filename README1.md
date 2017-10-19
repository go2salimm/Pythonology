# Elasticsearch/Logstash/Kibana stack
https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html
https://www.elastic.co/guide/index.html

https://www.elastic.co/guide/en/kibana/5.6/index.html
https://www.elastic.co/downloads/logstash
https://www.elastic.co/guide/en/kibana/5.6/connect-to-elasticsearch.html

C:\Program Files\Elastic\Elasticsearch\bin>elasticsearch.exe -Ecluster.name=my_first_cluster -Enode.name=my_first_node

we can actually see a pattern of how we access data in Elasticsearch. That pattern can be summarized as follows:
<REST Verb> /<Index>/<Type>/<ID>



C:\>curl -XPOST 127.0.0.1:9200/bank/account/_bulk?pretty --data-binary @accounts.json

http://127.0.0.1:5601/app/kibana#/visualize?_g=()
C:\Program Files\Elastic\Elasticsearch\bin>
C:\kibana-5.6.3-windows-x86\kibana-5.6.3-windows-x86\bin>


To test your Logstash installation, run the most basic Logstash pipeline. For example:

In setup.bat add the following lines
notepad logstash-5.6.3\bin\setup.bat

set JAVA_HOME=C:\Program Files\Java\jre1.8.0_144
set PATH=C:\Program Files\Java\jre1.8.0_144\bin

cd logstash-5.6.3
bin/logstash -e 'input { stdin { } } output { stdout {} }'


Open a PowerShell prompt as an Administrator (right-click the PowerShell icon and select Run As Administrator). 
If you are running Windows XP, you may need to download and install PowerShell.
From the PowerShell prompt, run the following commands to install Filebeat as a Windows service:

PS > cd 'C:\Program Files\Filebeat'
PS C:\Program Files\Filebeat> .\install-service-filebeat.ps1

Note:
If script execution is disabled on your system, you need to set the execution policy for the current session to allow
the script to run. For example: PowerShell.exe -ExecutionPolicy UnRestricted -File .\install-service-filebeat.ps1.


To start services :

Salim@WIN-0DL46PEHHT9 C:\elasticsearch-5.6.3\bin
> elasticsearch.exe -Ecluster.name=my_first_cluster -Enode.name=my_first_node

[2017-10-19T16:01:47,536][INFO ][o.e.t.TransportService   ] [my_first_node] publish_address {127.0.0.1:9300}, bound_addresses {127.0.0.1:9300}, {[::1]:9300}
[2017-10-19T16:01:50,624][INFO ][o.e.c.s.ClusterService   ] [my_first_node] new_master {my_first_node}{MfyrhP3eT82DZC9RRi9Z_g}{Ajo9yZgkSEa3c58x_SrHQA}{127.0.0.1}{127.0.0.1:9300}, reason: zen-disco-elected-as-master ([0] nodes joined)
[2017-10-19T16:01:52,109][INFO ][o.e.h.n.Netty4HttpServerTransport] [my_first_node] publish_address {127.0.0.1:9200}, bound_addresses {127.0.0.1:9200}, {[::1]:9200}
[2017-10-19T16:01:52,111][INFO ][o.e.n.Node               ] [my_first_node] started
[2017-10-19T16:01:52,334][INFO ][o.e.g.GatewayService     ] [my_first_node] recovered [7] indices into cluster_state
[2017-10-19T16:01:54,878][INFO ][o.e.c.r.a.AllocationService] [my_first_node] Cluster health status changed from [RED] to [YELLOW] (reason: [shards started [[.kibana][0]] ...]).


Salim@WIN-0DL46PEHHT9 C:\kibana-5.6.3\bin                                                                                                               
> kibana.bat                                                                                                                                            
  log   [20:03:26.912] [info][status][plugin:kibana@5.6.3] Status changed from uninitialized to green - Ready                                           
  log   [20:03:26.996] [info][status][plugin:elasticsearch@5.6.3] Status changed from uninitialized to yellow - Waiting for Elasticsearch               
  log   [20:03:27.034] [info][status][plugin:console@5.6.3] Status changed from uninitialized to green - Ready                                          
  log   [20:03:27.050] [info][status][plugin:metrics@5.6.3] Status changed from uninitialized to green - Ready                                          
  log   [20:03:27.446] [info][status][plugin:timelion@5.6.3] Status changed from uninitialized to green - Ready                                         
  log   [20:03:27.528] [info][listening] Server running at http://localhost:5601                                                                        
  log   [20:03:27.530] [info][status][ui settings] Status changed from uninitialized to yellow - Elasticsearch plugin is yellow                         
  log   [20:03:27.987] [info][status][plugin:elasticsearch@5.6.3] Status changed from yellow to green - Kibana index ready                              
  log   [20:03:27.989] [info][status][ui settings] Status changed from yellow to green - Ready                                                          
                                                                                                                                                        
    
Salim@WIN-0DL46PEHHT9 C:\filebeat-5.6.3
> .\filebeat -e -c filebeat.yml -d "publish"
2017/10/19 20:04:54.747605 beat.go:297: INFO Home path: [C:\filebeat-5.6.3] Config path: [C:\filebeat-5.6.3] Data path: [C:\filebeat-5.6.3\data] Logs path: [C:\filebeat-5.6.3\logs]
2017/10/19 20:04:54.747605 beat.go:192: INFO Setup Beat: filebeat; Version: 5.6.3
2017/10/19 20:04:54.747605 publish.go:228: WARN Support for loading more than one output is deprecated and will not be supported in version 6.0.
2017/10/19 20:04:54.747605 output.go:258: INFO Loading template enabled. Reading template file: C:\filebeat-5.6.3\filebeat.template.json
2017/10/19 20:04:54.749605 output.go:269: INFO Loading template enabled for Elasticsearch 2.x. Reading template file: C:\filebeat-5.6.3\filebeat.template-es2x.json
2017/10/19 20:04:54.750605 output.go:281: INFO Loading template enabled for Elasticsearch 6.x. Reading template file: C:\filebeat-5.6.3\filebeat.template-es6x.json
2017/10/19 20:04:54.752605 client.go:128: INFO Elasticsearch url: http://127.0.0.1:9200
2017/10/19 20:04:54.752605 outputs.go:108: INFO Activated elasticsearch as output plugin.
2017/10/19 20:04:54.752605 logstash.go:90: INFO Max Retries set to: 3
2017/10/19 20:04:54.752605 outputs.go:108: INFO Activated logstash as output plugin.
2017/10/19 20:04:54.752605 publish.go:243: DBG  Create output worker
2017/10/19 20:04:54.752605 publish.go:243: DBG  Create output worker    


Salim@WIN-0DL46PEHHT9 C:\logstash-5.6.3\bin
> logstash -f first-pipeline.conf --config.reload.automatic 
'findstr' is not recognized as an internal or external command, operable program or batch file.
Sending Logstash's logs to C:/logstash-5.6.3/logs which is now configured via log4j2.properties
[2017-10-19T16:07:45,654][INFO ][logstash.modules.scaffold] Initializing module {:module_name=>"fb_apache", :directory=>"C:/logstash-5.6.3/modules/fb_apache/configuration"}
[2017-10-19T16:07:45,671][INFO ][logstash.modules.scaffold] Initializing module {:module_name=>"netflow", :directory=>"C:/logstash-5.6.3/modules/netflow/configuration"}
[2017-10-19T16:07:46,716][INFO ][logstash.pipeline        ] Starting pipeline {"id"=>"main", "pipeline.workers"=>1, "pipeline.batch.size"=>125, "pipeline.batch.delay"=>5, "pipeline.max_inflight"=>125}
[2017-10-19T16:07:47,475][INFO ][logstash.inputs.beats    ] Beats inputs: Starting input listener {:address=>"0.0.0.0:5043"}
[2017-10-19T16:07:47,560][INFO ][org.logstash.beats.Server] Starting server on port: 5043
[2017-10-19T16:07:47,568][INFO ][logstash.pipeline        ] Pipeline main started
[2017-10-19T16:07:47,718][INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9600}                                                                                                                                            