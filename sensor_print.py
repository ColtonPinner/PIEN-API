from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=17, trigger=4)
ultrasonic.distance
while True:
    ultrasonic.wait_for_in_range()
    print("In range")
    ultrasonic.wait_for_out_of_range()
    print("Out of range")
