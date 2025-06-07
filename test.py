from cc3d.core.PyCoreSpecs import PyCoreSpecs

def load_simulation_from_xml(xml_file_path):
    # Create a PyCoreSpecs object
    core_specs = PyCoreSpecs()

    # Use the from_xml function to load the simulation specifications from an XML file
    core_specs.from_xml(xml_file_path)

    # Now you can work with the core_specs object, which contains the loaded simulation specifications
    print("Simulation specifications loaded successfully from:", xml_file_path)

# Example usage
xml_file_path = 'example.xml'
load_simulation_from_xml(xml_file_path)
