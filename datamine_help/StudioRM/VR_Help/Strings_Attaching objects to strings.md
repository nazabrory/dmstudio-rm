# Attaching Objects to Strings

Objects are attached to traces for the purpose of creating simulation playback. Only [mobile objects](<Objects_Simulation%20objects.md>) can be attached to traces. 

Different objects with different speeds and acceleration properties may be attached to the same trace - when an object catches up to a slower, leading object, the faster object will slow to the speed of the leading object or objects to form a queue. This could be used, say, to predict in-pit vehicle jams.

When more than one object is attached to a string, a start time is specified, so that the objects start moving along the trace at specified time intervals.

For more information on simulation objects, see [VR Objects and Simulations](<Objects_Simulation%20objects.md>).

Related topics and activities

  * [VR Objects and Simulations](<Objects_Simulation%20objects.md>)

  * [Stationary VR Object types](<Objects_Stationary%20objects.md>)

  * [Placing Objects on Surfaces](<Objects_Placing_objects_on_surfaces.md>)

  * [VR Objects and Types](<VR-Objects-and-Types.md>)

  * [Create a Flythrough](<Simulation_Creating%20a%20Flythrough.md>)