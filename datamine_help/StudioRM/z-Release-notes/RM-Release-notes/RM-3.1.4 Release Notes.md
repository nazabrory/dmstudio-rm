# Studio RM 3.1 (Update 4) Release Notes

This is an unscheduled maintenance release to provide urgent software changes for customers outside of the typical release program cadence. When installing this software, it is recommended that you uninstall any previous copies of Studio RM beforehand.

## All Improvements

### Commands & Processes

  * CORE-10156 You can now specify a reference surface when using the MAKEDTM process.

  * CORE-10109 We have improved the Cut and Fill tool to automatically filter out tiny noise solids where surfaces match, giving you cleaner, more meaningful results without sacrificing accuracy in mined areas.

  * CORE-10108 We have added an option in Make DTM to reuse triangulation from a reference surface so overlapping areas with identical XYZ data generate exactly the same triangles for highly consistent volumes.

  * CORE-10101 The **MAKEDTM** process has a new parameter (@DIAGONAL) to emulate the "Make Diagonals Consistent" switch of the interactive dtm-create screen.

    * CORE-10034 The "Make Diagonals Consistent" DTM feature is now accessible from a script.

### Other Changes

  * CORE-10117 The minimum amount permitted for solid volume removal during cut and fill operations is now 0.05 (previously 0).