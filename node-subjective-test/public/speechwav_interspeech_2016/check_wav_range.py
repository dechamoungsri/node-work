import wave
import contextlib

base = 'tscsdj01'

fname = './02_GPR_partofspeech/{}.wav'.format(base)
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print(duration)

fname = './01_GPR_multi_level_phone_gen/{}.wav'.format(base)
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print(duration)