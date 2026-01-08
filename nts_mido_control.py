import mido
import time
import random
import argparse

try:
    parser = argparse.ArgumentParser(description='MIDI ARP\n Python script that implements the midio library to play MIDI Music.')
    parser.add_argument('-p', '--port', type=str, help='Port Name', required=False)
    parser.add_argument('-c', '--channel', type=int, help='Channel number', required=False)
    args = parser.parse_args()

    channel = args.channel if args.channel else 1
    port_param = args.port if args.port else "NTS"

    # 1. Search MIDI port
    ports_list = mido.get_output_names()
    port_name = next((p for p in ports_list if port_param in p), None)

    if not port_name:
        print("\n\n\t (!!!) ERROR: MIDI Port not detected\n\n")
        exit()

    # Conf Arps
    note_key = 53  # Do
    note_duration = 0.15 # Arp Vel
    scale = [0, 3, 7, 10, 12] # Minor blues scale (intervals)


    print(f"\n\t ---> Port Active: {port_name} - Channel: {channel}")
                
    with mido.open_output(port_name) as port:
        try:
            #print(f"\t ---> Sending OSC (53): tri (18) ")
            print(f"\t ---> Sending OSC (53): waves (72) ")
            port.send(mido.Message('control_change', control=53, value=72, channel=channel))                
                        
            
            print(f"\t ---> Starting ARP")
            
            shape_val = 0
            while True:
                interval = random.choice(scale)
                octave = random.choice([-12, 0, 12, 24])
                
                note = note_key + interval + octave
                
                #Shape change
                port.send(mido.Message('control_change', control=54, value=shape_val, channel=channel))                
            
                            
                # Nota ON
                port.send(mido.Message('note_on', note=note, velocity=90, channel=channel))
                
                time.sleep(note_duration)
                
                # Nota OFF
                port.send(mido.Message('note_off', note=note, channel=channel))
                
                shape_val = random.randint(0, 127)
                
        except KeyboardInterrupt:
            port.send(mido.Message('note_off', note=note, channel=channel))
            print(f"\t ---> ARP Stop")

except Exception as e:
    print(f"\n\n\t (!!!) ERROR: {e}")
