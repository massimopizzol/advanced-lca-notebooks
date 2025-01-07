
# Import brightway2.5 packages
import bw2calc as bc
import bw2data as bd
import bw2io as bi

# Based on work by Ning An (https://vbn.aau.dk/en/persons/ningan)

# Before importing ecoinvent, we need to make a default setup of Brightway2.5. 
# This means importing all the environmental exchanges and all the LCIA methods. 
# Then when we import ecoinvent the ecoinvent activities will be linked to this database of environmental exchanges

PROJECT_NAME = "import-ei-oldway" # Set working project name as a variable.

# Import the biosphere database while creating the project. (In bw2.5, those two processes are merged.)
if PROJECT_NAME in bd.projects:
    # ATTENTION: "overwrite_existing=True" will overwrite the project which means all the old databases under this project will be deleted. 
    bi.remote.install_project('ecoinvent-3.9.1-biosphere', PROJECT_NAME, overwrite_existing=True) # Select the biosphere version accordingly.
else:
    bi.remote.install_project('ecoinvent-3.9.1-biosphere', PROJECT_NAME)



bd.projects.set_current('import-ei-oldway') # Still working in the same project
bd.databases


# Import ecoinvent
importer = bi.SingleOutputEcospold2Importer(
    dirpath='/Users/massimo/Documents/Databases/ecoinvent v3.9.1/ecoinvent 3.9.1_consequential_ecoSpold02/datasets', # Enter your own local directory of ecoinvent.
    db_name='ecoinvent 3.9.1 conseq'
)
importer.apply_strategies()
importer.write_database()
importer.statistics()

bd.projects.set_current('import-ei-oldway') # Still working in the same project
bd.databases

