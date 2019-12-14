from tabulate import tabulate
class Version1_pinouts:
    Pot_1=2
    Pot_2=3
    Pot_3=4
    Hall_effect_1=1
    Hall_effect_2=0
    LDR=5
    Thermistor_1=6
    Thermistor_2=7
    PIR=2
    Sw_tactile=3
    Buzzer=5
    B_led=6
    G_led=9
    R_led=10
    Ac_relay=8
    
    @staticmethod
    def print_pinouts():
        keys = [attr for attr in dir(Version1_pinouts) if not callable(getattr(Version1_pinouts, attr)) and not attr.startswith("__")]
        headers = ["Peripheral Name", "GPIO"]
        variables=[]
        for items in keys:
            variables.append([items,(vars(Version1_pinouts)[items])])
        print(tabulate(variables,headers,tablefmt="grid"))
