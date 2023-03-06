import pyCloudCompare as cc

cli = cc.CloudCompareCLI()
cmd = cli.new_command()
cmd.silent()  # Disable console
cmd.open("1.stl")  # Read file
cmd.sample_mesh(cc.SAMPLE_METHOD.POINTS, parameter=1000000)
cmd.cloud_export_format(cc.CLOUD_EXPORT_FORMAT.ASCII, extension="xyz")
cmd.subsampling(cc.SS_ALGORITHM.SPATIAL, parameter=2)
cmd.save_clouds("newPointcloud.xyz")
print(cmd)
cmd.execute()