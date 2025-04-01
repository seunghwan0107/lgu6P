
def outer_func(msg):
    def inner_fuc():
        # print(f"메세지: {msg}")
        print("메세지")

    return inner_fuc

closure = outer_func("안녕하세요")
closure()