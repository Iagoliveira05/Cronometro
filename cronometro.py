from time import sleep

def cronometro(min, seg):
    m, s = min, seg
    while True:
        if m < 10:
            min_sec_format = f"0{m}:{s}"
        if s < 10:
            min_sec_format = f"{m}:0{s}"
        if m < 10 and s < 10:
            min_sec_format = f"0{m}:0{s}"

        print(min_sec_format)
        sleep(1)

        if m != 0 and s == 0:
            s = 60
            m -= 1
        
        elif m == 0 and s == 0:
            break

        s -= 1

cronometro(1, 5)
