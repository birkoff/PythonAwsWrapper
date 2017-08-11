from awswrapper import ec2wrapper

# Tests


def test_get_instance_ids():
    instances_data = _get_ec2_instances_data()
    ec2_response = _generate_ec2_response(instances_data)
    instances_ids = ec2wrapper.get_instances_ids(ec2_instances=ec2_response)
    assert instances_ids[0] == instances_data[0]['InstanceId']
    assert instances_ids[1] == instances_data[1]['InstanceId']
    assert instances_ids[2] == instances_data[2]['InstanceId']
    assert instances_ids[3] == instances_data[3]['InstanceId']
    assert instances_ids[4] == instances_data[4]['InstanceId']


def test_get_instances_data():
    instances_data = _get_ec2_instances_data()
    ec2_response = _generate_ec2_response(instances_data)
    instances_ids = ec2wrapper.get_instances_data(ec2_instances=ec2_response)
    assert instances_ids[0]['InstanceId'] == 'instance-101'
    assert instances_ids[0]['Name'] == 'Instance Without Owner Tag'
    assert instances_ids[0]['Owner'] == ''

    assert instances_ids[1]['InstanceId'] == 'instance-202'
    assert instances_ids[1]['Name'] == 'Success-Instance-Owner'
    assert instances_ids[1]['Owner'] == 'Developer'


def test_get_tags_from_instance():
    # cover with test_get_instances_data
    pass


def test_list_instances_without_tag():
    instances_data = _get_ec2_instances_data()
    ec2_response = _generate_ec2_response(instances_data)
    tags_filter = get_tags_filter()
    instances = ec2wrapper.list_instances_without_tag(tags_filter, ec2_response)
    assert instances[0]['Name'] == 'Instance Without Owner Tag'
    assert instances[1]['Name'] == 'Instance With Wrong Tag Value'
    assert instances[2]['Name'] == 'Instance With Empty Tag Owner'
    assert len(instances) == 3


def _generate_ec2_response(ec2_instances_data):
    ec2_response = {
        "Reservations": [{
            'Instances': ec2_instances_data,
        }]
    }
    return ec2_response


def _get_ec2_instances_data():
    return [
        {
            'ImageId': 'image-101',
            'InstanceId': 'instance-101',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Instance Without Owner Tag'
                },
                {
                    'Key': 'AnotherRandomTag',
                    'Value': 'sdfdf-sdfsdf-sdfsdf'
                }
            ]
        },
        {
            'ImageId': 'image-202',
            'InstanceId': 'instance-202',
            'Tags': [
                {
                    'Key': 'Owner',
                    'Value': 'Developer'
                },
                {
                    'Key': 'Name',
                    'Value': 'Success-Instance-Owner'
                }
            ]
        },
        {
            'ImageId': 'image-303',
            'InstanceId': 'instance-303',
            'Tags': [
                {
                    'Key': 'product',
                    'Value': 'fusion-center'
                },
                {
                    'Key': 'Name',
                    'Value': 'Success-Instance-With-Tags'
                }
            ]
        },
        {
            'ImageId': 'image-404',
            'InstanceId': 'instance-404',
            'Tags': [
                {
                    'Key': 'product',
                    'Value': 'not-fusion-center'
                },
                {
                    'Key': 'Name',
                    'Value': 'Instance With Wrong Tag Value'
                }
            ]
        },
        {
            'ImageId': 'image-505',
            'InstanceId': 'instance-505',
            'Tags': [
                {
                    'Key': 'Owner',
                    'Value': ''
                },
                {
                    'Key': 'Name',
                    'Value': 'Instance With Empty Tag Owner'
                }
            ]
        },
    ]


def get_tags_filter():
    return {
        "Owner": "[^\s-]",  # Tag Owner with Any Value
        "product": "(^fusion-center$)"  # Tag product with value fusion-center
    }
