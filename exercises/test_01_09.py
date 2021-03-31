def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert type(nucleotides) == dict, "Are you sure it's a dictionary?"
    assert sum(nucleotides.values()) == len(DNA), "Did you include all the nucleotides?"

    __msg__.good("Well done!")
