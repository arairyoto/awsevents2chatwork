from functools import reduce

def flatten(d, reducer=None):
    """
    method to flatten dict object
    
    Parameters
    ----------
    d : dict
        target dict object
    reducer : function
        function to reduce tupled key
    
    Returns
    -------
    flatten_dict : dict
        flatten dict of d
        if reducer is None, it'll return tuple as a key
        if reducer is defined, it'll return reduced tuple as a key
    """
    flatten_dict = {}
    def loop(d, tupled_key=()):
        print(tupled_key)
        if type(d) is dict:
            for key, value in d.items():
                updated_tupled_key = tupled_key + (key,)
                flatten_dict.update(
                    {
                        updated_tupled_key: value
                    }
                )
                loop(value, updated_tupled_key)
        elif type(d) is list:
            for key, value in enumerate(d):
                updated_tupled_key = tupled_key + (key,)
                flatten_dict.update(
                    {
                        updated_tupled_key: value
                    }
                )
                loop(value, updated_tupled_key)
        else:
            flatten_dict.update(
                {
                    tupled_key: d
                }
            )
    loop(d)
    if reducer:
        _flatten_dict = {}
        for tupled_key, value in flatten_dict.items():
            _flatten_dict[reduce(reducer, tupled_key, None)] = value
        return _flatten_dict
    return flatten_dict

