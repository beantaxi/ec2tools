import sys
from . import kernel
from .kernel import cli
from pprint import pprint

def BundleTaskComplete (*ids):
    waiter = cli.get_waiter('bundle_task_complete')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(BundleIds=ids)

def ConsoleOutputAvailable (idInstance):
    waiter = cli.get_waiter('console_output_available')
    waiter.wait(InstanceId=id)

def ConversionTaskCancelled (*args):
    waiter = cli.get_waiter('conversion_task_cancelled')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(ConversionTaskIds=ids)

def ConversionTaskCompleted (*args):
    waiter = cli.get_waiter('conversion_task_completed')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(ConversionTaskIds=ids)

def ConversionTaskDeleted (*args):
    waiter = cli.get_waiter('conversion_task_deleted')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(ConversionTaskIds=ids)

def CustomerGatewayAvailable (*args):
    waiter = cli.get_waiter('customer_gateway_available')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(CustomerGatewayIds)

def ExportTaskCancelled (*args):
    waiter = cli.get_waiter('export_task_cancelled')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(ExportTaskIds)

def ExportTaskCompleted(*args):
    waiter = cli.get_waiter('export_task_completed')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(ExportTaskIds)

def ImageAvailable (*args):
    waiter = cli.get_waiter('image_available')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(ImageIds)

def ImageExists (*args):
    waiter = cli.get_waiter('image_exists')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(ImageIds)

def Instance (forWhat, *args):
    waiter = cli.get_waiter(forWhat)
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(InstanceIds=ids)

def InstanceExists (*args):
    Instance('instance_exists', *args)

def InstanceRunning (*args):
    Instance('instance_running', *args)

def InstanceStatusOk (*args):
    Instance('instance_status_ok', *args)

def InstanceStopped (*args):
    Instance('instance_stopped', *args)

def InstanceTerminated (*args):
    Instance('instance_terminated', *args)

def KeyPairExists (*names):
    waiter = cli.get_waiter('key_pair_exists')
    names = kernel.toList(*names)
    waiter.wait(KeyNames=names)

def NatGatewayAvailable (*args):
    waiter = cli.get_waiter('nat_gateway_available')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(NatGatewayIds=ids)

def NetworkInterfaceAvailable (*args):
    waiter = cli.get_waiter('network_interface_available')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(NetworkInterfaceIds=ids)

def PasswordDataAvailable (id):
    waiter = cli.get_waiter('password_data_available')
    waiter.wait(InstanceId=id)

def SnapshotCompleted (*ids):
    waiter = cli.get_waiter('snapshot_completed')
    ids = kernel.toList(*ids)
    waiter.wait(SnapshotIds=ids)

def SpotInstanceRequestFulfilled (*args):
    waiter = cli.get_waiter('spot_instance_request_fulfilled')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(SpotInstanceRequestIds=ids)

def SubnetAvailable (*args):
    waiter = cli.get_waiter('subnet_available')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(SubnetIds=ids)

def SystemStatusOk (*args):
    waiter = cli.get_waiter('system_status_ok')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(InstanceIds=ids)

def Volume (forWhat, *args):
    waiter = cli.get_waiter(forWhat)
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(VolumeIds=ids)

def VolumeAvailable (*ids):
    Volume('volume_available', *ids)

def VolumeDeleted (*ids):
    Volume('volume_deleted', *ids)

def VolumeInUse (*ids):
    Volume('volume_in_use', *ids)

def VpcAvailable (*ids):
    waiter = cli.get_waiter('vpc_available')
    ids = kernel.toList(*ids)
    waiter.wait(VpcIds=ids)

def VpcPeeringConnectionExists (*args):
    waiter = cli.get_waiter('vpc_peering_connection_exists')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(VpcPeeringConnectionIds=ids)

def VpnConnectionDeleted (*args):
    waiter = cli.get_waiter('vpn_connection_available')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(VpnConnectionIds=ids)

def VpnConnectionAvailable (*args):
    waiter = cli.get_waiter('vpn_connection_deleted')
    args = kernel.toList(*args)
    ids = [kernel.getId(o) for o in args]
    waiter.wait(VpnConnectionIds=ids)
