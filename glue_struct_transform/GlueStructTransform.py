import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from utils import working_with_types

class GlueStructTransform:
    """
    Instantiate a GlueStructTransform operation.
    
    This is the glue transform class, you  can call the function that converts:
    - Json Schema > Glue Struct
    """

    def __init__(self):
        pass


    def json_schema_to_glue_struct(jsonSchemaLoadProp:dict, *args, **kwargs)->str:
        """
        This function performs a loop for each data inside the json schema to understand the data type and return a string in the glue structure format at the end.
        """

        objectField = kwargs.get('objectField', None)
        fullSchema = kwargs.get('fullSchema', False)

        if fullSchema == False: 
            loopJsonSchemaLoadProp = jsonSchemaLoadProp['properties'][f'{objectField}']['properties']
        elif fullSchema == True:
            loopJsonSchemaLoadProp = jsonSchemaLoadProp['properties']

        tempStruct = ""
        for item in loopJsonSchemaLoadProp:
            result = working_with_types(item, loopJsonSchemaLoadProp)
            tempStruct += result

        if fullSchema == False: 
            finalGlueStruct = f"struct<{tempStruct[:-1]}>"
        elif fullSchema == True:
            finalGlueStruct =  tempStruct[:-1]

        return finalGlueStruct