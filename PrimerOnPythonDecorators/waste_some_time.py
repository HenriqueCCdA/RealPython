from decorators import timer, debug


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(2000)])

waste_some_time(1)


class TimeWaster:

    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
