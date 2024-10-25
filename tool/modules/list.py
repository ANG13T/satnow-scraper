def list_subsystems():
    """List all available subsystems."""
    return [subsystem.name for subsystem in SUBSYSTEMS]

def list_sub_subsystems(subsystem):
    """List all available component types for a subsystems"""
    pass