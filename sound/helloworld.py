


import winsound
#frequency = 5000  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
wav="applause.wav"

def getFrequency(note, A4=440):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    octave = int(note[2]) if len(note) == 3 else int(note[1])

    keyNumber = notes.index(note[0:-1]);

    if (keyNumber < 3):
        keyNumber = keyNumber + 12 + ((octave - 1) * 12) + 1;
    else:
        keyNumber = keyNumber + ((octave - 1) * 12) + 1;

    return int(A4 * 2 ** ((keyNumber - 49) / 12))


print(getFrequency("C4"))
print(getFrequency("D4"))
print(getFrequency("E4"))
print(getFrequency("F4"))
print(getFrequency("G4"))
print(getFrequency("A4"))
print(getFrequency("B4"))
print(getFrequency("C5"))


"""
#winsound.Beep(frequency, duration)
winsound.Beep(getFrequency("C4"), duration)
winsound.Beep(getFrequency("D4"), duration)
winsound.Beep(getFrequency("E4"), duration)
winsound.Beep(getFrequency("F4"), duration)
winsound.Beep(getFrequency("G4"), duration)
winsound.Beep(getFrequency("A4"), duration)
winsound.Beep(getFrequency("B4"), duration)
winsound.Beep(getFrequency("C5"), duration)
"""
winsound.PlaySound(wav, winsound.SND_FILENAME)
winsound.PlaySound("lose.wav", winsound.SND_FILENAME)

#print("This line will be printed.")

#a = input("enter a")
#b = input("enter b")
#print(int(a)+int(b))

