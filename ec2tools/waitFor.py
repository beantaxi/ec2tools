import sys
from . import _kernel
from ._kernel import cli

def BundleTaskComplete (*ids):
    waiter = cli.get_waiter('bundle_task_complete')
    ids = _kernel.toList(*ids)
    waiter.wait(BundleIds=ids)

def ConsoleOutputAvailable (idInstance):
    waiter = cli.get_waiter('console_output_available')
    waiter.wait(InstanceId=id)

def ConversionTaskCancelled (*ids):
    waiter = cli.get_waiter('conversion_task_cancelled')
    ids = _kernel.toList(*ids)
    waiter.wait(ConversionTaskIds=ids)

def ConversionTaskCompleted (*ids):
    waiter = cli.get_waiter('conversion_task_completed')
    ids = _kernel.toList(*ids)
    waiter.wait(ConversionTaskIds=ids)

def ConversionTaskDeleted (*ids):
    waiter = cli.get_waiter('conversion_task_deleted')
    ids = _kernel.toList(*ids)
    waiter.wait(ConversionTaskIds=ids)

def CustomerGatewayAvailable (*ids):
    waiter = cli.get_waiter('customer_gateway_available')
    ids = _kernel.toList(*ids)
    waiter.wait(CustomerGatewayIds)

def ExportTaskCancelled (*ids):
    waiter = cli.get_waiter('export_task_cancelled')
    ids = _kernel.toList(*ids)
    waiter.wait(ExportTaskIds)

def ExportTaskCompleted(*ids):
    waiter = cli.get_waiter('export_task_completed')
    ids = _kernel.toList(*ids)
    waiter.wait(ExportTaskIds)

def ImageAvailable (*ids):
    waiter = cli.get_waiter('image_available')
    ids = _kernel.toList(*ids)
    waiter.wait(ImageIds)

def ImageExists (*ids):
    waiter = cli.get_waiter('image_exists')
    ids = _kernel.toList(*ids)
    waiter.wait(ImageIds)

def Instance (forWhat, *ids):
    waiter = cli.get_waiter(forWhat)
    ids = _kernel.toList(*ids)
    waiter.wait(InstanceIds=ids)

def InstanceExists (*ids):
    Instance('instance_exists', *ids)

def InstanceRunning (*ids):
    Instance('instance_running', *ids)

def InstanceStatusOk (*ids):
    Instance('instance_status_ok', *ids)

def InstanceStopped (*ids):
    Instance('instance_stopped', *ids)

def InstanceTerminated (*ids):
    Instance('instance_terminated', *ids)

def KeyPairExists (*names):
    waiter = cli.get_waiter('key_pair_exists')
    names = _kernel.toList(*names)
    waiter.wait(KeyNames=names)

def NatGatewayAvailable (*ids):
    waiter = cli.get_waiter('nat_gateway_available')
    ids = _kernel.toList(*ids)
    waiter.wait(NatGatewayIds=ids)

def NetworkInterfaceAvailable (*ids):
    waiter = cli.get_waiter('network_interface_available')
    ids = _kernel.toList(*ids)
    waiter.wait(NetworkInterfaceIds=ids)

def PasswordDataAvailable (id):
    waiter = cli.get_waiter('password_data_available')
    waiter.wait(InstanceId=id)

def SnapshotCompleted (*ids):
    waiter = cli.get_waiter('snapshot_completed')
    ids = _kernel.toList(*ids)
    waiter.wait(SnapshotIds=ids)

def SpotInstanceRequestFulfilled (*ids):
    waiter = cli.get_waiter('spot_instance_request_fulfilled')
    ids = _kernel.toList(*ids)
    waiter.wait(SpotInstanceRequestIds=ids)

def SubnetAvailable (*ids):
    waiter = cli.get_waiter('subnet_available')
    ids = _kernel.toList(*ids)
    waiter.wait(SubnetIds=ids)

def SystemStatusOk (*ids):
    waiter = cli.get_waiter('system_status_ok')
    ids = _kernel.toList(*ids)
    waiter.wait(InstanceIds=ids)

def Volume (forWhat, *ids):
    waiter = cli.get_waiter(forWhat)
    ids = _kernel.toList(*ids)
    waiter.wait(VolumeIds=ids)

def VolumeAvailable (*ids):
    Volume('volume_available', *ids)

def VolumeDeleted (*ids):
    Volume('volume_deleted', *ids)

def VolumeInUse (*ids):
    Volume('volume_in_use', *ids)

def VpcAvailable (*ids):
    waiter = cli.get_waiter('vpc_available')
    ids = _kernel.toList(*ids)
    waiter.wait(VpcIds=ids)

def VpcPeeringConnectionExists (*ids):
    waiter = cli.get_waiter('vpc_peering_connection_exists')
    ids = _kernel.toList(*ids)
    waiter.wait(VpcPeeringConnectionIds=ids)

def VpnConnectionDeleted (*ids):
    waiter = cli.get_waiter('vpn_connection_available')
    ids = _kernel.toList(*ids)
    waiter.wait(VpnConnectionIds=ids)

def VpnConnectionAvailable (*ids):
    waiter = cli.get_waiter('vpn_connection_deleted')
    ids = _kernel.toList(*ids)
    waiter.wait(VpnConnectionIds=ids)
