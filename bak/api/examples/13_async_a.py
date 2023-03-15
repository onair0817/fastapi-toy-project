def gen_int_and_print(name: str, a: int):
    try:
        for i in range(a):
            yield i
            print(name, " ::: ", i)
    except Exception as e:
        print(e)
    finally:
        print(name, " done")


def main_event_loop(gens):
    while gens:
        try:
            for i, generator in enumerate(gens):
                next(generator)
        except StopIteration:
            del gens[i]
        except Exception as e:
            print(e)
    print("loop end")


if __name__ == "__main__":
    names = [("i", 2), ("j", 3), ("k", 4)]
    gens = [gen_int_and_print(name, a) for name, a in names]
    main_event_loop(gens)
