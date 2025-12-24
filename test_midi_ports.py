import mido
import time
print("\n\n")
print("\t\t##########################")
print("\t\t## __  __  _   _  ____  ##")
print("\t\t##|  \\/  || \\ | ||  _ \\ ##")
print("\t\t##| |\\/| ||  \\| || |_) |##")
print("\t\t##| |  | || |\\  ||  _ < ##")
print("\t\t##|_|  |_||_| \\_||_| \\_\\##")
print("\t\t##########################")
print("\t\t##### TEST MIDI PORTS ####")
print("\t\t##########################")
print("\n\n")
ports = mido.get_output_names()
for i,p in enumerate(ports):
    print(f"\t{i} | Port: '{p}'")

if not ports:
    print("\n\n\t (!!!) ERROR: Python did not detect MIDI ports\n\n")
    exit(1)

nports = len(ports) -1
selection = input(f"\t\nPlease select a port (0-{nports}): ")

if selection.isdigit() and 0 <= int(selection) <= nports:
    port_name = ports[int(selection)]
else:
    print(f"\t\n (!!!) Invalid input. Please enter a single digit between 0 and {nports}.\n\n")
    exit(1)

print(f"\n\t ---> TESTING PORT: {port_name} <---\n")

try:
    with mido.open_output(port_name) as port:
        for channel in range(1, 16):
            print(f"Sending note on channel {channel}...")
                
            # mido channels 0-15 (channel 0 = 1)
            port.send(mido.Message('note_on', note=60, velocity=100, channel=channel-1))
            time.sleep(0.5)
            port.send(mido.Message('note_off', note=60, channel=channel-1))
    print("\n\n\t did you hear the note?")

except Exception as e:
    print(f"\t\n (!!!) Error opening port {port_name}: {e}")

