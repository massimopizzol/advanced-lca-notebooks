# Error & Solution

- **Error Message**:
    ```
    OutsideTechnosphere: Can't find key 162531024708575232 in product dictionary
    ```
    - The activity/exchange id in technosphere is wrong, check if you provide the correct id.

- **Error Message**:
    ```
    File /opt/miniconda3/envs/bw2.5/lib/python3.11/site-packages/bw2data/utils.py:384, in get_node(**kwargs)
        382     raise MultipleResults("Found {} results for the given search".format(len(candidates)))
        383 elif not candidates:
    --> 384     raise UnknownObject
        385 return candidates[0]

    UnknownObject: 
    ```
    -  The activity/exchange code is wrong, check if you provide the correct code.

- **Error Message**:
    ```
    OperationalError: database is locked
    ```
    - You used the database multiple times at the same time. Restart the kernel, run it again. Remember to perform the next database operation after the previous one is completed.

- **Error Message**:
    ```
    UnknownObject: Exchange between ('ecoinvent 3.9 conseq', 'cea1e434115aa84cbfd7dc3086b61e80') and ('exldb', 'Fuel production') is invalid - one of these objects is unknown (i.e. doesn't exist as a process dataset)
    ```
    - Check your foreground system. 

- **Error Message**:
    ```
    MaybeEncodingError: Error sending result: '<multiprocessing.pool.ExceptionWithTraceback object at 0x000001E3A9825E50>'. Reason: 'TypeError("cannot pickle 'lxml.etree._ListErrorLog' object")'
    ```
    1. Delete the failed import databases
    ```
    del bd.databases["ecoinvent-3.11-biosphere"] # enter the database name you want to delete
    del bd.databases["ecoinvent-3.11-consequential"] # enter the database name you want to delete
    ```
    2.  use the following code to import again
    ```
    bi.import_ecoinvent_release(
        version='3.11',
        system_model='consequential',
        username=<enter your username>
        password=<enter your password>
        use_mp=False
    )
    ```
    3. If you encounter the following error, go to the path, delete the databases, unzip it manually.
    ```
    File ~\AppData\Local\pylca\EcoinventInterface\ecoinvent 3.11_consequential_ecoSpold02\datasets...
    XMLSyntaxError: Document is empty, line 1, column 1
    ```
    4. If you encounter the following error afterwards, follow the instruction, delete the file manually.
    ```
    C:\Users\xxx\AppData\Local\anaconda3\envs\brightway\Lib\site-packages\ecoinvent_interface\release.py:238 UserWarning: Can't automatically delete C:\Users\xxx\AppData\Local\pylca\EcoinventInterface\cache\ecoinvent 3.11_LCIA_implementation.7z
    Please delete manually
    warnings.warn(message)
    ```


