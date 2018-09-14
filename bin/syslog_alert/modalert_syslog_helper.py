
# encoding = utf-8
import logging
import logging.handlers

def process_event(helper, *args, **kwargs):
    """
    # IMPORTANT
    # Do not remove the anchor macro:start and macro:end lines.
    # These lines are used to generate sample code. If they are
    # removed, the sample code will not be updated when configurations
    # are updated.

    [sample_code_macro:start]

    # The following example gets the alert action parameters and prints them to the log
    syslog_server = helper.get_param("syslog_server")
    helper.log_info("syslog_server={}".format(syslog_server))

    port = helper.get_param("port")
    helper.log_info("port={}".format(port))

    field_list = helper.get_param("field_list")
    helper.log_info("field_list={}".format(field_list))


    # The following example adds two sample events ("hello", "world")
    # and writes them to Splunk
    # NOTE: Call helper.writeevents() only once after all events
    # have been added
    helper.addevent("hello", sourcetype="sample_sourcetype")
    helper.addevent("world", sourcetype="sample_sourcetype")
    helper.writeevents(index="summary", host="localhost", source="localhost")

    # The following example gets the events that trigger the alert
    events = helper.get_events()
    for event in events:
        helper.log_info("event={}".format(event))

    # helper.settings is a dict that includes environment configuration
    # Example usage: helper.settings["server_uri"]
    helper.log_info("server_uri={}".format(helper.settings["server_uri"]))
    [sample_code_macro:end]
    """

    helper.log_info("Alert action syslog started.")
    syslog_server = helper.get_param("syslog_server")
    helper.log_info("syslog_server={}".format(syslog_server))

    port = helper.get_param("port")
    helper.log_info("port={}".format(port))

    #proto = helper.get_param("proto")
    #helper.log_info("proto={}".format(proto))
    
    #syslog_version = helper.get_param("syslog_version")
    #helper.log_info("syslog_version={}".format(syslog_version))
    
    #level_field = helper.get_param("level_field")
    #helper.log_info("level_field={}".format(level_field))
    
    field_list = helper.get_param("field_list")
    helper.log_info("field_list={}".format(field_list))
    
    #facility = helper.get_param("facility")
    #helper.log_info("facility={}".format(facility))

    #priority = helper.get_param("priority")
    #helper.log_info("priority={}".format(priority))
    
    syslog_out = logging.handlers.SysLogHandler(address=(str(syslog_server), int(port)), facility="user")
    syslog_out.setFormatter(logging.Formatter('%(name)s %(levelname)s %(message)s'))

    syslog = logging.getLogger('syslog')
    syslog.setLevel(logging.DEBUG)
    syslog.addHandler(syslog_out)
    
    #syslog.debug('foo syslog message')
    events = helper.get_events()
    for event in events:
        output = []
        helper.log_info("event={}".format(event))
        for key in event:
            helper.log_info("key={}".format(key))
        if field_list:
            for field in field_list.split(","):
                cleaned_field = field.strip()
                helper.log_info("field={}".format(cleaned_field))
                
                if event.has_key(cleaned_field):
                    
                    output.append('%s="%s"' % (cleaned_field, event[cleaned_field]))
            
            syslog.info(" ".join(output))
        else:
            syslog.info(event)

    # TODO: Implement your alert action logic here
    return 0
    
    
    
    
    
    
    
    
