class Clock:
    def __init__(self, hour : int, minute : int):
        self.hour = hour
        self.minute = minute

    def get_clock(self, time: tuple) -> str:
        clock = tuple()

        for time_unit in time:
            if time_unit >= 0 and time_unit < 10:
                clock += ("0{}".format(time_unit),)
            else:
                clock += ("{}".format(time_unit),)

        return ":".join(clock)

    def get_time(self) -> str:
        if self.minute > 59 or self.minute < 0:
            if self.hour >= 0 and self.hour < 24: 
                self.hour += int(((self.minute - (self.minute % 60)) / 60) % 24)
                self.minute %= 60
            else:
                self.hour = (self.hour % 24) + int(((self.minute - (self.minute % 60)) / 60) % 24)
                self.minute %= 60

        if self.hour >= 0 and self.hour < 24:
            return self.get_clock((self.hour, self.minute))
        else:
            return self.get_clock((self.hour % 24, self.minute))

    def __repr__(self) -> str:
        return self.get_time()

    def __eq__(self, other):
        return self.get_time() == other.get_time()

    def __add__(self, minutes):
        self.minute += minutes

        return self.get_time()

    def __sub__(self, minutes):
        self.minute -= minutes

        return self.get_time()
