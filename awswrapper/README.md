awswrapper - AWS API Wrapper
========================

AWS API Wrapper

Usage
-----

It will look into your aws credentials file

Import the ec2wrapper

    >>> from awswrapper import ec2wrapper

Use describe functions for talk to aws

    >>> ec2wrapper.describe_all_running_instances()
    >>> ec2wrapper.describe_all_stopped_instances_with_tag(tag)
    >>> ec2wrapper.describe_all_running_instances_with_tag_and_value(tag, value)

This will return a regular EC2 Response

    >>> print aws.myaws
    aws > myaws
      Type: <class 'awsom.config.AccountEntity'>
      Attributes:
        .access_key_id = "xxxxxxxxxxxxxxxxxxxx"
        .name = "myaws"
        .secret_access_key = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
      Methods:
        .add_attr()
        .find()
      Children (1):
        ['ec2']

So far we only have access to some ec2 instance info, you can print your instance list

    >>> print aws.myaws.ec2.instances
    aws > myaws > ec2 > instances
      Type: <class 'awsom.services.ec2.EC2InstancesRootEntity'>
      Attributes:
        .name = "instances"
      Methods:
        .add_attr()
        .find()
      Children (2):
        ['i_xxxxxxxx']
        ['i_yyyyyyyy']

And some info about some instance:

    >>> print aws.myaws.ec2.instances.i_xxxxxxxx
    aws > myaws > ec2 > instances > i_xxxxxxxx
      Type: <class 'awsom.services.ec2.EC2InstanceEntity'>
      Attributes:
        .architecture = x86_64
        .dns_name = ec2-xx-yy-zz-ccc.compute-1.amazonaws.com
        .id = i-xxxxxxxx
        .instance_type = m1.large
        .name = i_xxxxxxxx
        .private_ip_address = 10.xxx.yyy.ccc
        .region = RegionInfo:us-east-1
        .tags = {}
      Methods:
        .add_attr()
        .find()
        .get_console_output()
      Children (0):

Another thing to try:

    >>> for i in aws.myaws.ec2.instances: print aws.myaws.ec2.instances[i]
