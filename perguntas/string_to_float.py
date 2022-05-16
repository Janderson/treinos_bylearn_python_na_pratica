print(float("2.1a"))


try: 
    number = float("2.1")
except ValueError as v_err:
    print(v_err)
