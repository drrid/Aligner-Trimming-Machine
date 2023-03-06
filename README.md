# Aligner-Trimming-Machine

1)Software:
  - When exporting STL files in Onyxceph, add base as 3D object
  - Export trimming curve for some steps
  - Execute cc.py
  - import generated curve in Rhino, execute macro 'ccrelative0'='! SelAll  Rotate 0,0,0 -90  SelAll CurveThroughPt   Enter    Delete    SelAll CopyToClipboard  Paste smooth enter      ExtrudeCrv   3    Enter   SelAll    Mirror  copy=no  0,0,0  90,0,0    SelAll  Rotate3D  0,0,0  90,0,0  90'
  
  - in RhinoCAM: 
      - import post processor 'grbl-custom-relative.spm'
      - Machine 4 axis, table, -Y
      - import aligner.vkb in RhinoCAM
      - generate gcode
      - execute post-process-axis.py
      - upload gcode to Octoprint
      
  
2)Hardware:
  - use laser to calibrate E axis
  
