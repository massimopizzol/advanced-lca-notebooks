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