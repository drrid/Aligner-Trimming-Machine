set local EnableDelayedExpansion
set Folder=C:\Users\user\Desktop\Process\deltaface-pts
for %%f in ( "%Folder%"\* ) do ("C:\Program Files\CloudCompare\cloudcompare.exe" -SILENT -C_EXPORT_FMT ASC -O %Folder%\%%~nxf -SS SPATIAL 2)